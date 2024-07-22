from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", is_home=True, active_page="home")


@app.route("/about")
def about():
    return render_template("about.html", active_page="about")


@app.route("/services")
def services():
    return render_template("services.html", active_page="services")


@app.route("/projects")
def projects():
    return render_template("projects.html", active_page="projects")


@app.route("/apply")
def apply():
    return render_template("apply.html", active_page="apply")


@app.route("/contact-us")
def contact():
    return render_template("contact-us.html", active_page="contact-us")


if __name__ == '__main__':
    app.run(debug=True)