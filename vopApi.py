#!/usr/bin/env python
# -*- coding: utf-8 -*-

from vop import VOP
from flask import Flask, request, render_template,jsonify
from flask_restful import Resource, Api
from datetime import date
import json

app = Flask("Vanila Option Pricer")
api = Api(app)
pricer = VOP()

@app.route('/vop/')
def home():
	""" Rendering the HTML Homepage """
	return render_template('index.html')


def __getPeriod(d1,d2):
	""" Calculate the Time Period between 2 dates in Years """
	d1 = map(int,d1.split('-'))
	d1 = date(d1[0],d1[1],d1[2])
	d2 = map(int,d2.split('-'))
	d2 = date(d2[0],d2[1],d2[2])
	delta = d1-d2
	return float(delta.days)/365.0


@app.route('/vop/',methods=['POST'])
def post():
	""" Method for Handling POST requests recieved from the HTML Homepage """
	try:
		spot = request.form['spot']
		strike = request.form['strike']
		vol = request.form['vol']
		rate = request.form['rate']
		sd = request.form['strike-date']
		md = request.form['maturity']
		t = request.form['type']
		d = {}
		d['spot'] = float(spot)
		d['strike'] = float(strike)
		d['vol'] = float(vol)
		d['rate'] = float(rate)
	except:
		res = {}
		res['Code'] = 405
		res['Message'] = 'Invalid Input!'
		return json.dumps(res)
	d['Strike-Date'] = sd
	d['Maturity-Date'] = md
	d['type'] = t
	try:
		d['period'] = __getPeriod(md,sd)
	except:
		res = {}
		res['Message'] = 'Bad Request! Option Type Not recognized'
		return jsonify(res)
	if(d['period']<=0):
		res = {}
		res['Message'] = 'Bad Request! Maturity Date should be later than Strike Date'
		return json.dumps(res)
	if t=="call":
		res = pricer.getCallPrice(float(spot),float(strike),float(vol),float(rate),d['period'])
		d['price'] = round(res['price'],5)
		d['delta'] = round(res['delta'],5)
		d['gamma'] = round(res['gamma'],5)
		d['theta'] = round(res['theta'],5)
		d['vega'] = round(res['vega'],5)
	elif t=='put':
		res = pricer.getPutPrice(float(spot),float(strike),float(vol),float(rate),d['period'])
		d['price'] = round(res['price'],5)
		d['delta'] = round(res['delta'],5)
		d['gamma'] = round(res['gamma'],5)
		d['theta'] = round(res['theta'],5)
		d['vega'] = round(res['vega'],5)
	else:
		res = {}
		res['Message'] = 'Bad Request! Option type not recognized'
		return json.dumps(res)
	res =  json.dumps(d)
	print res
	return res


def __format(d1):
	""" Format the date into all numerical form dd-mm-yyyy """
	d1[1] = {
		'Jan' : 1,
		'Feb' : 2,
		'Mar' : 3,
		'Apr' : 4,
		'May' : 5,
		'Jun' : 6,
		'Jul' : 7,
		'Aug' : 8,
		'Sep' : 9,
		'Oct' : 10,
		'Nov' : 11,
		'Dec' : 12
	}[d1[1]] 
	if(len(d1[2])==2):
		d1[2] = '20'+d1[2]
	for i in xrange(len(d1)):
		d1[i] = int(d1[i])
	return d1


def __processPutRequest(data):
	""" Calculate teh Price for a single Product """
	try:
		spot = float(data['ProductParams']['Spot'])
		strike = float(data['ProductParams']['Strike'])
		rate = float(data['ProductParams']['Rate'])
		vol = float(data['ProductParams']['Vol'])
		sd = data['ProductParams']['StrikeDate'].split('-')
		md = data['ProductParams']['MaturityDate'].split('-')
	except:
		data['Message'] = 'Bad Request! Poor Data Format'
		return data

	try:
		sd = __format(sd)
		md = __format(md)
		sd = date(sd[2],sd[1],sd[1])
		md = date(md[2],md[1],md[1])
		delta = md-sd
	except:
		data['Message'] = 'Bad Request! Not recognized Date Format!'
		return data
		
	period = float(delta.days)/365.0
	if period<=0:
		data['Message'] = 'Bad Request! Maturity Date should be later than Strike Date.'
	try:
		if data['ProductName'].lower()=="put":
			res = pricer.getPutPrice(spot,strike,vol,rate,period)
			data['price'] = res['price']
			data['delta'] = res['delta']
			data['gamma'] = res['gamma']
			data['theta'] = res['theta']
			data['vega'] = res['vega']
		elif data['ProductName'].lower()=="call":
			res = pricer.getCallPrice(spot,strike,vol,rate,period)
			data['price'] = res['price']
			data['delta'] = res['delta']
			data['gamma'] = res['gamma']
			data['theta'] = res['theta']
			data['vega'] = res['vega']
		else:
			data['Message']='Wrong option Choice. '+data['ProductName']+' is not recognized'
		return data
	except:
		data['Message'] = 'Bad Request!'
		return data
	

@app.route('/vop/',methods=['PUT'])
def put():
	""" Handling Put Requests """
	print request.headers
	try:
		data = request.headers['data']
	except:
		res = {}
		res['Message'] = 'Bad Request!'
		return json.dumps(res)
	try:
		data = json.loads(data)
	except:
		res = {}
		res['Message'] = 'Bad JSON.'
		return json.dumps(res)
	res = []
	try:
		for item in data['Products']:
			res.append(__processPutRequest(item))
	except:
		res = {}
		res['Message'] = 'Bad Request!'
		return json.dumps(res)
	result = {}
	result['Products'] = res
	return json.dumps(result)


if __name__=="__main__":
	app.run(port=5000)
