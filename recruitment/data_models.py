# import db
from recruitment import db


class Listing(db.Model):
    # schema for the Listing model
    id = db.Column(db.Integer, primary_key=True)
    job_title = db.Column(db.String(100), nullable=False)
    salary = db.Column(db.Integer, nullable=False)
    location = db.Column(db.String(100), nullable=False)
    company = db.Column(db.String(100), nullable=False)
    experience_required = db.Column(db.Text, nullable=False)
    job_description = db.Column(db.Text, nullable=False)
    requirements = db.Column(db.Text, nullable=False)
    benefits = db.Column(db.Text, nullable=False)
    applicants = db.relationship(
        "Applicant", backref="listing", cascade="all, delete", lazy=True
    )

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.job_title


class Applicant(db.Model):
    # schema for the Applicant model
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    experience_level = db.Column(db.String(50), nullable=False)
    personal_statement = db.Column(db.Text, nullable=False)
    education = db.Column(db.Text, nullable=False)
    work_experience = db.Column(db.Text, nullable=False)
    listing_id = db.Column(
        db.Integer, db.ForeignKey("listing.id", ondelete="CASCADE"),
        nullable=False
    )

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.name
