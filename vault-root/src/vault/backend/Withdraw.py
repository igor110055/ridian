# third party import:
from flask import Blueprint
from flask import Flask, request, jsonify, json
from requests import Request, Session
from flask import request
import datetime


# third party import:
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase import firebase
if not firebase_admin._apps:
    cred = credentials.Certificate('key.json')
    default_app = firebase_admin.initialize_app(cred)

db = firestore.client()
firebase = firebase.FirebaseApplication('https://crypto-d33e5-default-rtdb.asia-southeast1.firebasedatabase.app/', None)


# this project  imports:
from HelperFunction.transaction import transaction
from HelperFunction.randomword import randomword
from HelperFunction.userdetail import getUserDetail

withdraw_api = Blueprint('withdraw_api', __name__)
session = Session()


@withdraw_api.route("/widthdraw", methods=["POST", "GET"])
def widthdraw():
    
    response_object = {'status': 'success'}
    if request.method == "POST":
        post_data = request.get_json()

        amount = post_data.get('amount')
        print(amount)
        coin = post_data.get('coin')
        address = post_data.get('address')
        api_key='szi72POBX0TH086Gebtut76pKUC7vVAPnM2QUf0X'
        secrets_key='IUw47_jaWULymqs-gZd2udPUYYQq1_n76V8bwJsm'
    
        collection= getUserDetail('adeel@ridian.io')
        print(collection)
        userTransactionCount=widthdraw_transaction('adeel@ridian.io')
        print(userTransactionCount)

        now = datetime.datetime.now()
        todayDate=now.strftime("%Y-%m-%d %H:%M:%S")
        if(collection['withdrawable_balance'] >= float(amount)):
            data=transaction(amount,coin,address,api_key,secrets_key)
            session = Session()
            resp = session.send(data)
            res = resp.json()
            if (res['success'] == True):
               db.collection('withdrawal_history').document(randomword(10)).set(
                {
                            "email": "adeel@ridian.io",
                            "transaction_id": res["result"]["id"],
                            "coin": res["result"]["coin"],
                            "amount": res["result"]["size"],
                            "time": res["result"]["time"],
                            "status": res["result"]["status"],
                })  
               collection = db.collection("registered_users").where("email", "==", "adeel@ridian.io")
               for doc in collection.stream():
                 Data = doc.to_dict()
                 update_register_user = db.collection('registered_users').document(doc.id)
                 update_register_user.update({"withdrawable_balance": float(Data['withdrawable_balance'])-float(amount)})
                 update_register_user.update({"last_withdraw_date": todayDate})
            else:
             response_object['message'] =res['error']
             print(res['error'])
             return jsonify(response_object)

     
            print("pass")
            response_object['message'] = 'success'
        else:
         print("failed")
         response_object['message'] = 'failed'

        return jsonify(response_object)

def widthdraw_transaction(email):
    docs = db.collection('withdrawal_history').where('email','==',email).stream()
    a = 0
    for doc in docs:
        stock = doc.to_dict()
        a += stock['amount']
    return a
    