from flask import Flask
from flask import request
from datetime import datetime
import requests
from flask import jsonify
from flask import make_response
import json
app = Flask(__name__)
try:
    with open("credits1.json","r") as f:
        credits = json.load(f)
        print(credits['api_key'])
except FileNotFoundError:
    print("please create a file with credits and add your api_key of openweathermap")

@app.route('/api')
def hello():
    try:
        date = request.args.get('date',default=datetime.today(), type=str)
        if type(date) != datetime:
            date = datetime.strptime(str(date), '%d-%m-%Y')
        day = date.day
        if day > 1:
            for i in range(2,day//2):
                if (day % i) ==0:
                    return make_response(jsonify(error="Date is not prime so no data"), 404)
                    break
            else:
                data = requests.get("https://api.openweathermap.org/data/2.5/onecall",
                params = {'lat':17.3850,'lon':78.4867,
                'exclude':'hourly,daily','appid':credits['api_key']},
                headers = {'Content-Type':'application/json', 'charset':'utf-8'})
                return make_response(data.json(), 200)
        else:
            return make_response(jsonify(error="Date is not prime so no data"), 404)
    except Exception as e:
        return make_response(jsonify(error="Error at server side,please contact me!"), 500)

if __name__ == "__main__":
    app.run()