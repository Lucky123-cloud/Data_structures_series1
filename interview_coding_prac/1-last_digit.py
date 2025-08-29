# #!/usr/bin/python3
# import random
# number = random.randint(-10000, 10000)
# # YOUR CODE HERE
# rem = abs(number) % 10
# if number < 0:
#     rem *= -1
# if rem > 5:
#     print(f"Last digit of {number} is {rem} and is greater than 5")
# elif rem == 0:
#     print(f"Last digit of {number} is {rem} and is 0")
# else:
#     print(f"last digit of {number} is {rem} and is less than 6 and not 0")


#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
if number >= 0:
    last_digit = number % 10
else:
    last_digit = ((number * -1) % 10) * -1

message = "Last digit of %d is %d and is " % (number, last_digit)

if last_digit == 0:
    print(message, "0")
elif last_digit > 5:
    print(message, "greater than 5")
else:
    print(message, "less than 6 and not 0")

