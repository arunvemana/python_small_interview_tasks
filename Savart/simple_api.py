from flask import Flask
from flask import request
from datetime import datetime
import requests
from flask import jsonify
from flask import make_response
import json
# database link
import sqlite3

app = Flask(__name__)
# getting api_creditins from the credits.json file
try:
    with open("credits.json", "r") as f:
        credits = json.load(f)
        print(credits['api_key'])
except FileNotFoundError:
    print("please create a file with credits and add \
        your api_key of openweathermap")
# setting up the database


def data_base_insert(date_v=None, data=None):
    database_conn = sqlite3.connect("simplejson.db")
    cursor_v = database_conn.cursor()
    table_YesNo = cursor_v.execute("SELECT name FROM sqlite_master \
         WHERE type='table' AND name='simpleApi';").fetchone()
    print(table_YesNo)
    if table_YesNo is None:
        print("create a Database")
        print("Creating a table")
        try:
            cursor_v.execute("CREATE TABLE simpleApi (id INTEGER PRIMARY KEY AUTOINCREMENT,date varchar(50), data json)")
            print("Creation of the table was succesful")
            if date_v and data:
                cursor_v.execute("INSERT INTO simpleApi (date,data) VALUES(?,?)",[str(date_v),json.dumps(data)])
            return None
            database_conn.commit()
        except Exception as e:
            print(e)
    else:
        # cursor_v.execute("drop table simpleApi")
        db_data = cursor_v.execute("select id,date,json(data) from simpleApi")
        # print(db_data.fetchall())
        if date_v and data:
            cursor_v.execute("INSERT INTO simpleApi (date,data) VALUES(?,?)",[str(date_v),json.dumps(data)])
            database_conn.commit()
        else:
            return db_data.fetchall()
        print("connecting to the existing Database")
        print("Connecting to the existing table")

@app.route('/api')
def hello():
    try:
        date = request.args.get('date',default=datetime.today(), type=str)
        if type(date) != datetime:
            date = datetime.strptime(str(date), '%d-%m-%Y')
        day = date.day
        if day > 1:
            for i in range(2, day//2):
                if (day % i) ==0:
                    return make_response(jsonify(error="Date is not prime so no data"), 404)
                    break
            else:
                data = requests.get("https://api.openweathermap.org/data/2.5/onecall",
                params = {'lat':17.3850,'lon':78.4867,
                'exclude':'hourly,daily','appid':credits['api_key']},
                headers = {'Content-Type':'application/json', 'charset':'utf-8'})
                data_base_insert(date,data.json())
                return make_response(data.json(), 200)
        else:
            return make_response(jsonify(error="Date is not prime so no data"), 404)
    except Exception as e:
        return make_response(jsonify(error=f"Error at server side,please contact me! and error is {e}"), 500)


@app.route('/api/audit')
def audit():
    total_rows = data_base_insert()
    if total_rows:
        # print(total_rows)
        temp_list = []
        for index,row in enumerate(total_rows):
            d = dict()
            # print(row[0])
            d['id'] = row[0]
            d['date'] = row[1]
            d['data'] = json.loads(row[2])
            temp_list.append(d)
        return jsonify(Search_History = temp_list)

if __name__ == "__main__":
    app.run()