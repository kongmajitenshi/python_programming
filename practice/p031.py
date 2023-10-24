data1 = [1,2,3]
print(data1[0])
print(data1[-1])
print(data1[0] + data1[-1])

data2 = [1,2,3, ['a', 'b', 'c']]
print(data2[0], type(data2[0]))
print(data2[-1], type(data2[-1]))
print(data2[-1][-1], type(data2[-1][-1]))
print(data2[-1][:2], type(data2[-1][:2]))
      
data1.append([4,5])
print(data1)

numbers = [1,2,3,4,5,10]
numbers.remove(6) # remove(n) 은 인덱스가 아니라 값에 접근하는 함수.
print(numbers)