import os
import json
from flask import Flask, render_template, request, redirect
if os.path.exists("env.py"):
    import env


app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")

# Home Page
@app.route("/")
def index():
    images = []
    with open("static/data/images.json", "r") as json_images:
        images = json.load(json_images)
    return render_template("index.html", title="Home", header="Home",  images=images)


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

# Contact Page
@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        return redirect("contact_sent")
    else:
        return render_template("contact.html", title="Contact", header="Contact")

# Contact Sent Page
@app.route("/contact_sent")
def contact_sent():
    return render_template("contact_sent.html", title="Contact Sent", header="Contact Sent")

# Recruiter Applicants Page
@app.route("/recruiter_applicants")
def recruiter_applicants():
    return render_template("recruiter_applicants.html", title="Recruiter Applicants", header="Recruiter Applicants")

# Recruiter Edit Page
@app.route("/recruiter_edit")
def recruiter_edit():
    return render_template("recruiter_edit.html", title="Recruiter Edit", header="Recruiter Edit")

# Recruiter List Page
@app.route("/recruiter_list", methods=["GET", "POST"])
def recruiter_list():
    if request.method == "POST":
        return redirect("recruiter_listed")
    else:
        return render_template("recruiter_list.html", title="Recruiter List", header="Recruiter List")

# Recruiter Listed Page
@app.route("/recruiter_listed")
def recruiter_listed():
    return render_template("recruiter_listed.html", title="Recruiter Listed", header="Recruiter Listed")

# Recruiter Page
@app.route("/recruiter")
def recruiter():
    return render_template("recruiter.html", title="Recruiter", header="Recruiter")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)