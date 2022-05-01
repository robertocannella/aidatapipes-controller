################################################################################
#
#   GOOGLE FIRESTORE NOSQL DATA BASE SERVICE
#   
################################################################################

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from decouple import config


DB_KEY = config("FS_KEY")
# Use the application default credentials
cred = credentials.Certificate(DB_KEY)
firebase_admin.initialize_app(cred)
db = firestore.client() # Get Database 