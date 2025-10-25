from flask import Flask, render_template, request, redirect, url_for, flash
import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from send_email import send_email

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'your-secret-key-here')  # Use environment variable for production

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/send_mail', methods=['POST'])
def send_mail():
    try:
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        
        # Use the send_email function from send_email.py
        success = send_email(name, email, message)
        
        if success:
            flash('Messaggio inviato con successo! Ti contatteremo presto.', 'success')
        else:
            flash('Errore nell\'invio del messaggio. Riprova più tardi.', 'error')
        
    except Exception as e:
        flash('Errore nell\'invio del messaggio. Riprova più tardi.', 'error')
    
    return redirect(url_for('home') + '#contact')

if __name__ == '__main__':
    # For production, use environment variables
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_ENV') == 'development' 
    app.run(host='0.0.0.0', port=port, debug=debug)
