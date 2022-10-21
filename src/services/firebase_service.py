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


################################################################################
#
#   Utility Functions
#
################################################################################

def get_or_create_document():
    # creating the date object of today's date
    todays_date = datetime.today()

    # printing todays date
    #print("Current date: ", todays_date)

    # fetching the current year, month and day of today
    current_year = todays_date.year
    current_month = todays_date.month
    current_week = int(todays_date.day / 7) + 1
    # print(todays_date.day/7)

    # print("Current year:", current_year)
    # print("Current month:", current_month)
    # print("Current week:", current_week)
    collection_id = "{0}-{1}-{2}".format(current_year,
                                         current_month, current_week)
    return collection_id
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
# This functionality needs to be split up.  Possibly create a function
# get_or_create_document()
#
######################################################################


def append_last_temp_reading(system_id, degrees_fahrenheit, collection, document, zone_index, reading_type):
    """
    appends a reading into an array. 

    """
    # get or create document id
    collection_id = get_or_create_document()

    # generate link to collection
    doc_ref = db.collection(collection).document(collection_id)

    # does the collection exist?
    doc = doc_ref.get()
    if doc.exists:
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
    else:
        # create the document

        # generate timestamp
        javascript_timestamp = datetime.timestamp(datetime.now()) * 1000

        # build object
        obj = {
            'timeStamp': javascript_timestamp,
            'degF': degrees_fahrenheit
        }
        # append temperature
        locator = document + str(zone_index) + '.lineRT'
        #doc_ref.update({locator: firestore.ArrayUnion([obj])})
        doc_ref.set({locator: firestore.ArrayUnion([obj])})
        # print the dictionary out
        #print(f'Document data: {doc.to_dict()}')
        #print(u'Had to generate new document')
