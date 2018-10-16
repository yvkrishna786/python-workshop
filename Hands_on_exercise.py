import math
import random
# TODO: Write a print statement that displays both the type and value of `pi`
pi = math.pi
print (math.pi)

# TODO: Write a conditional to print out if `i` is less than or greater than 50
i = random.randint(0, 100)
if i<50:
    print("i is less than 50")
elif i == 50:
    print(" i is equal to 50")
elif i>50:
    print("i is greater than 50")
print(i)

# TODO: Write a conditional that prints the color of the picked fruit
picked_fruit = random.choice(['orange', 'strawberry', 'banana'])
if picked_fruit == 'orange':
    print("picked fruit is orange")
elif picked_fruit == 'strawberry':
    print("picked fruit is strawberry")
elif picked_fruit == 'banana':
    print("picked fruit is banana")
print(picked_fruit)

# TODO: Write a function that multiplies two numbers and returns the result
def mul(num1, num2):
        result = num1 * num2
        return result
print (mul(30, 40))

# TODO: Now call the function a few times to calculate the following answers
print (mul(12, 96))
print (mul(48, 17))
print (mul(196523, 87323))
