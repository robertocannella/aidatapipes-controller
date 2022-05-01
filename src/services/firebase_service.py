################################################################################
#
#   GOOGLE FIRESTORE NOSQL DATA BASE SERVICE
#   
################################################################################

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use the application default credentials
cred = credentials.Certificate("fb-key-ai-datapipes.json")
firebase_admin.initialize_app(cred)
db = firestore.client() # Get Database 