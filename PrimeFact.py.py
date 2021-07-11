#Meaning of prime factors => any given number we are interested in its prime factors until we reach end
list_of_prime_facts = []
divisor = 2
def prime_fact(num,divisor):
    while (divisor <= num):
        if ( num % divisor == 0):
            res = int(num/divisor)
            print (str(divisor) + "times "+ str(num)+ " is " + str(res))
            num = res
            list_of_prime_facts.append(divisor)
        else:
            divisor += 1

prime_fact(630,2)
print (list_of_prime_facts)
