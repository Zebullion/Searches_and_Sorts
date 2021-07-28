from classicAlgorithms import linearSearch, binarySearch, bubbleSort, mergeSort

def main():
  values = [0, 2, 4, 7, 9, 23, 24, 36, 60, 62]
  usValues =  [7, 23, 3, 24, 62, 9, 36, 60, 4, 0]

  #search target
  target = 24

#linear search
  print(f' {target} is at index {linearSearch(values, target)}.')
#binary search
  print(f'{target} is at index {binarySearch(values, target)}.' )
#bubblesort
  print(f'{bubbleSort(usValues)}')
#mergeSort
  print(mergeSort(usValues))



main()