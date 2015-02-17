# coding=UTF8

# 003
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?


def factorise(target):
	t = 2
	while t < target:
		#print "%s %s = %s" % (target,t,target%t)
		if target%t==0:
			return t
		t+=1
	return 0	
		
if __name__ == "__main__":	
	t=1
	target = 600851475143
	factors = []
	while t>0:
		t = factorise(target)
		if (t):
			target = target/t
			factors.append(t)
		else:
			factors.append(target)
	print factors
		
	
