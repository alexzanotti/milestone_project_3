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
