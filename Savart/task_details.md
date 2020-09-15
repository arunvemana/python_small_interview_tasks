# Simple Api

* get any JSON output from https://openweathermap.org/api
* create Python api which send same json output.
* If current date(day) is prime,
* If current date(day) is not prime then api will send "Date is not prime so no data"/
* Add audit data in database.

**_NOTE:_**  we just take date from user for testing , instead of taking current date.

*Create a credits.json file and enter your api_key of openwhetherapi*

**_Note:_** Input date formate is http://127.0.0.1:5000/api?date=09-03-2000.
* http://127.0.0.1:5000/api (Default take *Today* date from datetime)
* http://127.0.0.1:5000/api/audit --> TO DISPLAY THE STORED AUDIT DATA ALONG WITH DATE.