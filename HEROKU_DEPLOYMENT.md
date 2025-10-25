# Heroku Deployment Guide for Laundry Website

## Prerequisites
- GitHub account
- Heroku account (free at heroku.com)
- Heroku CLI installed on your computer

## Step 1: Install Heroku CLI

**On macOS:**
```bash
brew tap heroku/brew && brew install heroku
```

**On Windows:**
Download from: https://devcenter.heroku.com/articles/heroku-cli

**On Linux:**
```bash
curl https://cli-assets.heroku.com/install.sh | sh
```

## Step 2: Prepare Your Code for GitHub

1. **Initialize Git repository:**
   ```bash
   cd /Users/elanastroud/laundry/Laundry
   git init
   git add .
   git commit -m "Initial commit - Laundry website"
   ```

2. **Create GitHub repository:**
   - Go to github.com
   - Click "New repository"
   - Name it "laundry-website" (or any name you prefer)
   - Don't initialize with README (since you already have files)
   - Click "Create repository"

3. **Connect and push to GitHub:**
   ```bash
   git remote add origin https://github.com/YOUR_USERNAME/laundry-website.git
   git branch -M main
   git push -u origin main
   ```

## Step 3: Set Up Heroku

1. **Login to Heroku:**
   ```bash
   heroku login
   ```

2. **Create Heroku app:**
   ```bash
   heroku create your-laundry-app-name
   ```
   (Replace "your-laundry-app-name" with a unique name)

3. **Set environment variables:**
   ```bash
   heroku config:set SECRET_KEY="your-super-secret-key-here"
   heroku config:set FLASK_ENV="production"
   heroku config:set SMTP_SERVER="smtp.gmail.com"
   heroku config:set SMTP_PORT="465"
   heroku config:set EMAIL_USERNAME="your-email@gmail.com"
   heroku config:set EMAIL_PASSWORD="your-gmail-app-password"
   heroku config:set CONTACT_RECEIVER="info@pulitolindo.it"
   ```

## Step 4: Deploy to Heroku

1. **Deploy your app:**
   ```bash
   git push heroku main
   ```

2. **Open your app:**
   ```bash
   heroku open
   ```

## Step 5: Test Your Application

1. **Visit your Heroku URL** (something like: https://your-laundry-app-name.herokuapp.com)
2. **Test the contact form** - make sure emails are being sent
3. **Check all pages load correctly**
4. **Verify all images and CSS are working**

## Email Setup for Gmail

To get your Gmail app password:

1. **Enable 2-Factor Authentication** on your Gmail account
2. **Go to Google Account settings** → Security → App passwords
3. **Generate a new app password** for "Mail"
4. **Use this password** in the EMAIL_PASSWORD environment variable

## Troubleshooting

### Common Issues:

1. **Build fails:**
   ```bash
   heroku logs --tail
   ```
   Check the logs for specific errors

2. **Static files not loading:**
   - Check that all files are committed to git
   - Verify file paths in templates

3. **Email not working:**
   - Double-check Gmail app password
   - Verify all environment variables are set
   - Check Heroku logs for email errors

4. **App crashes:**
   ```bash
   heroku logs --tail
   ```
   Look for Python errors in the logs

### Useful Heroku Commands:

```bash
# View logs
heroku logs --tail

# Check app status
heroku ps

# Restart app
heroku restart

# View config variables
heroku config

# Open app in browser
heroku open

# Scale app (if needed)
heroku ps:scale web=1
```

## Next Steps After Testing

Once your Heroku app is working perfectly:

1. **Test thoroughly** - make sure everything works
2. **Take note of any issues** and fix them
3. **Document any customizations** you made
4. **Then proceed with Aruba deployment** using the main deployment guide

## Heroku Free Tier Limitations

- App sleeps after 30 minutes of inactivity
- 550-1000 dyno hours per month (usually enough for small sites)
- No custom domains on free tier (but you can test functionality)

## Upgrading Later

If you want to keep using Heroku for production:
- **Hobby plan ($7/month)** - keeps app always running, custom domains
- **Professional plans** - for higher traffic sites

---

**Your Heroku URL will be:** `https://your-app-name.herokuapp.com`

Test everything thoroughly before switching your domain to Aruba!
