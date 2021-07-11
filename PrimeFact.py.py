list_of_prime_facts = []
def prime_fact(num):
    for i in range(2,100):
        while (num %i == 0):
            res = int(num/i)
            print (str(i) + "times "+ str(num)+ " is " + str(res))
            num = res
            list_of_prime_facts.append(i)

prime_fact(630)
print (list_of_prime_facts)