"""
@Author: Anil
@Date: 2021-10-01 10:45
@Last Modified by: Anil
@Last Modified time: 2021-10-01 11:00
@Title : To multiply matrices
"""
X = [[12,7,3],
[4 ,5,6],
[7 ,8,9]]
Y = [[5,8,1],
[6,7,3],
[4,5,9]]
	
result = [[0, 0, 0],
		[0, 0, 0],
		[0, 0, 0]]

# iterating by row of X
for i in range(len(X)):

	# iterating by column by Y
	for j in range(len(Y[0])):

		# iterating by rows of Y
		for k in range(len(Y)):
			result[i][j] += X[i][k] * Y[k][j]

for r in result:
	print(r)
