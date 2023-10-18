def remove_value(num, remove) :
    result = []
    for value in num :
        if value != remove :
            result.append(value)
    
    return result
        

numbers = [1,2,3,2,4,2,5,5,2,3,5,4]
value_to_remove = 2
updated_list = remove_value(numbers, value_to_remove)
print(f"제거 후 리스트:{updated_list}")