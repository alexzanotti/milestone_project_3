listing = list(Applicant.query.order_by(Applicant.id).all())
    applicants = listing.applicants