"""
@Author: Anil
@Date: 2021-10-01 10:45
@Last Modified by: Anil
@Last Modified time: 2021-10-01 11:00
@Title : To perform multiplication of given matrix and vector
"""
X = [[12,7,3],
[4 ,5,6],
[7 ,8,9]]

Y = [[1], [2], [3]]
	
result = [[0],[0],[0]]

# iterating by row of A
for i in range(len(X)):

	# iterating by column by B
	for j in range(len(Y[0])):

		# iterating by rows of B
		for k in range(len(Y)):
			result[i][j] += X[i][k] * Y[k][j]

for r in result:
	print(r)
