from datetime import datetime
from app import db


class FormSubmission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    problem_description = db.Column(db.String(300), nullable=False)
    device_serial_number = db.Column(db.String(255), nullable=False)
    indicator_light1 = db.Column(db.String(255), nullable=False)
    indicator_light2 = db.Column(db.String(255), nullable=False)
    indicator_light3 = db.Column(db.String(255), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    response_status = db.Column(db.String(255))

    def __repr__(self):
        return f'<FormSubmission {self.id}>'
