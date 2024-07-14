from flask import Flask, render_template, request, abort
from flask_mail import Mail, Message
import requests
from config import MAIL_USERNAME, MAIL_PASSWORD, MAIL_PORT, MAIL_SERVER, MAIL_DEFAULT_SENDER, MAIL_TO, RECAPTCHA_SITE_KEY, RECAPTCHA_SECRET_KEY, RECAPTCHA_VERIFY_URL

app = Flask(__name__)

# adding all configs 
app.config.from_pyfile('config.py')

# SMTP server configuration
app.config["MAIL_SERVER"] = MAIL_SERVER
app.config["MAIL_PORT"] = MAIL_PORT
app.config["MAIL_USERNAME"] = MAIL_USERNAME
app.config["MAIL_PASSWORD"] = MAIL_PASSWORD
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USE_SSL"] = False
app.config["MAIL_DEFAULT_SENDER"] = MAIL_DEFAULT_SENDER

# initialize the mailer
mail = Mail()
mail.init_app(app)

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


@app.route("/contact-us", methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # recaptcha...make sure user isn't a bot
        recaptchaResponse = request.form['g-recaptcha-response']
        verifyResponse = requests.post(url=f"{RECAPTCHA_VERIFY_URL}?secret={RECAPTCHA_SECRET_KEY}&response={recaptchaResponse}").json()
        if verifyResponse['success'] == False:
            abort(401)
            
        # user is not a bot...send the message as a email
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        msg = Message("Message from website contact form", recipients=[MAIL_TO], reply_to=email)
        msg.html = render_template("contact-email.html", message=message, email=email, name=name)
        mail.send(msg)
        # after email is sent successfully, show a success alert
        return render_template("contact-us.html", active_page="contact-us", success=1, site_key=RECAPTCHA_SITE_KEY)
    return render_template("contact-us.html", active_page="contact-us", site_key=RECAPTCHA_SITE_KEY)


if __name__ == '__main__':
    app.run(debug=True)