import random

rand_num = random.random() # returns random num 0 - 1 exclusive
# Task: print random number between 1-10
num = 4.55
int(num) # returns 4
print(int(num* 10)) # print 45
# print(rand_num * 10)


# answer
print("Random number, 1 - 100", int(rand_num*100) + 1)
