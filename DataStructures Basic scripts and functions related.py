#List comprehensions

st = 'Create a list of the first letters of every word in this string'

[word[0] for word in st.split()]

#Map usage

names = ['Gopi','Sreekanth','Chukkapalli']

list(map(lambda x: x[0],names))

#Fizz Buzz program

for num in range(1,101):
    if num %3 == 0 and num %5 == 0:
        print(f"FizzBuzz and {num}")
    elif num %3 == 0:
        print(f"Fizz and {num}")
    elif num %5 == 0:
        print(f"Buzz and {num}")