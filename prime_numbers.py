def is_prime(num):
    """Returns True if the number is a prime number
    else return False."""

    if num <= 1:
        return False

    for x in range(2, num):
        if num % x == 0:
            return False
    else:
        return True

def numbers(x):
	primenumbers = []
	for n in range(1,x):
		if is_prime(n):
			primenumbers.append(n)
	return primenumbers
print (numbers(100))



