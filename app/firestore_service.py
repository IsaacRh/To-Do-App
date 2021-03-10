import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

project_id = 'to-do-list-307121'
credentials = credentials.ApplicationDefault()
firebase_admin.initialize_app(credentials, {
  'projectId': project_id,
})
db = firestore.client()

def get_users():
    return db.collection('users').get()