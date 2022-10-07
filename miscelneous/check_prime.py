# Ques. Write a code to check whether no is prime or not. 
# Condition use function check() to find whether entered no is positive or negative ,if negative then enter the no, 
# And if yes pas no as a parameter to prime() and check whether no is prime or not?

# TODO:
def is_prime(num):
    if num <= 1:
        return False
    elif num == 2:
        return True
    