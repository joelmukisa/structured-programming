print("Enter 5 numbers:")
numbers = []
for i in range(5):
    num = float(input())

    numbers.append(num)

print("\nNumbers:",numbers)

maximum = max(numbers)
minimum = min(numbers)
average = sum(numbers) / len(numbers)

print("Maximum:",maximum)
print("Minimum:",minimum)
print("Average:",average)   

sorted_numbers = sorted(numbers)
print("Sorted:",sorted_numbers)




