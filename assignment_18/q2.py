def list_intersection(list1, list2):
   #dono lsit ko set me convert kr diya 
    set1 = set(list1)
    set2 = set(list2)
    # fir set ka intersection krwa diya 
    intersect_list = set1.intersection(set2)
   
    return list(intersect_list)


list1 = list(input('Enter elements of list 1 seperated by space :').split())
list2 = list(input('Enter elements of list 2 seperated by space :').split())

intersected_list = list_intersection(list1, list2)
print("Merged lists are : ", intersected_list)