from flask import current_app
from app import db
from sqlalchemy import DateTime


class Task(db.Model):
    task_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    completed_at = db.Column(db.DateTime, nullable=True)

    # creates a dictionary of key-value pairs describing the given task
    def to_json(self):
        return {
            "task_id": self.task_id,
            "title": self.title,
            "description": self.description
        }
