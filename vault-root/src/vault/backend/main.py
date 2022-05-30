# third party import:
from flask import Flask
from flask import Flask, request, jsonify, json
from flask_cors import CORS, cross_origin
from flask_apscheduler import APScheduler


# file import of blueprint:
from Convert import convert_api
from Deposit import deposit_api
from Withdraw import withdraw_api


# this project  imports:
from HelperFunction.userdetail import usdcVaultTotalSupply
from HelperFunction.userdetail import getUserDetail
from HelperFunction.userdetail import getConvertPannding


app = Flask(__name__)
Cors = CORS(app)
scheduler = APScheduler()

CORS(app, resources={r'/*': {'origins': '*'}}, CORS_SUPPORTS_CREDENTIALS=True)
app.config['CORS_HEADERS'] = 'Content-Type'


#flask app divide different component using blueprint
app.register_blueprint(convert_api)
app.register_blueprint(deposit_api)
app.register_blueprint(withdraw_api)

@app.route('/detail', methods=['GET'])
def detail():
    response = {'status': 'success'}
    # usdcVaultTotalSupply()  --> Get All Detail of Matic Coin
    supply = usdcVaultTotalSupply()
    userDetail = getUserDetail('adeel@ridian.io')

    response['total_ridian_shares'] = supply['total_ridian_shares']
    response['ridian_shares'] = supply['ridian_shares']
    response['user_ridian_shares'] = userDetail['ridian_shares']
    response['withdrawable_balance'] = userDetail['withdrawable_balance']
    return jsonify(response)




def scheduleTask():
    getConvertPannding()
    print("This test runs every 60 seconds")


if __name__ == "__main__":
    scheduler.add_job(id = 'Scheduled Task', func=scheduleTask, trigger="interval", seconds=60)
    scheduler.start()
    app.run(debug=True)
