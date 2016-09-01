from flask import Flask, render_template, request

import os
import datetime
import json

import responder

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])


def update_data(url):
	return responder.getHttpResponse(url)

def picker(pick):
	url = "https://www.bitstamp.net/api/v2/ticker/"+pick+"/"
	return update_data(url)

@app.route('/')
def index():
	data = update_data('https://www.bitstamp.net/api/v2/ticker/btcusd/')
	bfDate = datetime.datetime.fromtimestamp(float(data["timestamp"])).strftime('%Y-%m-%d %H:%M:%S')
	return render_template('index.html', data=data, bfDate=bfDate)

@app.route('/<pick>/')
def get_your_pick(pick):
    data = picker(pick)
    bfDate = datetime.datetime.fromtimestamp(float(data["timestamp"])).strftime('%Y-%m-%d %H:%M:%S')
    return render_template('index.html', data=data, bfDate=bfDate)

if __name__ == "__main__":
	app.run()