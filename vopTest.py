import unittest
from vop import VOP

class VOPTest(unittest.TestCase):

	def setUp(self):
		self.obj = VOP()

	def test_getCallPrice(self):
		res = self.obj.getCallPrice(100,100,0.4,0.02,1)
		self.assertTrue(len(res)==5)
		self.assertTrue('price' in res)
		self.assertTrue('delta' in res)
		self.assertTrue('gamma' in res)
		self.assertTrue('theta' in res)
		self.assertTrue('vega' in res)
		self.assertTrue(round(res['price'],1)==16.7)
		self.assertTrue(round(res['delta'],3)==0.599)
		self.assertTrue(round(res['gamma'],4)==0.0097)
		self.assertTrue(round(res['vega'],3)==0.387)

	def test_getPutPrice(self):
		res = self.obj.getPutPrice(100,100,0.4,0.02,1)
		self.assertTrue(len(res)==5)
		self.assertTrue('price' in res)
		self.assertTrue('delta' in res)
		self.assertTrue('gamma' in res)
		self.assertTrue('theta' in res)
		self.assertTrue('vega' in res)
		self.assertTrue(round(res['price'],1)==14.7)
		self.assertTrue(round(res['delta'],3)==-0.401)
		self.assertTrue(round(res['gamma'],4)==0.0097)
		self.assertTrue(round(res['vega'],3)==0.387)


if __name__=="__main__":
	unittest.main()