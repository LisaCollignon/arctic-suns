from app import db


class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    person_id = db.Column(db.Integer, nullable=False)
    workday = db.Column(db.Date)
    start_hour = db.Column(db.Time)
    end_hour = db.Column(db.Time)
    type_day = db.Column(db.String(20))
    total_leave_days = db.Column(db.Integer)
    extra_hours = db.Column(db.Integer)
