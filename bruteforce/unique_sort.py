def unique_sort(lst):
  purgedList = []
  for i in sorted(lst):
    if i not in purgedList:
      purgedList.append(i)
  return purgedList
