#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
from scipy.stats import norm

class VOP():


	def __d1(self,spot,strike,vol,rate,time):
		""" Term in Black-Scholes solution """
		v1 = math.log(float(spot)/float(strike))
		v2 = (rate + (vol*vol)/2.0) * time
		v3 = vol * math.sqrt(time)
		return float(v1+v2)/float(v3)

	def __d2(self,spot,strike,vol,rate,time):
		""" Term in Black-Scholes solution """
		return self.__d1(spot,strike,vol,rate,time) - vol * math.sqrt(time)


	def getCallPrice(self,spot,strike,vol,rate,time):
		""" Price a call option using Black-Sholes """
		v1 = self.__d1(spot,strike,vol,rate,time)
		v2 = self.__d2(spot,strike,vol,rate,time)
		res = {}
		res['price'] = spot * norm.cdf(v1) - strike * math.exp(-rate*time) * norm.cdf(v2)
		T_sqrt = math.sqrt(time)
		res['delta'] = norm.cdf(v1)
		res['gamma'] = norm.pdf(v1)/(spot*vol*T_sqrt)
		res['theta'] = -(spot*vol*norm.pdf(v1)) / (2*T_sqrt)- rate*strike * math.exp(-rate*time) * norm.cdf(-v2)
		res['vega'] = (spot * T_sqrt * norm.pdf(v1))/100.0
		return res

	def getPutPrice(self,spot,strike,vol,rate,time):
		""" Price a put option using Black-Sholes """
		v1 = self.__d1(spot,strike,vol,rate,time)
		v2 = self.__d2(spot,strike,vol,rate,time)
		res = {}
		print 'getPutPrice called;'
		res['price'] = strike * math.exp(-rate*time) * norm.cdf(-v2) - spot * norm.cdf(-v1)
		T_sqrt = math.sqrt(time)
		res['delta'] = -norm.cdf(-v1)
		res['gamma'] = norm.pdf(v1) / (spot * vol * T_sqrt)
		res['theta'] =  (-(spot * vol * norm.pdf(v1)) / (2 * T_sqrt)) - (rate * strike * math.exp(-rate * time) * norm.cdf(v2))
		res['vega'] = (spot * T_sqrt * norm.pdf(v1))/100.0
		return res

if __name__=="__main__":
	VOP()
