a=[12,2,34,33,10,5]
k=3
def maxsubArray(a,k):
  sum=0
  for i in range(k):
    sum+=a[i]
  max=sum
  for i in range(k,len(a)):
    sum=sum+a[i]-a[i-k]
    if(sum>max):
     max=sum
  print(max)

maxsubArray(a, k)


a=[12,2,34,33,10,5]
k=3
def minsubArray(a,k):
  sum=0
  for i in range(k):
    sum+=a[i]
  min=sum
  for i in range(k,len(a)):
    sum=sum+a[i]-a[i-k]
    if(sum<min):
     min=sum
  print(min)

minsubArray(a, k)

n=int(input())
a=[int(input()) for i in range(n)]
def sumofarray(a):
  sum=0
  for i in a:
    sum+=i
  print(sum)
sumofarray(a)


n=int(input())
a=list(map(int,input().split(' ')))[:n]
def reverseArray(a):
  if len(a)<=0:
    print("invalid size. the munber of elements")
  else:
    for i in range(len(a)-1,-1,-1):
      print(a[i],end=" ")

reverseArray(a)