# a) Python Program - Print Date and Time

import datetime
print("Do you want to print Today's Date and Time ? (y/n): ")
check = input()
if check == 'n':
    exit()
else:
    print("\nToday's date and time is:")
    print(datetime.datetime.today())
    

# b) Print out all the even numbers from the below given list of numbers. Write the solution into a function and have it called in your main block for the requested answer

numbers = [{'sequence': '951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544, 615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941, 386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470, 743, 527'}]
number1 = numbers[0]
string2 = number1['sequence']
str1 = string2.split(", ")
array1 = []
for i in str1:
	if (int(i) % 2) == 0:
		array1.append(i)
print ("Even numbers are listed below")
print (array1)