import db

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
    applicants = db.relationship("Applicant", backref="listing", cascade="all, delete", lazy=True)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.job_title
      