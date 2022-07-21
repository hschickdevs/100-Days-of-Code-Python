from flask import Flask, render_template, request

from scripts.backend import load_posts, send_contact_email

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", posts=load_posts())


@app.route('/index')
def index():
    return render_template("index.html", posts=load_posts())


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        subject = f"Contact Form Submission from {request.form['name']}"
        message = f"Name: {request.form['name']}\n" \
                  f"Email: {request.form['email']}\n" \
                  f"Phone #: {request.form['phone']}\n" \
                  f"\nMessage:\n{request.form['message']}"
        send_contact_email(subject, message)
        return render_template('contact.html', form_submitted=True)
    else:    
        return render_template('contact.html', form_submitted=False)


@app.route('/post')
def post():
    return render_template('post.html')


@app.route('/post/<int:p_id>')
def get_post(p_id):
    return render_template('post.html', post=load_posts()[int(p_id) - 1])


if __name__ == "__main__":
    app.run(debug=True)