class Solution:
	# @param A : list of integers
	# @return a list of integers
	def plusOne(self, A):
	    if len(A)==1 and A[0]!=9:
	        return [A[0]+1]
	    if len(A)==1 and A[0]==9:
	        return [1,0]
	    count=0
	    arr=[]
	    for i in range(len(A)):
	        if A[i]==0:
	            count+=1
	        else:
	            break
	    for i in range(count,len(A)):
	        arr.append(A[i])
	    s = int(''.join(map(str, arr)))+1
	    return [int(x) for x in str(s)]
	        
	        
