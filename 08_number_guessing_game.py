#Simple number guessing game – set a secret number (e.g. 7), ask user to guess in a while loop, give hints (“too high” / “too low”), and stop when correct. Limit to max 5 attempts.

secret_number = 7
attempt = 0
max_attempt = 5
while attempt < max_attempt:
    print("this is number guessing game ")
    num = int(input("enter the number (1 to 50 ) :  "))
    attempt += 1
    if(num == secret_number ):
        print("number guessed is correct ")
        break
    elif(num > secret_number):
        print("number is lower than this ")
    else:
        print("number is higher than this ")
if num != secret_number :
    print("out of attempts , the number was" ,  secret_number)
