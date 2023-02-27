import os
import json
from flask import Flask, render_template, request
if os.path.exists("env.py"):
    import env


app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")

# Home Page
@app.route("/")
def index():
    return render_template("index.html", title="Home", header="Home")

# Applicants Applied Page
@app.route("/applicants_applied")
def applicants_applied():
    return render_template("applicants_applied.html", title="Applicants Applied", header="Applicants Applied")

# Applicants Apply Page
@app.route("/applicants_apply")
def applicants_apply():
    return render_template("applicants_apply.html", title="Apply", header="Apply")

# Applicants Page
@app.route("/applicants")
def applicants():
    return render_template("applicants.html", title="Applicants", header="Applicants")

# Contact Sent Page
@app.route("/contact_sent")
def contact_sent():
    return render_template("contact_sent.html", title="Contact Sent", header="Contact Sent")

# Contact Page
@app.route("/contact")
def contact():
    return render_template("contact.html", title="Contact", header="Contact")

# Recruiter Applicants Page
@app.route("/recruiter_applicants")
def recruiter_applicants():
    return render_template("recruiter_applicants.html", title="Recruiter Applicants", header="Recruiter Applicants")

# Recruiter Edit Page
@app.route("/recruiter_edit")
def recruiter_edit():
    return render_template("recruiter_edit.html", title="Recruiter Edit", header="Recruiter Edit")

# Recruiter List Page
@app.route("/recruiter_list")
def recruiter_list():
    return render_template("recruiter_list.html", title="Recruiter List", header="Recruiter List")

# Recruiter Listed Page
@app.route("/recruiter_listed")
def recruiter_listed():
    return render_template("recruiter_listed.html", title="Recruiter Listed", header="Recruiter Listed")

# Recruiter Page
@app.route("/recruiter")
def recruiter():
    return render_template("recruiter.html", title="Recruiter", header="Recruiter")