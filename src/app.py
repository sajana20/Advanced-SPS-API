from flask import Flask, request
from src.repositories.parking_area_repository import ParkingAreaRepository
from src.repositories.user_repo import UserRepository
from src.repositories.user_token_repo import UserTokenRepository
from src.repositories.user_reservation_repo import UserReservationRepository
from src.push_notification import Notification
from src.repositories.footage_repo import FootageRepository

import json

app = Flask(__name__)


@app.route("/login", methods=['post'])
def login():
    print("Hi login1")
    # req_json = request.get_json()
    email = request.form["email"]
    password = request.form['password']
    print(email,password)
    return UserRepository().get_user_details(email, password)

@app.route("/signup", methods=['post'])
def signup():
    print("Hi login1")
    # req_json = request.get_json()
    user_name = request.form["user_name"]
    email = request.form['email']
    password = request.form['password']

    print(email,password)
    return UserRepository().set_user_details(user_name, email, password)

@app.route("/logout", methods=['delete'])
def logout():
    print("Hi login1")
    # req_json = request.get_json()
    user_id = request.form["user_id"]
    print("user_id")
    print(user_id)
    return UserTokenRepository().delete_user_token(user_id)


# @app.route("/register", methods=['post'])
# def login():
#     # req_json = request.get_json()
#     email = request.form["email"]
#     password = request.form['password']
#     print(email,password)
#     return UserRepository().set_user_details(email, password)


@app.route("/availability")
def get_availability():
    print("hi1")
    a = ParkingAreaRepository().get_parking_availability()
    print('a')
    print(a)
    return a


@app.route("/availability", methods=['post'])
def set_availability():
    print("set availability")
    user_id = request.form["user_id"]
    slot_id = request.form["slot_id"]
    availability = request.form['availability']
    active = not availability

    # data = request.get_json() - Use for raspberry
    # slot_id = data['slot_id']
    # availability = data['availability']
    print(slot_id, availability)
    ParkingAreaRepository().update_parking_availability(user_id, slot_id, availability)
    UserReservationRepository().update_user_reservation(user_id, slot_id, active)
    return json.dumps({"status": "Success"})

# @app.route("/unAvailability", methods=['post'])
# def set_unAvailability():
#     print("set availability")
#     slot_id = request.form["slot_id"]
#     video_data = request.form['video_data']
#
#     # data = request.get_json() - Use for raspberry
#     # slot_id = data['slot_id']
#     # availability = data['availability']
#     print(slot_id, video_data)
#     ParkingAreaRepository().update_parking_availability(user_id, slot_id, availability)
#     UserReservationRepository.update_user_reservation(user_id, slot_id, video_data, active)
#     return json.dumps({"status": "Success"})

@app.route("/footage", methods=['post'])
def set_unAvailability():
    print("set availability")
    slot_id = request.form["slot_id"]
    file_name = request.form['file_name']

    # data = request.get_json() - Use for raspberry
    # slot_id = data['slot_id']
    # availability = data['availability']
    print(slot_id, file_name)
    FootageRepository().set_footage(slot_id, file_name)
    return json.dumps({"status": "Success"})

# change this to POST request and pass the message from raspberry
@app.route("/pushNotification", methods=['post'])
def send_pushNotification():
    # data = request.get_json()
    slot_id = request.form["slot_id"]
    title = request.form["title"]
    message = request.form["message"]
    # slot_id = data['slot_id']
    # message = data['message']
    token = UserTokenRepository().get_user_token(slot_id)
    print("token")
    print(token)
    response = Notification().send_push_notification(token, title, message)
    return response

@app.route("/fcmToken", methods=['post'])
def save_token():
    user_id = request.form["user_id"]
    token = request.form["token"]
    response = UserTokenRepository().set_user_token(user_id, token)
    return response

@app.route("/reservations/<user_id>")
def getReservationsByUserId(user_id):
    print("userrrId")
    print(user_id)
    response = UserReservationRepository().get_user_reservation(user_id)
    return response

app.run()
