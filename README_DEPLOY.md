Deployment notes:
- Install dependencies from requirements.txt.
- Set DJANGO_SECRET_KEY and DJANGO_ALLOWED_HOSTS in your hosting environment.
- For Render/Heroku-style deployment, use the included Procfile and Dockerfile.
- The app now uses WhiteNoise for static files and a startup command that runs migrations.
