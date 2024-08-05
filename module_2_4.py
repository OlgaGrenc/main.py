numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# len(numbers) = values in list(numbers)
Primes_ = []
Not_Primes = []
for i in range(2, len(numbers) + 1):
    prime = True
    for j in range(2, i):
        if i % j == 0:
            prime = False
            Not_Primes.append(i)
    if prime:
        Primes_.append(i)
print(Primes_)
Not_Primes = set(Not_Primes)
Not_Primes = list(Not_Primes)
print(Not_Primes)
