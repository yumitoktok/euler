# coding=UTF8

# 002
# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
# Find the sum of all the multiples of 3 or 5 below 1000.
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

def matchGenerator():
	a = 1
	b = 2
	
	while b < 4000000:
		next = a+b
		yield next
		a=b
		b=next
		
if __name__ == "__main__":	
	res = sum([a for a in matchGenerator() if a%2==0])+2
	print res