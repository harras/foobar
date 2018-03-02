def answer(n):
	primes = [2] 	# Initialize a list of primes with just 2
	primes_str = "2"
	num = 3			# Start iterating from 3
	while len(primes_str) < n+5:
		isPrime = True
		for i in primes:
			if num%i == 0:
				isPrime = False
				break
			elif i**2 > num: 	# No need to keep looking for factors 
				break			# past sqrt(num)
		if isPrime:
			primes.append(num)
			primes_str += str(num)
		num += 1

	return primes_str[n:n+5]




print answer(3) # input's tested here