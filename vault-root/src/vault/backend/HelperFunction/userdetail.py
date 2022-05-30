# third party  import:
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase import firebase
from datetime import datetime

if not firebase_admin._apps:
    cred = credentials.Certificate({
        "type": "service_account",
        "project_id": "crypto-d33e5",
        "private_key_id": "b0701ccaccff652ddbc067ff62fce75693fb064e",
        "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQCgNkK4tmpfJ7DP\nbbAl/PMS8zv6FcpG7w6vTclfhDPVAG0dsRmAwzXj+0Ut1NHlMOl31V1iZl5CfiOF\nE+wMktu+MBo7DVCZkZOCO+zcLal5cWTwX1rHy+lyMPXeSKa+FnQjP/oQfMsa3Xf7\nhIGlFk7DvFvpaN+87JO1ciqBXOGD/frJfcfaK1vRXgZioqnozNxmBW0AXtcxfm06\nQb9PpmHhMFInLn8olS8YmLtzzhlo3ywXNb0RSb503s5Rah+G2MLLSBvSscrnkUsy\nVph7vMoLwdapuUiG+vcPBMSkZD41Rwqd9WQfENS+tYP/UmjfihXorZ/l5QZoM9qI\nY8t7m9xfAgMBAAECggEADqE10YkyyHKm5iIliiqBhdL5QJp5yKVuyVpIj7TSSNqL\nnED+S7BHvQRGamt7KTsgrqUorGIdrGO5WZ8amIFWmJTq6EaMfCF7f1J6jBaNWb4d\nkgebEhCQRjGrWft3YndJbqiabKQApfjgSnLspccWNTB/kh5WA/n0eQauU/bHzxYe\nmseiQyRDCnhoSfyGNGUPJ5l36zX+IGfCIzS0HZbO0TAjUVYPF9aki3fKCRAqV5Kl\ncQyiwlMIudzajh3dQ1FGGPJFCtN0qnK7qbi4f02n+wYibA/3ol12UYcLPwNpz/HV\ncaZJY7F4OdvZMG5vnMWlOqKxpa81L8duo+n3Utqs9QKBgQDZWPuuT+y0Sp8wrzF4\nOIbFVxhClpRiaCfuEwbwUpuZ7e8v1RguxjGWmlKiNZmvtJdhBbYgZFS+G5DQShop\nIyuS1JpT1FbnrzRqkta+d74H8+arkK83UyHQzsSrro6IVm3k85pZmG1GkPIQfwd8\n9dIQpj7L3+qSCAdea4Vw65XW9QKBgQC8tBt5u+3tEnU5vWrP50Yhd78i+9X92VHw\naEd6bUV0Ns0vsItgc5jFz5mvYDQ5dnfJ4jR7awZd4rOXcz4bruuEcGgu6U8J5RR4\n6WbnNhofmKy28wlaW9HDM2xRQKqppG4ENuPiNZUJNpgCR4Whnxq6lHYhinGuGqJn\nTunO0TdJgwKBgD9wip25dHS3Zzm1mTHnBedp4YnmG8+RaT5DTX4uDn7ihTMn9tQI\nQ4ca6k2waXhwtNK78QoJXvbSYvV4+6PQQTKtXZJkYy1i5WDKFWYo203E8ipXo9z5\nJeClyZ/25mGDILZ4KDBInnS/b/hCq7PcqID1lVS6ueP/9e6oYZ2xFd5VAoGAIpwV\n/fnN5ZFhFrn7AS612iWQVOZDlU9qi+FUWsv31RzH/Vsv9Py+pGkzEsteSLvFtK1c\nWtaCUG3n6nskhQdMAvpq4U/BQ1tUqeiFCxsNJ4ZlBxkEOiJlEpw33Z8yrfKOiw9W\nNIMHVq1ArApaJA5+ZIIeOICf4QLZjoEWuOv+a+kCgYA5uMQJXK8wFtY7jUVddxNU\nGy0Uur3l1MWV2uNCXfGd4XLbf2FYX81uIkFA7Ip1pvBiwcACMclqoFAc8e8AT9JF\nb2n782Zhrgk8xgxknkaSBbk5pC0CvmeVgw9A8dapN2ZM8AzYaIPd4hQeWM04kGce\n2M0Ej7Q7Mzu4ynqRdGmrbg==\n-----END PRIVATE KEY-----\n",
        "client_email": "firebase-adminsdk-9npbw@crypto-d33e5.iam.gserviceaccount.com",
        "client_id": "107081134227466775771",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-9npbw%40crypto-d33e5.iam.gserviceaccount.com"
        })
    default_app = firebase_admin.initialize_app(cred)

db = firestore.client()
firebase = firebase.FirebaseApplication(
    'https://crypto-d33e5-default-rtdb.asia-southeast1.firebasedatabase.app/', None)

def getUserDetail(useremail):
    docs = db.collection('registered_users').where('email','==',useremail).stream()
    for doc in docs:
        stock = doc.to_dict()
        userDetail= stock

    return userDetail


def usdcVaultTotalSupply():
    doc = db.collection('ridian_vault').document('zNlP1fyst4q6vv9trCvU').get()
    data = doc.to_dict()

    return data


def transactionCount(email):
    now = datetime.today().isoformat()
    TransactoinCount=0
    docs = db.collection('usdc_transactions').where('time','>',now).stream()
    for doc in docs:
     stock = doc.to_dict()
     if(stock['email'] == email):
         TransactoinCount+= stock['amount']
    return    TransactoinCount 
    

def getLastRecord():
   docs = db.collection('usdc_transactions').where('email','==','adeel@ridian.io').limit_to_last(1).stream()
   for doc in docs:
        stock = doc.to_dict()
        res= stock



def getConvertPannding():
    usertotalRidian = getUserDetail('adeel@ridian.io')
    now = datetime.now()
    todayDate=now.strftime("%Y-%m-%d %H:%M:%S")
    checks=db.collection("convert").where("status", '==', 'pennding').get();

    for check in checks:
        result=check.to_dict()
        print(result)
        last_convert_date =  result['created_at']
        print(last_convert_date)
        print(todayDate)
        dt_a = datetime.strptime(last_convert_date, '%Y-%m-%d %H:%M:%S')
        dt_b = datetime.strptime(todayDate, '%Y-%m-%d %H:%M:%S')
        dt=dt_b - dt_a
        print((dt.days)*24)
        print((dt.seconds//60)%60)

        if((dt.seconds//60)%60 >=2 ) :
         update_convert = db.collection('convert').document(check.id)
         update_convert.update({"status": 'success'})

         # database -->  data update in registered_users table against current user
         collection = db.collection("registered_users").where("email", "==", result['email'])
         for doc in collection.stream():
                Data = doc.to_dict()
                update_amount = db.collection('registered_users').document(doc.id)
                update_amount.update({"withdrawable_balance": float(Data['withdrawable_balance'])+float(result['usdc_amount'])})
             # database -->  data update in ridian_vault table

         collection = db.collection("ridian_vault").where("name", "==", "usdc")
         for doc in collection.stream():
                Data = doc.to_dict()
                update_amount = db.collection('ridian_vault').document(doc.id)
                update_amount.update({"usdc_amount": float(Data['usdc_amount']) + float(result['usdc_amount'])})
                update_amount.update({"ridian_shares": float(Data['ridian_shares'])+float(result['usdc_ridian_shares'])})
         
         print("Convert Successfull")
        # else:
        
        #  print("Time Limit")              
         
       


 