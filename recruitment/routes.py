import os
import json
from flask import Flask, render_template, request, redirect, url_for
from recruitment import app, db
from recruitment.data_models import Listing, Applicant


# Home Page
@app.route("/")
def index():
    images = []
    with open("recruitment/static/data/images.json", "r") as json_images:
        images = json.load(json_images)
    return render_template(
        "index.html",
        title="Home",
        header="Recruitment World",
        images=images)


# Applicants Page
@app.route("/applicants")
def applicants():
    applicants = list(Listing.query.order_by(Listing.id).all())
    return render_template(
        "applicants.html",
        title="Applicants",
        header="Applicants",
        applicants=applicants,
    )


# Applicants Apply Page
@app.route("/applicants_apply/<listing_id>", methods=["GET", "POST"])
def applicants_apply(listing_id):
    listing = Listing.query.get_or_404(listing_id)
    if request.method == "POST":
        applicant = Applicant(
            name=request.form.get("name"),
            phone=request.form.get("phone"),
            email=request.form.get("email"),
            experience_level=request.form.get("experience_level"),
            personal_statement=request.form.get("personal_statement"),
            education=request.form.get("education"),
            work_experience=request.form.get("work_experience"),
            listing=listing,
        )
        db.session.add(applicant)
        db.session.commit()
        return redirect(url_for("applicants_applied"))
    else:
        return render_template(
            "applicants_apply.html",
            title="Apply",
            header="Apply",
            listing=listing
        )


# Applicants Applied Page
@app.route("/applicants_applied")
def applicants_applied():
    return render_template(
        "applicants_applied.html",
        title="Applicants Applied",
        header="Applicants Applied",
    )


# Recruiter Page
@app.route("/recruiter")
def recruiter():
    recruiter = list(Listing.query.order_by(Listing.id).all())
    return render_template(
        "recruiter.html",
        title="Recruiter",
        header="Recruiter",
        recruiter=recruiter
    )


# Recruiter List Page
@app.route("/recruiter_list", methods=["GET", "POST"])
def recruiter_list():
    if request.method == "POST":
        recruiter = Listing(
            job_title=request.form.get("job_title"),
            salary=request.form.get("salary"),
            location=request.form.get("location"),
            company=request.form.get("company"),
            experience_required=request.form.get("experience_required"),
            job_description=request.form.get("job_description"),
            requirements=request.form.get("requirements"),
            benefits=request.form.get("benefits"),
        )
        db.session.add(recruiter)
        db.session.commit()
        return redirect("recruiter_listed")
    else:
        return render_template(
            "recruiter_list.html",
            title="Recruiter List",
            header="Recruiter List"
        )


# Recruiter Listed Page
@app.route("/recruiter_listed")
def recruiter_listed():
    return render_template(
        "recruiter_listed.html",
        title="Recruiter Listed",
        header="Recruiter Listed"
    )


# Recruiter Applicants Page
@app.route("/recruiter_applicants/<int:listing_id>")
def recruiter_applicants(listing_id):
    listing = list(
        Listing.query
        .order_by(Listing.id)
        .filter_by(id=listing_id)
        .all())
    applicants = listing[0].applicants
    return render_template(
        "recruiter_applicants.html",
        title="Recruiter Applicants",
        header="Recruiter Applicants",
        applicants=applicants,
    )


# Recruiter Applicant Delete
@app.route("/recruiter_applicant_delete/<int:applicant_id>")
def recruiter_applicant_delete(applicant_id):
    applicant = Applicant.query.get_or_404(applicant_id)
    db.session.delete(applicant)
    db.session.commit()
    return redirect(
        url_for("recruiter_applicants", listing_id=applicant.listing_id))


# Recruiter Applicant Edit Page
@app.route("/recruiter_applicant_edit/<int:applicant_id>", methods=["GET",
                                                                    "POST"])
def recruiter_applicant_edit(applicant_id):
    applicant = Applicant.query.get_or_404(applicant_id)
    listing = Listing.query.get_or_404(applicant.listing_id)
    if request.method == "POST":
        applicant.name = (request.form.get("name"),)
        applicant.phone = (request.form.get("phone"),)
        applicant.email = (request.form.get("email"),)
        applicant.experience_level = (request.form.get("experience_level"),)
        applicant.personal_statement = (
            request.form.get("personal_statement"),)
        applicant.education = (request.form.get("education"),)
        applicant.work_experience = request.form.get("work_experience")
        db.session.commit()
        return redirect(
            url_for("recruiter_applicants", listing_id=applicant.listing_id)
        )
    return render_template(
        "recruiter_applicant_edit.html",
        title="Recruiter Applicant Edit",
        header="Recruiter Applicant Edit",
        applicant=applicant,
        listing=listing
    )


# Recruiter Edit Page
@app.route("/recruiter_edit/<int:listing_id>", methods=["GET",
                                                        "POST"])
def recruiter_edit(listing_id):
    listing = Listing.query.get_or_404(listing_id)
    if request.method == "POST":
        listing.job_title = (request.form.get("job_title"),)
        listing.salary = (request.form.get("salary"),)
        listing.location = (request.form.get("location"),)
        listing.company = (request.form.get("company"),)
        listing.experience_required = (
            request.form.get("experience_required"),)
        listing.job_description = (request.form.get("job_description"),)
        listing.requirements = (request.form.get("requirements"),)
        listing.benefits = request.form.get("benefits")
        db.session.commit()
        return redirect(url_for("recruiter"))
    return render_template(
        "recruiter_edit.html",
        title="Recruiter Edit",
        header="Recruiter Edit",
        listing=listing,
    )


# Recruiter Delete Page
@app.route("/recruiter_delete/<int:listing_id>")
def recruiter_delete(listing_id):
    listing = Listing.query.get_or_404(listing_id)
    db.session.delete(listing)
    db.session.commit()
    return redirect(url_for("recruiter"))


# Contact Page
@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        return redirect("contact_sent")
    else:
        return render_template(
            "contact.html",
            title="Contact",
            header="Contact")


# Contact Sent Page
@app.route("/contact_sent")
def contact_sent():
    return render_template(
        "contact_sent.html", title="Contact Sent", header="Contact Sent")
