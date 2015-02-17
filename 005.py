# coding=UTF8

# 005
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

import math

def candidateGenerator():
	y = 999
	while y > 99:
		x = 999
		while x > 99:
			yield (x*y)
			x=x-1
		y=y-1

def isPalindrome(x):
	s = str(x)
	l = int(math.floor(len(s)/2))
	start = int(s[:l])
	end   = int(s[-l:][::-1])
	return start==end
	
		
if __name__ == "__main__":	
	mx = reduce(max,[c for c in candidateGenerator() if isPalindrome(c)==True])
	print "MX = %s" % (mx,)