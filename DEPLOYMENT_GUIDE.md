# Deployment Guide: Switching from WordPress to Flask on Aruba

## Pre-Deployment Checklist

### 1. Backup Your Current WordPress Site
Before making any changes, create a complete backup of your WordPress site:

**Via Aruba Control Panel:**
1. Log into your Aruba hosting control panel
2. Go to "File Manager" or "Backup" section
3. Create a full backup of your current website files
4. Export your WordPress database (if applicable)

**Alternative: Manual Backup**
- Download all files from your public_html directory
- Export your WordPress database via phpMyAdmin

### 2. Prepare Your Flask Application

Your Flask app is now ready with:
- ✅ `requirements.txt` - Python dependencies
- ✅ `app.py` - Updated for production
- ✅ `send_email.py` - Email functionality
- ✅ `env.example` - Environment variables template

## Deployment Steps

### Step 1: Upload Your Flask Application

1. **Compress your Flask app:**
   ```bash
   cd /Users/elanastroud/laundry/Laundry
   zip -r laundry-app.zip . -x "venv/*" "__pycache__/*" "*.pyc"
   ```

2. **Upload to Aruba:**
   - Log into Aruba control panel
   - Go to File Manager
   - Navigate to your domain's public_html directory
   - Upload the `laundry-app.zip` file
   - Extract it in the public_html directory

### Step 2: Set Up Python Environment

**Option A: If Aruba supports Python hosting:**
1. In Aruba control panel, look for "Python" or "Python Apps" section
2. Create a new Python application
3. Point it to your Flask app directory
4. Set the application file to `app.py`

**Option B: If using shared hosting without Python support:**
You may need to upgrade to a VPS or dedicated server that supports Python.

### Step 3: Configure Environment Variables

1. Create a `.env` file in your Flask app directory:
   ```bash
   cp env.example .env
   ```

2. Edit `.env` with your actual values:
   ```
   SECRET_KEY=your-actual-secret-key-here
   FLASK_ENV=production
   SMTP_SERVER=smtp.gmail.com
   SMTP_PORT=465
   EMAIL_USERNAME=your-actual-email@gmail.com
   EMAIL_PASSWORD=your-actual-app-password
   CONTACT_RECEIVER=info@pulitolindo.it
   PORT=5000
   ```

### Step 4: Install Dependencies

If you have SSH access:
```bash
cd /path/to/your/flask/app
pip install -r requirements.txt
```

If no SSH access, Aruba should handle this automatically if Python hosting is configured.

### Step 5: Configure Web Server

**For Apache (most common on shared hosting):**
Create a `.htaccess` file in your public_html directory:
```apache
RewriteEngine On
RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME} !-d
RewriteRule ^(.*)$ /app.py/$1 [QSA,L]
```

**For Nginx:**
```nginx
location / {
    try_files $uri $uri/ @flask;
}

location @flask {
    proxy_pass http://127.0.0.1:5000;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
}
```

### Step 6: Test Your Application

1. Visit your domain to ensure the Flask app loads
2. Test the contact form functionality
3. Check that all static files (CSS, images) load correctly

## Email Configuration

### Gmail Setup (Recommended)
1. Enable 2-factor authentication on your Gmail account
2. Generate an "App Password" for your application
3. Use this app password in your `.env` file

### Alternative Email Providers
- **Outlook/Hotmail:** Use smtp-mail.outlook.com, port 587
- **Yahoo:** Use smtp.mail.yahoo.com, port 587
- **Custom SMTP:** Contact your hosting provider for SMTP settings

## Troubleshooting

### Common Issues:

1. **Static files not loading:**
   - Check file permissions (644 for files, 755 for directories)
   - Verify paths in your HTML templates

2. **Contact form not working:**
   - Check environment variables are set correctly
   - Verify SMTP credentials
   - Check server logs for errors

3. **Python not supported:**
   - Contact Aruba support about Python hosting options
   - Consider upgrading to VPS hosting
   - Alternative: Deploy to Heroku, DigitalOcean, or similar

### Getting Help:
- Check Aruba's documentation for Python hosting
- Contact Aruba support if Python hosting isn't available
- Consider cloud platforms like Heroku, Railway, or DigitalOcean for easier Flask deployment

## Post-Deployment

1. **Update DNS if needed** (usually not required if staying with Aruba)
2. **Test all functionality** thoroughly
3. **Set up monitoring** for uptime and errors
4. **Keep backups** of your Flask application files

## Alternative Deployment Options

If Aruba doesn't support Python hosting, consider these alternatives:

### Heroku (Free tier available)
```bash
# Install Heroku CLI
# Create Procfile
echo "web: python app.py" > Procfile
# Deploy
git init
git add .
git commit -m "Initial commit"
heroku create your-app-name
git push heroku main
```

### Railway
- Connect your GitHub repository
- Railway auto-detects Flask apps
- Automatic deployments

### DigitalOcean App Platform
- Similar to Heroku but with more control
- Good pricing for small applications

---

**Important:** Always test your deployment thoroughly before switching your domain's DNS settings!
