# third party import:
from flask import request
from requests import Request, Session
from flask import Flask, request, jsonify, json
from flask import Blueprint
import datetime


# this project  import:
from HelperFunction.getdeposithistory import get_deposit_history
from HelperFunction.randomword import randomword
from HelperFunction.transaction import transaction
from HelperFunction.userdetail import usdcVaultTotalSupply
from HelperFunction.userdetail import transactionCount



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

deposit_api = Blueprint('deposit_api', __name__)
session = Session()

@deposit_api.route("/dataentry", methods=["POST", "GET"])
def submitData():

    response_object = {'status': 'success'}
    if request.method == "POST":
        post_data = request.get_json()

        amount = post_data.get('amount')
        coin = post_data.get('coin')
        userTransactionCount= transactionCount('adeel@ridian.io')

        now = datetime.datetime.now()
        todayDate=now.strftime("%Y-%m-%d %H:%M:%S")
       
        print(userTransactionCount)

       
        
        deposit_address = '0xC1d203247F827Ab2b6EBF9E67351eBf4347D282b'
        api_key = 'I5mLyHv9iVbPaNYwuDTnQrMS-bIBCQ-uZAS0szCU'
        secrets_key = 'spIQBiRHoeY3eVgluoFgmDNM-gflxYfTYH57em_f'
        # call withdraw function
        
        suppldata = usdcVaultTotalSupply()    
        percentage=(20 * suppldata['total_usdc_amount']) / 100.0     
        print(percentage)
        if(coin == 'MATIC' and userTransactionCount+float(amount) <=1000  and  userTransactionCount <= percentage):

            data = transaction(amount, coin, deposit_address, api_key, secrets_key)
            # usdcVaultTotalSupply() --> count total matic supply
           
            supply = suppldata['usdc_amount']
             # usersMaticCount() --> total matic count specific user
            collection = usersMaticCount()
            finalresult = float(collection) + float(amount)
            remaining_shares = float(supply)-float(collection)
            if(supply >= finalresult):
                session = Session()
                resp = session.send(data)
                res = resp.json()
                print(res)
                if (res['success'] == True):

                  # user deposit amount update
                    collection = db.collection("registered_users").where(
                        "email", "==", "adeel@ridian.io")
                    for doc in collection.stream():
                        Data = doc.to_dict()
                        update_register_users = db.collection('registered_users').document(doc.id)
                        update_register_users.update({"usdc_amount": float(Data['usdc_amount'])+float(amount)})
                        update_register_users.update({"ridian_shares": float(Data['ridian_shares'])+float(amount)*2})
                        update_register_users.update({"last_deposit_date": todayDate})
                    #data save in matic_transaction table against user
                    db.collection('usdc_transactions').document(randomword(10)).set(
                        {
                            "email": "adeel@ridian.io",
                            "Total_usdc_Ridian_shares": float(Data['ridian_shares'])+float(amount)*2,
                            "current_minted_shares ": float(amount)*2,
                            "coin": res["result"]["coin"],
                            "amount": res["result"]["size"],
                            "time": res["result"]["time"],
                        })
                        #data save in deposit_history table against user

                    db.collection('deposit_history').document(randomword(10)).set(
                        {
                            "email": "adeel@ridian.io",
                            "transaction_id": res["result"]["id"],
                            "coin": res["result"]["coin"],
                            "amount": res["result"]["size"],
                            "time": res["result"]["time"],
                            "status": res["result"]["status"],
                        }
                    ) 
                    #update ridian_valut table
                    updateStakeCoin(float(amount))
                    #get deposit history detail
                    deposit_history = get_deposit_history()
                    x = session.send(deposit_history)
                    deposits_res = x.json()
                    if (deposits_res['success'] == True):
                        for elem in deposits_res["result"]:
                            if elem["id"] == res["result"]["id"]:
                                print("Deposit matched")
                                break
                            else:
                                response_object['message'] = 'Deposit not matched'
                                print('Deposit not matched')
                                return jsonify(response_object)
                    else:
                        response_object['message'] = deposits_res['error']
                        print(deposits_res['error'])
                        return jsonify(response_object)

                    response_object['message'] = 'success'
                    response_object['remaining_shares'] = remaining_shares
                    print("add")

                else:
                    response_object['message'] = res['error']
                    print(res['error'])
                    return jsonify(response_object)

            else:
                response_object['message'] = 'failed'
                print("failed")
        else:  
         response_object['message'] = 'Limit Reached'     
         print("Limit Reached")

        return jsonify(response_object)



def usersMaticCount():
    docs = db.collection('usdc_transactions').stream()
    a = 0
    for doc in docs:
        stock = doc.to_dict()
        a += stock['amount']
    return a


def updateStakeCoin(amount):
    collection = db.collection("ridian_vault").where("name", "==", "usdc")
    for doc in collection.stream():
        Data = doc.to_dict()
        update_ridian = db.collection('ridian_vault').document(doc.id)
        update_ridian.update({"usdc_amount": float(Data['usdc_amount'])-amount})
        update_ridian.update({"ridian_shares": float(Data['ridian_shares'])-amount*2})

    return "update"
