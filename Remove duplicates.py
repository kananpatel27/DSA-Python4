lst = [10,20,20,30,40,40,50]
unique_lst = []

for i in lst:
    if i not in unique_lst:
        unique_lst.append(i)
    
print("List after removing duplicates", unique_lst)
