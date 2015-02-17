# coding=UTF8

# 005
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

import math

def candidateGenerator():
	i=2520
	while True:
		yield i
		i+=20
	
def checkCandidate(c):	
	n=20
	while n > 10:
		if c%n!=0:
			#print "Fail: %s %s" % (c,n,)
			return False
		n-=1
	return True	
		
		
if __name__ == "__main__":	
	for c in candidateGenerator():
		if checkCandidate(c):
			print c
			break
	
	