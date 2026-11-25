
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))
oc = 0
ec = 0
for i in range(start, end + 1):
    if i % 2 == 0:
        print(f"{i} is even.")
        ec += 1
    else:
        print(f"{i} is odd.")
        oc += 1
print(f"Count of even numbers between {start} and {end}: {ec}")
print(f"Count of odd numbers between {start} and {end}: {oc}")    

lengts = int(input("Enter the length: "))
oc1 = 0
ec1 = 0
for i in range(lengts):
    if i % 2 == 0:
        print(f"{i} is even.")
        ec1 += 1
    else:
        print(f"{i} is odd.")
        oc1 += 1
print(f"Count of even numbers: {ec1}")
print(f"Count of odd numbers: {oc1}")    

#time bomb
import time

t = int(input("Enter the countdown time in seconds: "))
for _ in range(t, 0, -1):
    print(f"Time remaining: {_} seconds")
    time.sleep(1)
time.sleep(1)
print("BOOM! Time is up.")

#multiplication table
num = int(input("num = ")) 
time.sleep(1)
print(f"Multiplication table for {num}:")
time.sleep(1)
for i in range(1, 11):
    time.sleep(1)
    print(f"{num} x {i} = {num * i}")    
time.sleep(1)