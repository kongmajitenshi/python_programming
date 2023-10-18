def count_duplicates(li) :
    li_dict = {}
    for i in li :
        if i not in li_dict :
            li_dict[i] = 1
        else :
            li_dict[i] += 1
        
    # li_dict = { key : value for key, value in li_dict.items() if value >=2 }
    result = dict()
    for key, value in li_dict.items() :
        if value >= 2 :
            result[key] = value           


    return result
            

numbers = [1,2,3,2,4,2,5,3]
duplicate_counts = count_duplicates(numbers)
print(f"중복 항목:{duplicate_counts}")