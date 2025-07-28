from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime, timedelta

app = Flask(__name__)

# Dummy data
horses = ["Dusty", "Willow", "Rocket"]
availability = {
    "Monday": ["16:00", "16:45", "17:30", "18:15", "19:00"],
    "Tuesday": ["16:00", "16:45", "17:30", "18:15", "19:00"],
    "Wednesday": ["16:00", "16:45", "17:30", "18:15", "19:00"],
    "Friday": ["16:00", "16:45", "17:30"]
}
bookings = []

@app.route('/')
def booking_form():
    return render_template('booking.html', horses=horses, availability=availability)

@app.route('/book', methods=['POST'])
def book():
    name = request.form['name']
    email = request.form['email']
    day = request.form['day']
    time = request.form['time']
    horse = request.form['horse']
    bookings.append({
        "name": name,
        "email": email,
        "day": day,
        "time": time,
        "horse": horse
    })
    return render_template('confirmation.html', name=name, venmo="@cassandragood34")

@app.route('/admin')
def admin():
    return render_template('admin.html', bookings=bookings)

if __name__ == '__main__':
    app.run(debug=True)