import firebase_admin
from firebase_admin import credentials

# Before running this script, make sure to:
# 1. Install the Firestore library by running the following command in your terminal:
#    pip install google-cloud-firestore

# firebase admin sdk configuration
cred = credentials.Certificate('firebase_service_account_info.json')
firebase_admin.initialize_app(cred)
