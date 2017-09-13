class Solution:
	# @param A : list of integers
	# @param B : list of integers
	# @return an integer
	def coverPoints(self, A, B):
	    arr=[]
	    sum=0
	    for i in range(0,len(A)):
	        arr.append([A[i],B[i]])
	    for i in range(1,len(arr)):
	        dif_x=arr[i][0]-arr[i-1][0]
	        dif_y=arr[i][1]-arr[i-1][1]
	        dif=max(abs(dif_x),abs(dif_y))
	        sum=sum+abs(dif)
	    return sum     
