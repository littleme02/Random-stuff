__author__ = 'LittleMe'
import csv

targetprimeamount = 20000
numbertotest = 7

modul = 0
primes = ["Value"]

primes.append(3)
primes.append(5)
primesfound = 2





while targetprimeamount > primesfound:
    done = 0
    primetotest = 1
    primesfound = len(primes)-1

    print(("primes found  " + str(primesfound)), end ="\r")

    while done == 0:





        if primetotest > primesfound:
            done = 1

            primes.append(numbertotest)

            numbertotest += 2

            #print("tes")
            break


        elif numbertotest == primes[primetotest]:


            #print("ive seeen this before")
            numbertotest += 2
            done = 1
            break

        else:
            #print("deviding   " + str(numbertotest) + "  by  " + str(primes[primetotest]))

            if numbertotest % primes[primetotest] == 0:

                #print(str(numbertotest) + "   not")
                done = 1
                numbertotest += 2

            else:
                primetotest += 1





#print(primes)


#for x in range (0, len(primes)):
    #print(primes[x])



with open('primes.csv', 'w',encoding='utf-8', newline='') as fp:
    a = csv.writer(fp, delimiter=',')
    a.writerows([primes])


