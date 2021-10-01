"""
@Author: Anil
@Date: 2021-10-01 10:25
@Last Modified by: Anil
@Last Modified time: 2021-10-01 10:40
@Title : To perform scalar multiplication of matrix and a number
"""
N = 3

def scalarProductMat( mat, k):

	# scalar element is multiplied
	# by the matrix
	for i in range( N):
		for j in range( N):
			mat[i][j] = mat[i][j] * k	


if __name__ == "__main__":
	
	mat = [[ 12, 7, 3 ],
		[ 4, 5, 6 ],
		[ 7, 8, 9 ]]
	k = 9

	scalarProductMat(mat, k)

	# to display the resultant matrix
	print("Scalar Product Matrix is : ")
	for i in range(N):
		for j in range(N):
			print(mat[i][j], end = " ")
		print()


