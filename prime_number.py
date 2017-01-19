def generate_primes(n):

	primes = []
	for num in range (2, n + 1):
		isPrime = True
		for x in range (2, num):
			if num % x == 0:
				isPrime = False
		if isPrime:
			primes.append(num)

	return primes