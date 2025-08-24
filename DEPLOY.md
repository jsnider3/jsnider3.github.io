# GitHub Pages Deployment Instructions

Your blog has been modernized and is ready for GitHub Pages! Follow these steps to deploy:

## 1. Commit and Push Changes

```bash
git add .
git commit -m "Migrate from Google App Engine to GitHub Pages"
git push origin master
```

## 2. Enable GitHub Pages

1. Go to your repository on GitHub: https://github.com/jsnider3/www.joshuasnider.com (or whatever your repo is named)
2. Click on **Settings** (in the repo navigation)
3. Scroll down to **Pages** section (in the left sidebar)
4. Under **Source**, select:
   - **Deploy from a branch**
   - Branch: **master** (or main)
   - Folder: **/ (root)**
5. Click **Save**

## 3. Configure Custom Domain

Since you already have `www.joshuasnider.com`:

1. In the **Pages** settings, under **Custom domain**, enter: `www.joshuasnider.com`
2. Click **Save**
3. Check **Enforce HTTPS** (may take a few minutes to be available)

## 4. Update DNS Records

Update your domain's DNS settings with your domain registrar:

- **CNAME Record**: `www` → `jsnider3.github.io`
- **A Records** for apex domain (joshuasnider.com):
  - 185.199.108.153
  - 185.199.109.153
  - 185.199.110.153
  - 185.199.111.153

## 5. Wait for Deployment

- Initial deployment may take 10-20 minutes
- DNS propagation can take up to 24 hours
- GitHub will automatically handle SSL certificates

## What's Changed

### From GAE to GitHub Pages:
- ✅ Modern Jekyll with GitHub Pages gems
- ✅ Automatic SSL certificates (no more Let's Encrypt manual updates)
- ✅ JavaScript-based tagline rotation (replaced Flask API)
- ✅ Free hosting with no maintenance
- ✅ Automatic builds on push

### Files You Can Delete (after confirming everything works):
- `app.yaml` - GAE configuration
- `main.py` - Flask backend
- `requirements.txt` - Python dependencies
- `appengine_config.py` - GAE config
- `client-secret.json.enc` - Old secrets
- `lib/` directory - Python libraries
- `templates/` directory - Flask templates
- `src/` directory - Old Jekyll location
- `.travis.yml` - Old CI configuration

### To Run Locally (Optional):

```bash
bundle install
bundle exec jekyll serve
# Visit http://localhost:4000
```

## Troubleshooting

- **404 errors**: Wait for deployment to complete (check Actions tab)
- **Domain not working**: Verify DNS records and CNAME file
- **SSL errors**: Wait for GitHub to provision certificates (up to 24 hours)
- **Build errors**: Check the Actions tab in your GitHub repo for error logs

## Next Steps

Consider:
- Adding new blog posts in `_posts/` folder
- Updating the About page
- Customizing the theme
- Adding GitHub Actions for additional automation