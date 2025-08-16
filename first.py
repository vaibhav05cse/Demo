# Take n numbers from user and sort them in ascending order

n = int(input("Enter how many numbers you want to input: "))
numbers = []

for i in range(n):
    num = float(input(f"Enter number {i+1}: "))
    numbers.append(num)

numbers.sort()
print("Sorted numbers in ascending order:", numbers)