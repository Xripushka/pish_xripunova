#1 задание
array = [1, 2, 3, 4, 5]
shift = 2


result = array[-shift:] + array[:-shift]

#2 задание
def shift_matrix_rows(matrix, shift):
    
    return [row[-(shift % len(row)):] + row[:-(shift % len(row))] 
            for row in matrix]

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
shift = 1
result = shift_matrix_rows(matrix, shift)

print("Результат:", result)

#3 задача
array = [1, 2, 3, 4, 5, 6, 7]
block_size = 3

result = []
for i in range(0, len(array), block_size):
    block = array[i:i + block_size]
    
    if len(block) == block_size:
        result.extend(block[::-1])  
    else:
        result.extend(block)        

print("Выход:", result)

#4 задача
нет решения