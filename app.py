from flask import Flask, render_template, request, redirect
from flask_mail import Mail, Message

app = Flask(__name__)

# Configure Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.your-email-provider.com'  # Replace with your email provider
app.config['MAIL_PORT'] = 587  # Use 465 for SSL or 587 for TLS
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'your-email@example.com'  # Replace with your email
app.config['MAIL_PASSWORD'] = 'your-email-password'  # Replace with your email password
app.config['MAIL_DEFAULT_SENDER'] = 'tshediso@sekasquare.co.za'

mail = Mail(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/qa')
def qa():
    return render_template('qa.html')

@app.route('/send_email', methods=['POST'])
def send_email():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    
    msg = Message("New Contact Form Submission",
                  sender=email,
                  recipients=['your-email@example.com'])  # Replace with your recipient email
    msg.body = f"Name: {name}\nEmail: {email}\nMessage:\n{message}"

    mail.send(msg)
    
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
