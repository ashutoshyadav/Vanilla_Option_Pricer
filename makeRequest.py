#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json

url = 'http://127.0.0.1:5000/vop/'
data =	{
	"Products": [
		{
			"ProductName": "Call",
			"ProductParams":
			{
				"Underlying": "UnderlyingA",
				"Spot": 1,
				"Strike": 1,
				"Rate": 0,
				"Vol": 0.25,
				"StrikeDate": "23-Feb-18",
				"MaturityDate": "22-Feb-19"
			}
		},
		{
			"ProductName": "Put",
			"ProductParams":
			{
				"Underlying": "UnderlyingA",
				"Spot": 100,
				"Strike": 100,
				"Rate": 0.02,
				"Vol": 0.4,
				"StrikeDate": "23-Feb-18",
				"MaturityDate": "22-Feb-19"
			}
		}
	]
}
data1 = {
	"Products": [
		{
			"ProductName": "Put",
			"ProductParams":
			{
				"Underlying": "UnderlyingB",
				"Spot": 100,
				"Strike": 100,
				"Rate": 0,
				"Vol": 0.25,
				"StrikeDate": "23-Feb-18",
				"MaturityDate": "23-Feb-19"
			}
		},
		{
			"ProductName": "Call",
			"ProductParams":
			{
				"Underlying": "UnderlyingB",
				"Spot": 100,
				"Strike": 100,
				"Rate": 1.50,
				"Vol": 0,
				"StrikeDate": "23-Feb-18",
				"MaturityDate": "23-Feb-19"
			}
		},
		{
			"ProductName": "Put",
			"ProductParams":
			{
				"Underlying": "UnderlyingB",
				"Spot": 100,
				"Strike": 50,
				"Rate": 0,
				"Vol": 0.25,
				"StrikeDate": "23-Feb-18",
				"MaturityDate": "23-Feb-19"
			}
		}
	]
}
print data
data = json.dumps(data)
print data
headers = {"Content-Type": "application/json", 'data':data}
response = requests.put(url, data=data, headers=headers)

#Print Response
print(response.text)