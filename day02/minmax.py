def max(lst):
    my_list=lst[0]
    for i in range (len(lst)):
        
        if my_list<lst[i] : 
            my_list= lst[i]
    return my_list

print(max([1,5,0,15,7]))