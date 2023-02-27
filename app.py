# Home Page
@app.route("/")
def index():
    return render_template("index.html", title="Home", header="Home")
