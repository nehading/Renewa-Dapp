from web3 import Web3
from marshmallow import Schema, fields, ValidationError
from flask import Flask, Response, request, jsonify, session

#from flask.session import Session
import json
from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)

# SESSION_TYPE = 'filesystem'
# app.config.from_object(__name__)
# Session(app)

# # web3.py instance
# try:
#     w3 = Web3(Web3.currentProvider)
# except:
#     # set the provider you want from Web3.providers
#     #w3 = Web3(Web3.HTTPProvider("http://localhost:8545"))
#     "https://mainnet.infura.io/
#
# #w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
# #w3 = Web3(Web3.HTTPProvider("https://ropsten.infura.io/v3/"))
# # test
# print("Connected to infura url: " + str(w3.isConnected()))
# print("Ethereum Block Number: " + str(w3.eth.blockNumber))
# # test
# w3.eth.defaultAccount = w3.eth.accounts[0]
# # Get stored abi and contract_address
#
# with open("DigitalRECdata.json", 'r') as f:
#     datastore = json.load(f)
#     abi = datastore["abi"]
#     contract_address = datastore["address"]


# the majority of the logic, including interacting with the deployed smart contract and saving state is implemented in the html files
# via web3.js and javascript
wallet_address = 0


@app.route("/<name>/<acc>")
def home_view_guest(name, acc):
    wallet_address = acc
    return render_template('home.html', name=name, acc=acc)


@app.route("/")
def show():
    return render_template('login.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        acc = request.form['acc']
        # session['user'] = user
        return redirect(url_for('home_view_guest', name=user, acc=acc))
    else:
        user = request.args.get('nm')
        acc = request.form['acc']

        # session['user'] = user
        return redirect(url_for('home_view_guest', name=user, acc=acc))


@app.route("/uploadpage")
def uploadpage():
    return render_template('upload.html', acc=wallet_address)


@app.route("/purchasepage")
def purhcasepage():
    return render_template('purchase.html', acc=wallet_address)


@app.route("/viewpage")
def viewpage():
    return render_template('view.html', acc=wallet_address)


@app.route('/mint', methods=['POST', 'GET'])
def mint():
    if request.method == 'POST':
        #user = request.form['nm']
        price = request.form['price']
        state_id = request.form['state_id']

    else:
        #user = request.args.get('nm')
        price = request.args.get('price')
        state_id = request.args.get('state_id')

    return render_template('minted.html', state_id=state_id, price=price, acc=wallet_address)


@app.route('/transferred', methods=['POST', 'GET'])
def transferred():
    if request.method == 'POST':
        rec_id = request.form['rec_id']

    else:
        rec_id = request.args.get('rec_id')

    return render_template('transferred.html', rec_id=rec_id, acc=wallet_address)


if __name__ == '__main__':
    app.debug = True
    app.run()


# api to set new user every api call


# @app.route("/blockchain/user", methods=['POST'])
# def user():
#     # Create the contract instance with the newly-deployed address
#     user = w3.eth.contract(address=contract_address, abi=abi)
#     body = request.get_json()
#     result, error = UserSchema().load(body)
#     if error:
#         return jsonify(error), 422
#     tx_hash = user.functions.setUser(
#         result['name'], result['gender']
#     ).transact()
#     # Wait for transaction to be mined...
#     receipt = w3.eth.waitForTransactionReceipt(tx_hash)
#     user_data = user.functions.getUser().call()
#     return jsonify({"data": user_data}), 200
