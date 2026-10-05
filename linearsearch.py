# Linear Search

def linearsearch(a,el):
  for i in range(len(a)):
    if a[i]==el:
       print(f'{el} is found at index {i}')
       return
  print(f'{el} is not found in array')

# linear search with return index

def linearsearch2(a,e):
  for i in range (len(a)):
    if a[i]==e:
      return i
  return -1

# linear search with return all indexes

def linearsearch_ar(a,el):
  ar=[]
  for i in range (len(a)):
    if a[i]==el:
      ar.append(i)
  return ar



a=[12,3,4,5,1,8,4,30,29,4]

linearsearch(a,1)
print(linearsearch2(a,1))

res=linearsearch_ar(a,4)
for i in res:
  print(i,end=" ")
print()
