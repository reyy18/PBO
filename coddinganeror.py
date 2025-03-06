def calculate_average(numbers):
     total = sum(numbers)
     average = total / len(numbers)
     return average

result = calculate_average([5,5,7,8]) #input yang benar adalah list
print(result)
