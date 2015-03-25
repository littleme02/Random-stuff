# coding=utf-8
__author__ = 'LittleMe'
import csv

target_prime_amount = 20000
number_to_test = 7

modulus = 0
primes = [3, 5]

primes_found = 2

while target_prime_amount > primes_found:

    prime_to_test = 1
    primes_found = len(primes) - 1

    print("primes found  {}".format(primes_found))

    while True:
        if prime_to_test > primes_found:
            primes.append(number_to_test)
            number_to_test += 2
            break
        elif number_to_test == primes[prime_to_test]:
            number_to_test += 2
            break
        else:
            # print('dividing {} by {}'.format(number_to_test,
            #                                  primes[prime_to_test]))
            if number_to_test % primes[prime_to_test] == 0:
                # print("{} ".format(number_to_test))
                number_to_test += 2

            else:
                prime_to_test += 1
                # print(primes)
                # for x in range (0, len(primes)):
                # print(primes[x])

with open('primes.csv', 'w', encoding='utf-8', newline='') as fp:
    a = csv.writer(fp, delimiter=',')
    a.writerow(['Value'])
    a.writerow(primes)
