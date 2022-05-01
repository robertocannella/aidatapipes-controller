# Firestore setup guide 
[google python documentation](https://firebase.google.com/docs/firestore/quickstart#python)

## Packages:

* run the following command in the application root directory
```
pip install --upgrade firebase-admin
```

* import the following modules in the python service file:
```
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
```

* generate a new config.json file from google firebase-admin services
[create new key and download json configuration file](https://console.cloud.google.com/iam-admin/serviceaccounts)

* instantiate instance in python service file:
```
cred = credentials.Certificate(<path to newly created firestore config file>)
firebase_admin.initialize_app(cred)
db = firestore.client() # Get Database 
```

## configuration of CRUD
* example from: [google python documentation](https://firebase.google.com/docs/firestore/)quickstart#python)

```
doc_ref = db.collection(u'users').document(u'alovelace')
doc_ref.set({
    u'first': u'Ada',
    u'last': u'Lovelace',
    u'born': 1815
})
```





