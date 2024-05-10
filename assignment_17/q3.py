lst = [25, 41, 85, 96, 35, 64, 75, 9, 12, 21, 32, 23, 25, 56]
square_list = [x ** 2 for x in lst]
even_list = [x for x in lst if x % 2 == 0]

print("List of square elements:", square_list)
print("List of even numbers:", even_list)
