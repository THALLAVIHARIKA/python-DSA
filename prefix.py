def calprifix(a):
  sum=a[0]
  res=[0 for i in range(len(a))]
  res[0]=sum
  for i in range(1,len(a)):
    sum+=a[i]
    res[i]=sum
  return res    
def rangesum1(a,s,e):
  sum=0
  if s>1 and e<len(a):
    for i in range(s,e+1):
      sum+=a[i]
    return sum

def rangesum(a,s,e):
  return prefix[e]-prefix[s-1]
    

a=[1,2,3,4,5,6,7,8,9]
prefix=calprifix(a)
print(prefix)
print(rangesum1(a,3,8))
print(rangesum(a,3,6))