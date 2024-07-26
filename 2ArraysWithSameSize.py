''' Given 2 arrays A and B,of equal size n,the task is to find the minimum value
of A[0]*B[0]+A[1]*B[1]+...+A[n-1]*B[n-1].shuffling of elements of arrays A and B
is allowed.
I/P: A[]={3,1,1} and B[]={6,5,4}
O/P: 23'''
A=list(map(int,input().split()))
B=list(map(int,input().split()))
A.sort()
B=sorted(B)[::-1]
total=0
for i in range(len(A)):
    total+=A[i]*B[i]
print(total)
