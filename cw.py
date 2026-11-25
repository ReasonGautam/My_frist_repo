# All numbers from 1 to 20
for i in range(1, 21):
    print(i)        

# All odd numbers from 1 to 15
for i in range(1, 16, 2):
    print(i, end = ", ")   

#printing name seven times and then printing done one time
for i in range(7):
    print("Reason")
print("Done!")

#Ask the user for number n and print the sum of numbers from 1 to n
n = int(input("n = "))
sum = 0
for i in range(1, n + 1):
    sum += i
print(f"The sum of numbers from 1 to {n} is: {sum}")

# multiplication table of 9
for i in range(1, 11):
    print(f"9 x {i} = {9 * i}")

# Ask the user for a word and print the number of vowels in that word
W = input("Enter a word: ").lower()
vowels = "aeiou"
count = 0
for char in W:
    if char in vowels:
        count += 1
print(f"There are {count} vowels in the word '{W}'.")

# print numbers from 10 to 1 in reverse order
for i in range(10, 0, -1):
    print(i)    

# Find the factoral of 6 using a for loop
factorial = 1
for i in range(1,7):
    factorial *= i
print(f"The factorial of 6 is: {factorial}")


