# Take n numbers from user and sort them in ascending order using Bubble Sort

n = int(input("Enter how many numbers you want to input: "))
numbers = []

for i in range(n):
    num = float(input(f"Enter number {i+1}: "))
    numbers.append(num)

# Bubble Sort implementation
for i in range(len(numbers) - 1):
    for j in range(len(numbers) - i - 1):
        if numbers[j] > numbers[j + 1]:
            # Swap
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

print("Sorted numbers in ascending order:", numbers)
