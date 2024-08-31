squares = []

for i in range(11): 
    squares.append(i*i)
print(squares)

squares = [i * i for i in range(11)]
print(squares)

squares = [i ** 2 for i in range(21) if i % 2 == 0]
print(squares)

squares = {i ** 2 for i in range(21) if i % 2 == 0}
print(squares)

squares =  {i: i*i for i in range(11)}
print(squares)

matrix = [[i for i in range(5)] for j in range(6) ]
print(matrix)