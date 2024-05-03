import numpy as np

def min_max_per_row(array):
    min_max_array = np.zeros((array.shape[0], 2), dtype=int)  
    
    for i, row in enumerate(array):
        min_val = np.min(row)
        max_val = np.max(row)
        min_max_array[i] = [min_val, max_val]
    
    return min_max_array


array = np.random.randint(0, 100, size=(12, 5))
print("Original Array:")
print(array)
result = min_max_per_row(array)


print("\nMinimum and Maximum elements in each row:")
print(result)
