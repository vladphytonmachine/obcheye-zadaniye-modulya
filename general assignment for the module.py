grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
A=list(students)
B = sorted ( A )
b = ((sum (grades [0] ) ) / (len (grades [0] ) ) )
c = ((sum (grades [1] ) ) / (len (grades [1] ) ) )
e = ((sum (grades [2] ) ) / (len (grades [2] ) ) )
d = ((sum (grades [3] ) ) / (len (grades [3] ) ) )
f = ((sum (grades [4] ) ) / (len (grades [4] ) ) )
result = { B [0] : b , B [1] : c , B [2] : e , B [3] : d , B [4 ] : f }
print ( result )