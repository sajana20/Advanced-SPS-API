import firebase_admin
from firebase_admin import credentials, messaging

firebase_credentials = credentials.Certificate('firebase.json')
firebase_app = firebase_admin.initialize_app(firebase_credentials)

class Notification():
    def send_push_notification(self, token, title, msg):
        title = title
        body = msg
        token = token
        try:
            message = messaging.MulticastMessage(
                notification=messaging.Notification(
                    title=title,
                    body=body
                ),
                tokens=token
            )
            messaging.send_multicast(message)
            return "Message Sent"

        except Exception as err:
            return err

