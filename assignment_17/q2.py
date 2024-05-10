## linear search
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1  # Return -1 if target element is not found

# Take user input for the array
arr = list(map(int, input("Enter the elements of the array separated by spaces: ").split()))
target = int(input("Enter the target element to search for: "))
result = linear_search(arr, target)

if result != -1:
    print(f"Target element {target} found at index {result}")
else:
    print(f"Target element {target} not found in the list")




### binary search

def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid 
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  

arr = [1, 2, 4, 6, 7, 9]
target = 9
result = binary_search(arr, target)
if result != -1:
    print(f"Target element {target} found at index {result} using binary search")
else:
    print(f"Target element {target} not found in the list using binary search")
