#linear search

def linearSearch(values, target):
  for i in range(len(values)):
    if (values[i] == target):
     return i

  return -1


#binary search

def binarySearch(values,target):
  low = 0
  high = len(values)-1
  mid = 0

  #mid
  while low<=high:

    mid = (low+high)//2


    if values[mid]<target:
      low = mid+1

    elif values[mid]>target:
      high = mid-1

    else:
      return mid

  return -1




"""Sorts"""

#Bubble Sort

def bubbleSort(usValue):
  #sorts list of unsorted values
  done = False
  sortedCount = 0

  while not done:
    done = True
    i = 0

    while i < len(usValue) -1 - sortedCount:
      if usValue[i] > usValue[i+1]:
        swap(usValue,i,i+1)
        done = False
      i+=1
    sortedCount+=1
  print(usValue)



#merge sort

def mergeSort(values):
  if len(values)<=1:
    return values

  sortedValues = []

  mid = len(values)//2

  low = mergeSort(values[:mid])
  upper = mergeSort(values[mid:])

  while len(low)>0 and len(upper)>0:
    if low[0]<upper[0]:
      sortedValues.append(low.pop(0))
    else:
      sortedValues.append(upper.pop(0))
  if len(low)>0:
    sortedValues.extend(low)
  elif len(upper)>0:
    sortedValues.extend(upper)
  return sortedValues
  print(sortedValues)
  




#helper functions

def swap(liste,index1,index2):
  """Swap list[index1] and list[index2]"""

  if liste[index1]>liste[index2]:
    liste[index1],liste[index2] = liste[index2],liste[index1]




