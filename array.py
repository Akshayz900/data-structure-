def linearsearch(a,e1):
  for i in range(len(a)):
    if a[i]==e1:
      print(i)
      return
print('no element found')
def occurence(a,e1):
  ar=[]
  for i in range(len(a)):
    if a[i]==e1:
      ar.append(i)
  if len(ar)>0:
    print(ar)
  else:
    print('element not found')
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