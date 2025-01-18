from app import db, Service, app  # Import the database and Service model

# Example services to add to the database
services = [
    Service(name="Cleaning", price=500, description="Professional house cleaning services."),
    Service(name="Electrician", price=800, description="Licensed electricians for household issues."),
    Service(name="Plumber", price=700, description="Expert plumbing services for leaks and repairs."),
    Service(name="Laundry", price=300, description="Efficient and affordable laundry services."),
    Service(name="WiFi Setup", price=1000, description="Home WiFi setup and troubleshooting."),
]

with app.app_context():  # Required to access the Flask application and database
    db.session.add_all(services)
    db.session.commit()  # Commit the changes to the database
    print("Services added successfully.")
