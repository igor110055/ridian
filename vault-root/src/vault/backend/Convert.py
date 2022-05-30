# third party import:
from flask import request
from requests import Request, Session
from flask import Flask, request, jsonify, json
from flask import Blueprint
import datetime


# this project  imports:
from HelperFunction.userdetail import getUserDetail
from HelperFunction.randomword import randomword
from HelperFunction.userdetail import getConvertPannding



# third party import:
from firebase_admin import firestore
from firebase_admin import credentials
import firebase_admin
from firebase import firebase
if not firebase_admin._apps:
    cred = credentials.Certificate('key.json')
    default_app = firebase_admin.initialize_app(cred)

db = firestore.client()
firebase = firebase.FirebaseApplication('https://crypto-d33e5-default-rtdb.asia-southeast1.firebasedatabase.app/', None)


convert_api = Blueprint('convert_api', __name__)
session = Session

@convert_api.route("/convert", methods=["POST", "GET"])
def convert():

    response_object = {'status': 'success'}
    if request.method == "POST":
        post_data = request.get_json()
        ridian_shares = post_data.get('amount')
        coin = post_data.get('coin')
        type= post_data.get('type')
    
    
        now = datetime.datetime.now()
        todayDate=now.strftime("%Y-%m-%d %H:%M:%S")
        #getConvertDetail() --> get current user convert ridian Count 
        convertDetail = getConvertDetail('adeel@ridian.io')

        #getUserDetail() --> get current user  detail 
        usertotalRidian = getUserDetail('adeel@ridian.io')

        if(usertotalRidian['ridian_shares'] >= float(ridian_shares)):
               
            if( type == 'delay' ):

               # getConvertPannding()

                getrecord=db.collection("convert").where("email", '==', 'adeel@ridian.io').where("status", '==', 'pennding').get();
                if(getrecord):
                 response_object['message'] = 'All ready Status pennding'
                 print("delay")
                 return jsonify(response_object)
                else:
                 print("null")
                 usdc_amount = float(ridian_shares)/2
                 db.collection('convert').document(randomword(10)).set(
                    {
                        "email": "adeel@ridian.io",
                        "coin": coin,
                        "usdc_amount": usdc_amount,
                        "usdc_ridian_shares": float(ridian_shares),
                        "status": "pennding",
                        "created_at":todayDate
                    })
                 collection = db.collection("registered_users").where("email", "==", "adeel@ridian.io")
                 for doc in collection.stream():
                     Data = doc.to_dict()
                     update_register_user = db.collection('registered_users').document(doc.id)
                     update_register_user.update({"ridian_shares": float(Data['ridian_shares'])-float(ridian_shares)})
                     update_register_user.update({"usdc_amount": float(Data['usdc_amount'])-float(usdc_amount)})

                response_object['message'] = 'Waiting 24 Hour'
                print("delay")
                return jsonify(response_object)

                
            else:
             print("instant")
             usdc_amount = float(ridian_shares)/2
             percentage=(0.3 * usdc_amount) / 100.0
             print(percentage)
             actualAmount = float(usdc_amount)-percentage
             

          #  database -->  data save in convert table against current user
            db.collection('convert').document(randomword(10)).set(
                {
                    "email": "adeel@ridian.io",
                    "coin": coin,
                    "usdc_amount": usdc_amount,
                    "usdc_ridian_shares": float(ridian_shares),
                    "status": "success",
                     "created_at":todayDate
                }
            )
             # database -->  data update in registered_users table against current user
            collection = db.collection("registered_users").where("email", "==", "adeel@ridian.io")
            for doc in collection.stream():
                Data = doc.to_dict()
                update_register_user = db.collection('registered_users').document(doc.id)
                update_register_user.update({"withdrawable_balance": float(Data['withdrawable_balance'])+float(actualAmount)})
                update_register_user.update({"ridian_shares": float(Data['ridian_shares'])-float(ridian_shares)})
                update_register_user.update({"usdc_amount": float(Data['usdc_amount'])-float(usdc_amount)})
                update_register_user.update({"last_convert_date": todayDate})
             # database -->  data update in ridian_vault table
            collection = db.collection("ridian_vault").where("name", "==", "usdc")
            for doc in collection.stream():
                Data = doc.to_dict()
                update_ridian_vault = db.collection('ridian_vault').document(doc.id)
                update_ridian_vault.update({"usdc_amount": float(Data['usdc_amount']) + float(usdc_amount)})
                update_ridian_vault.update({"ridian_shares": float(Data['ridian_shares'])+float(ridian_shares)})

            print("pass")
            response_object['message'] = 'success'
        else:
            print("fail")
            response_object['message'] = 'failed'

    return jsonify(response_object)


def getConvertDetail(useremail):
    docs = db.collection('convert').where('email', '==', useremail).stream()
    
    a = 0
    for doc in docs:
        stock = doc.to_dict()
        print(stock)
        a += stock['usdc_ridian_shares']

    return a
