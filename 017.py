# coding=UTF8

# 017
# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

import math

digits = ("one","two","three","four","five","six","seven","eight","nine")
tens   = ("ten","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety")
teens  = ("eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen")


# Lazy, only powered to 1000
def addThousands(x): 
	if x:
		return "one thousand"
	else:
		return ""

def addHundreds(x):
	if x:
		return "%s hundred" % (digits[x-1],)
	else:
		return ""

def addTens(hundred,ten,digit):
	ret = ""
	if hundred and (ten>0 or digit>0):
		ret = " and "
	if ten==1 and digit>0:
		ret = "%s%s" % (ret,teens[digit-1])
	else:
		if ten>0:
			ret = "%s%s" % (ret,tens[ten-1])
		if digit>0:
			ret = "%s %s" % (ret,digits[digit-1])
	return ret
	

def numberWordGenerator():
	for x in range(1,1001):
		xpad = "%04d" % (x,)
		thousand,hundred,ten,digit = [int(n) for n in xpad]
		str = addThousands(thousand)+addHundreds(hundred)+addTens(hundred,ten,digit)
		yield str
			

			
	
if __name__ == "__main__":
	total = 0
	for x in numberWordGenerator():	
		clean = ''.join(x.split())
		print clean
		total = total + len(clean)
	print "Total: %s" % (total)