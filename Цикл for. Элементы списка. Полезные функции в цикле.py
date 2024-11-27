numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = True
for number in numbers:
    if number == 1:
        continue
    for j in range(2, number):
        if number % j == 0:
            break
    else:
        primes.append(number)
    if number % 2 == 0 and number != 2 or number % 3 == 0 and number != 3:
        continue
    is_prime = False
    not_primes.append(number)

print(primes)
print(not_primes)