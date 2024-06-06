from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", is_home=True)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/services")
def services():
    return render_template("services.html")


@app.route("/projects")
def projects():
    return render_template("projects.html")


@app.route("/apply")
def apply():
    return render_template("apply.html")


@app.route("/contact-us", methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # send the message as a email
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        
    return render_template("contact-us.html")


if __name__ == '__main__':
    app.run(debug=True)