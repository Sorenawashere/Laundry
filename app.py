from flask import Flask, render_template, request, redirect, url_for, flash
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Change this to a random secret key

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/send_mail', methods=['POST'])
def send_mail():
    try:
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        
        # Email configuration (you'll need to set up your SMTP settings)
        # For now, we'll just flash a success message
        flash('Messaggio inviato con successo! Ti contatteremo presto.', 'success')
        
        # Here you would normally send the email using SMTP
        # smtp_server = "smtp.gmail.com"
        # smtp_port = 587
        # sender_email = "your-email@gmail.com"
        # sender_password = "your-app-password"
        # 
        # msg = MIMEMultipart()
        # msg['From'] = sender_email
        # msg['To'] = "info@pulitolindo.it"
        # msg['Subject'] = f"Nuovo messaggio da {name}"
        # 
        # body = f"Nome: {name}\nEmail: {email}\nMessaggio: {message}"
        # msg.attach(MIMEText(body, 'plain'))
        # 
        # server = smtplib.SMTP(smtp_server, smtp_port)
        # server.starttls()
        # server.login(sender_email, sender_password)
        # server.send_message(msg)
        # server.quit()
        
    except Exception as e:
        flash('Errore nell\'invio del messaggio. Riprova più tardi.', 'error')
    
    return redirect(url_for('home') + '#contact')

if __name__ == '__main__':
    app.run(debug=True)
