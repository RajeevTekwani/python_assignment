def odd_even(ls):
    count_odd=0
    sum_odd=0
    count_even=0
    sum_even=0
    for items in ls:
        if items%2==0:
            sum_even=sum_even+items
            count_even+=1
        else:
            sum_odd=sum_odd+items
            count_odd+=1
    print("sum of even is : ",sum_even)
    print("sum of odd is : ",sum_odd)
    print("no. of even: ",count_even)
    print("no. of odd: ",count_odd)
lst = [25,41,85,96,35,64,75,9,12,21,32,23,25,56]
odd_even(lst)