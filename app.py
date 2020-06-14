from flask import Flask, render_template, request
import smtplib
import os

app = Flask(__name__)

subscribers = []


@app.route('/')
def index():
    title = "Kim Granaderos' Blog"
    return render_template("index.html", title=title)


@app.route('/about')
def about():
    title = "About Kim Granaderos"
    names = ["John", "Mary", "Wes", "Sally"]
    return render_template("about.html", names=names, title=title)


@app.route('/subscribe')
def subscribe():
    title = "Subscribe to my Email Newsletter"
    return render_template("subscribe.html", title=title)


@app.route('/form', methods=["POST"])
def form():
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    email = request.form.get('email')

    message = "You have been subscribed to my email newsletter"
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(os.environ.get('EMAIL_USER'), os.environ.get('EMAIL_PASS'))
    server.sendmail("xxnamelessxx090897@gmail.com", email, message)

    if not first_name or not last_name or not email:
        error_statement = "All Form Fields Required..."
        return render_template("subscribe.html",
                               error_statement=error_statement,
                               first_name=first_name,
                               last_name=last_name,
                               email=email)

    subscribers.append(f"{first_name} {last_name} | {email}")
    title = "Thank You!"
    return render_template("form.html", title=title, subscribers=subscribers)
