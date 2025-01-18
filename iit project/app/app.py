from flask import Flask, render_template, redirect, url_for, request, session,flash
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from models import BookingRequest, db, User, Service, ServiceRequest, Review, Professional # Import all models 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SECRET_KEY'] = 'mysecretkey'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db.init_app(app)

# Create tables within application context
def init_db():
    with app.app_context():
        db.drop_all()  # Drop all tables first to ensure clean slate
        db.create_all()  # Create all tables
        print("Database tables created successfully.")

@app.route('/')
def home():
     # Hardcoded services for the homepage
    services = [
        {"name": "Plumbing", "description": "Fix leaks, pipes, and more!", "price": 50},
        {"name": "Electrician", "description": "Electrical repairs and installations.", "price": 70},
        {"name": "House Cleaning", "description": "Professional cleaning services.", "price": 40},
        {"name": "Gardening", "description": "Maintain your garden and lawn.", "price": 60},
    ]
    return render_template('home.html', services=services)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            session['role'] = user.role
            if user.role == 'admin':
                return redirect(url_for('admin_dashboard'))
            elif user.role == 'professional':
                return redirect(url_for('professional_dashboard'))
            else:
                return redirect(url_for('home'))
        else:
            flash("Invalid credentials. Please try again.", "danger")
    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        role = request.form['role']
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
        new_user = User(username=username, password=hashed_password, role=role)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/admin_dashboard')
def admin_dashboard():
    if session.get('role') != 'admin':
        return redirect(url_for('home'))
    
    # Fetch all users from the database
    users = User.query.all()

    professionals = Professional.query.all()
    
    # Hardcoded services for the "Existing Services" section
    services = [
        {"name": "Plumbing", "description": "Fix leaks, pipes, and more!", "price": 50},
        {"name": "Electrician", "description": "Electrical repairs and installations.", "price": 70},
        {"name": "House Cleaning", "description": "Professional cleaning services.", "price": 40},
        {"name": "Gardening", "description": "Maintain your garden and lawn.", "price": 60},
    ]
    
    return render_template('admin_dashboard.html', users=users,professionals=professionals, services=services)

@app.route('/delete_user', methods=['POST'])
def delete_user():
    if session.get('role') != 'admin':
        return redirect(url_for('home'))

    # Get the user ID from the form data
    user_id = request.form.get('user_id')

    if user_id:
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        flash("User deleted successfully.", "success")
        return redirect(url_for('admin_dashboard'))

    flash("Invalid user ID.", "danger")
    return redirect(url_for('admin_dashboard'))


@app.route('/delete_professional', methods=['POST'])
def delete_professional():
    if session.get('role') != 'admin':
        return redirect(url_for('home'))

    # Get the professional ID from the form data
    professional_id = request.form.get('professional_id')

    if professional_id:
        professional = Professional.query.get_or_404(professional_id)
        db.session.delete(professional)
        db.session.commit()
        flash("Professional deleted successfully.", "success")
        return redirect(url_for('admin_dashboard'))

    flash("Invalid professional ID.", "danger")
    return redirect(url_for('admin_dashboard'))


@app.route('/professional_dashboard', methods=['GET', 'POST'])
def professional_dashboard():
    if session.get('role') != 'professional':
        return redirect(url_for('login'))

    if request.method == 'POST':
        name = request.form['name']
        skill = request.form['skill']
        experience = request.form['experience']
        contact = request.form['contact']
        professional = Professional(name=name, skill=skill, experience=experience, contact=contact)
        db.session.add(professional)
        db.session.commit()
        flash("You are registered successfully!", "success")
        return redirect(url_for('professional_dashboard'))

    services = Service.query.all()  # Fetch services for the skill dropdown
    return render_template('professional_dashboard.html', services=services)


@app.route('/add_service', methods=['GET', 'POST'])
def add_service():
    if 'role' in session and session['role'] == 'admin':
        if request.method == 'POST':
            name = request.form['name']
            price = float(request.form['price'])
            description = request.form['description']
            new_service = Service(name=name, price=price, description=description)
            db.session.add(new_service)
            db.session.commit()
            return redirect(url_for('home'))
        return render_template('add_service.html')
    return redirect(url_for('home'))  # Redirect if not admin

@app.route('/book_slot', methods=['GET', 'POST'])
def book_slot():
    # Restrict access to logged-in users
    if 'user_id' not in session:
        flash("Please log in to access the booking page.")
        return redirect(url_for('login'))

    # Hardcoded services for dropdown
    services = ["Plumbing", "Electrician", "House Cleaning", "Gardening"]

    if request.method == 'POST':
        service_name = request.form['service']
        time_slot = request.form['time_slot']
        user_id = session['user_id']

        # Check if the selected time slot for the service is already booked
        existing_booking = BookingRequest.query.filter_by(service_name=service_name, time_slot=time_slot).first()
        if existing_booking:
            flash(f"The time slot '{time_slot}' for '{service_name}' is already booked. Please choose another slot.")
        else:
            # Save the booking in the database
            new_booking = BookingRequest(service_name=service_name, time_slot=time_slot, user_id=user_id)
            db.session.add(new_booking)
            db.session.commit()
            flash(f"Booking confirmed for {service_name} at {time_slot}!")

    return render_template('book_slot.html', services=services)


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))

if __name__ == '__main__':
    init_db()  # Initialize database before running app
    app.run(debug=True)
