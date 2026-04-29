"""This is an example Python script for local_settings.py."""

import os

from dotenv import load_dotenv

load_dotenv()

BASE_DIR = os.path.abspath(".")

FRONTEND_HOST = "http://127.0.0.1:8000"
PORTAL_NAME = "MediaCMS"
SSL_FRONTEND_HOST = FRONTEND_HOST.replace("http", "https")
SECRET_KEY = os.getenv("SECRET_KEY")
LOCAL_INSTALL = True
DEBUG = True
ACCOUNT_EMAIL_VERIFICATION = "none"  # 'mandatory' 'none'
USE_X_ACCEL_REDIRECT = False

CORS_ALLOW_ALL_ORIGINS = True
# Custom MFA settings
MFA_REQUIRED_ROLES = ["superuser"]  # options: superuser, advanced_user, authenticated, manager, editor

# /health/ready shared-secret gate.
# Leave empty (or unset) for local dev — gate is disabled. In production,
# set a long random value here and store the SAME value in your deploy
# verifier's secrets (e.g. GitHub Actions secret HEALTH_READY_TOKEN). Generate
# with:
#     python -c "import secrets; print(secrets.token_urlsafe(32))"
# Anonymous external probes that don't send `X-Healthcheck-Token: <value>`
# will be rejected with 401 *before* the four readiness checks run.
HEALTH_READY_TOKEN = ""
