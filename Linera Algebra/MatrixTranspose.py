"""
@Author: Anil
@Date: 2021-10-01 10:45
@Last Modified by: Anil
@Last Modified time: 2021-10-01 11:00
@Title : To find transpose matrix
"""
M = 3
N = 3
def transpose(Y, B):

	for i in range(N):
		for j in range(M):
			B[i][j] = Y[j][i]
Y = [[5,8,1],
[6,7,3],
[4,5,9]]

# To store result
B = [[0 for x in range(M)] for y in range(N)]

transpose(Y, B)

print("Result matrix is")
for i in range(N):
	for j in range(M):
		print(B[i][j], " ", end='')
	print()	
