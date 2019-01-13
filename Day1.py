'''Question- Write a program that prints the numbers from 1 to n and for multiples of ‘3’ print “Fizz” instead of the number,
for the multiples of ‘5’ print “Buzz”, and for the numbers which are divisible by both 3 and 5, print FizzBuzz.
'''

n = int(input()) 

for i in range(1, n+1):
         if i%15 == 0:
                  print("fizzbuzz" , end = " ")
         elif i%3 == 0:
                  print("fizz", end = " ")
         elif i%5 == 0:
                  print("buzz", end = " ")
         else:
                  print(i, end = " ")
