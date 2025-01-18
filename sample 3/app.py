import cv2
import pytesseract
from flask import Flask, render_template, Response, request, jsonify
from PIL import Image
from textblob import TextBlob
import numpy as np
from transformers import pipeline
from googletrans import Translator

app = Flask(__name__, static_url_path='/static', static_folder='static')

# Text Extraction route
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/text_extraction', methods=['GET', 'POST'])
def text_extraction():
    if request.method == 'POST':
        if 'file' not in request.files:
            return render_template('text_extraction.html', error="No file part")

        file = request.files['file']

        if file.filename == '':
            return render_template('text_extraction.html', error="No selected file")

        try:
            # Read the image
            nparr = np.frombuffer(file.read(), np.uint8)
            img = cv2.imdecode(nparr, cv2.IMREAD_UNCHANGED)

            # Perform text detection using pytesseract
            text = pytesseract.image_to_string(img)

            return render_template('text_extraction.html', error=None, text=text)

        except Exception as e:
            return render_template('text_extraction.html', error=f"Error processing image: {e}", text=None)

    return render_template('text_extraction.html', error=None, text=None)


# Sentiment Analysis route
@app.route('/sentiment_analysis', methods=['GET', 'POST'])
def sentiment_analysis():
    if request.method == 'POST':
        text = request.form.get('sentiment_text')
        if text:
            result = analyze_sentiment_text(text)
            return render_template('sentiment_analysis.html', text=text, result=result)

    return render_template('sentiment_analysis.html', text=None, result=None)

def analyze_sentiment_text(text):
    analysis = TextBlob(text)
    
    # Define a threshold for sentiment polarity
    threshold = 0.0
    
    if analysis.sentiment.polarity > threshold:
        return "Positive Impact"
    elif analysis.sentiment.polarity < threshold:
        return "Negative Impact"
    else:
        return "Neutral Impact"

# Text Summarization route
@app.route('/text_summarization', methods=['GET', 'POST'])
def text_summarization():
    if request.method == 'POST':
        paragraph = request.form['paragraph']
        summary = get_summary(paragraph)
        return render_template('text_summarization.html', paragraph=paragraph, summary=summary)
    return render_template('text_summarization.html', paragraph='', summary='')

def get_summary(paragraph):
    summarizer = pipeline("summarization")
    summary = summarizer(paragraph, max_length=150, min_length=50, length_penalty=2.0, num_beams=4, early_stopping=True)
    return summary[0]['summary_text']

# Language Converter route
@app.route('/language_converter')
def language_converter():
    return render_template('language_converter.html')

@app.route('/translate', methods=['POST'])
def translate():
    input_text = request.form['inputText']
    selected_language = request.form['languageSelector']

    if not input_text:
        return render_template('language_converter.html', error="Please enter some text.")

    try:
        translator = Translator()
        translated_text = translator.translate(input_text, dest=selected_language).text
        return render_template('language_converter.html', translated_text=f"Translated Text ({selected_language}): {translated_text}")
    except Exception as e:
        return render_template('language_converter.html', error=f"Translation failed. Error: {str(e)}")

# Camera OCR route
cap = cv2.VideoCapture(0)

def capture_and_ocr():
    while True:
        # Capture a frame
        ret, frame = cap.read()

        # Convert the frame to grayscale for better OCR accuracy
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Use Tesseract to extract text
        text = pytesseract.image_to_string(gray)

        # Display the captured frame
        cv2.imshow('Camera OCR', frame)

        # Break the loop if 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        yield f"data:{text}\n\n"

    # Release the camera and close all OpenCV windows
    cap.release()
    cv2.destroyAllWindows()

@app.route('/ocr', methods=['GET', 'POST'])
def ocr():
    return render_template('ocr.html')

@app.route('/video_feed')
def video_feed():
    return Response(capture_and_ocr(), mimetype='text/event-stream')

if __name__ == '__main__':
    app.run(debug=True)
