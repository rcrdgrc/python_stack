# Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
# Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]
def biggie_size(arr):
    new_arr = []
    for num in arr:
        if num >= 0:
            new_arr.append("big")
        else:
            new_arr.append(num)
    return new_arr

print(biggie_size([-1,3,5,-5]))


# Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. 
# (Note that zero is not considered to be a positive number).
# Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
# Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it

def positive(arr):
    count = 0
    for i in range(len(arr)):
        if arr[i] > 0:
            count += 1
        if i == len(arr) - 1:
            arr[i] = count
    
    return arr

print(positive([1,6,-4,-2,-7,-2]))

# Sum Total - Create a function that takes a list and returns the sum of all the values in the list.
# Example: sum_total([1,2,3,4]) should return 10
# Example: sum_total([6,3,-2]) should return 7
def sum_total(arr):
    sum = 0
    for num in arr:
        sum += num
    return sum

print(sum_total([1,2,3,4]))

# Average - Create a function that takes a list and returns the average of all the values.x
# Example: average([1,2,3,4]) should return 2.5
def average(arr):
    sum = sum_total(arr)
    print(sum)
    print(len(arr))
    return float(sum) / len(arr)

print(average([1,2,3,4]))

# Length - Create a function that takes a list and returns the length of the list.
# Example: length([37,2,1,-9]) should return 4
# Example: length([]) should return 0
def length(arr):
    return len(arr)

print(length([]))

# Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
# Example: minimum([37,2,1,-9]) should return -9
# Example: minimum([]) should return False
def minimum(arr):
    if len(arr) == 0:
        return False
    
    min = arr[0]
    for num in arr:
        if num < min:
            min = num
    
    return min

print(minimum([37,2,1,-9]))

# Maximum - Create a function that takes a list and returns the maximum value in the list. If the list is empty, 
# have the function return False.
# Example: maximum([37,2,1,-9]) should return 37
# Example: maximum([]) should return False
def maximum(arr):
    if len(arr) == 0:
        return False
    
    max = arr[0]
    for num in arr:
        if num > max:
            max = num
    
    return max

print(maximum([37,2,1,-9]))
# Ultimate Analysis - Create a function that takes a list and returns a dictionary 
# that has the sumTotal, average, minimum, maximum and length of the list.
# Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }
def ultimate_analysis(arr):
    analysis = {
        "sumTotal": sum_total(arr),
        "average": average(arr),
        "minimum": minimum(arr),
        "maximum": maximum(arr),
        "length": length(arr),
    }

    return analysis

print(ultimate_analysis([37,2,1,-9]) )
# Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
# Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]