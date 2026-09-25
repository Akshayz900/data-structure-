a=[1,2,3,4,5]
b=10
def  traversal(ar):
  print('[',end="")
  for i in range(len(ar)-1):
    print(ar[i],end=', ')
  print(ar[-1],end=']')
print(b)
print(a)
traversal(a)


a=[1,2,3,4,5]
b=10
def insert(ar,e1,ind):
  ar2=[0 for i in range(len(ar)+1)]
  for i in range (ind):
    ar2[i]=ar[i]
  for i in range (ind,len(ar)):
    ar2[i+1]=ar[i]
  ar2[ind]=e1
  print(ar2)
  print()
insert(a,10,3)

a=[1,2,3,4,5]
b=10

def delete(ar,ind):
  ar2=[0 for i in range(len(ar)-1)]
  for i in range (ind):
    ar2[i]=ar[i]
  for i in range (ind+1,len(ar)):
    ar2[i-1]=ar[i]
  print(ar2)
  print()
delete(a,2)


a=[1,2,3,4,5]
b=10
def search(a,e1):
  for i in range(len(a)):
    if a[i]==e1:
      print(f'element {e1} is found at index {i}')
      return
  print(f'element {e1}not found')
search(a,3)

#array rotation
a=[12,43,65,33,22]
k=2
def leftshift(ar,key):
    print(ar)
    ar2=[0 for _ in range(len(ar))]
    ind=0
    for i in range(key,len(ar)):
        ar2[ind]=ar[i]
        ind+=1
    for i in range(key):
        ar2[ind]=ar[i]
        ind+=1
    print(ar2)

leftshift(a,k)

a=[1,2,3,4,5,6]
k=2
def rightshift(ar,key):
    print(ar)
    ar2=[0 for _ in range(len(ar))]
    ind=0
    for i in range(len(ar)-key,len(ar)):
        ar2[ind]=ar[i]
        ind+=1
    for i in range(len(ar)-key):
        ar2[ind]=ar[i]
        ind+=1
    print(ar2)

rightshift(a,k)