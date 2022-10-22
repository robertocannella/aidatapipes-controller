################################################################################
#
#   GOOGLE FIRESTORE NOSQL DATA BASE SERVICE
#
################################################################################

#**************************   IMPORTS   ***************************************#
from pydoc import doc
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from decouple import config
from datetime import datetime


################################################################################
#
#   GOOGLE FIRESTORE INSTANCE
#
################################################################################

# Import credentials from json
cred = credentials.Certificate("fs-aidatapipes-key-04-30-2022.json")

# Initialize app
firebase_admin.initialize_app(cred)

# create db object
db = firestore.client()


#**************************   Utility Functions   *****************************#

################################################################################
#
#   Get or Create a Firestore documnet
#
################################################################################

def get_or_create_document(collection):
    """
    checks for the exsitence of a firestore document. if one doesn't exist,
    generates a new one and returns it.
    """
    # creating the date object of today's date
    todays_date = datetime.today()

    # fetching the current year, month and day of today
    current_year = todays_date.year
    current_month = todays_date.month
    current_week = int(todays_date.day / 7) + 1

    # concat data for reference
    collection_id = "{0}-{1}-{2}".format(current_year, current_month, current_week)

    # generate link to collection
    doc_ref = db.collection(collection).document(collection_id)

    # get the document
    doc = doc_ref.get()

    # does the collection exist?
    if not doc.exists:
        doc_ref.set({})

    return doc_ref

#**************************   CRUD   ***************************************#


######################################################################
#
# Replace a temperature reading
#
######################################################################
def overwrite_last_temp_reading(sensor_id, degrees_fahrenheit, type):
    """
    adds a reading into the database. 
    """
    # generate link to collection
    doc_ref = db.collection(type).document(sensor_id)

    # generate timestamp
    javascript_timestamp = datetime.timestamp(datetime.now()) * 1000

    # write to database
    doc_ref.set({
        'timeStamp': javascript_timestamp,
        'sensorId': sensor_id,
        'degreesFahrenheit': degrees_fahrenheit
    })


######################################################################
#
# Append temperature reading
#
######################################################################


def append_last_temp_reading(system_id, degrees_fahrenheit, collection, document, zone_index, reading_type):
    """
    appends a reading into an array. 

    """
    # get or create document id
    doc_ref = get_or_create_document(collection)

    # generate timestamp
    javascript_timestamp = datetime.timestamp(datetime.now()) * 1000

    # build object
    obj = {
        'timeStamp': javascript_timestamp,
        'degF': degrees_fahrenheit
    }

    # append temperature
    locator = document + str(zone_index) + '.lineRT'
    doc_ref.update({locator: firestore.ArrayUnion([obj])})

    # print the dictionary out
    #print(f'Document data: {doc.to_dict()}')

