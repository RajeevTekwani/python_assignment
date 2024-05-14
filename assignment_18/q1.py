def merge_lists(list1, list2):
   #dono lsit ko set me convert kr diya 
    set1 = set(list1)
    set2 = set(list2)
    # fir set ka union krwa diya 
    merge_sets = set1.union(set2)
   
    return list(merge_sets)


list1 = list(input('Enter elements of list 1 seperated by space :').split())
list2 = list(input('Enter elements of list 2 seperated by space :').split())

merged_list = merge_lists(list1, list2)
print("Merged lists are : ", merged_list)