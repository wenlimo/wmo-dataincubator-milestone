# -*- coding: UTF-8 -*-
"""
hello_flask: First Python-Flask webapp
"""
from flask import Flask, render_template, request
from functions import tickerrequest
import os
app = Flask(__name__)

@app.route('/')
def main():
#    return render_template('j2_query.html')
    return render_template('request_query.html')

@app.route('/process', methods=['POST'])
def process():
    tickersymbol = request.form.get('tickersymbol')
    start_date = request.form.get('start_date')
    end_date = request.form.get('end_date')
    return tickerrequest(tickersymbol, start_date, end_date)
#    if tickersymbol:
#        return 'ticker:', tickersymbol
#    else:
#        return 'NO!'
    

#def process():
#    # Retrieve the HTTP POST request parameter value from 'request.form' dictionary
#    _username = request.form.get('username')  # get(attr) returns None if attr is not present
# 
#    # Validate and send response
#    if _username:
#        return render_template('j2_response.html', username=_username)
#    else:
#        return 'Please go back and enter your name...', 400  # 400 Bad Request

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)