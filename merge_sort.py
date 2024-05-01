def merge_sort(arr):
  if len(arr) <=1 :
    return arr 
  
  mid = len(arr)//2
  leftArr = arr[:mid]
  rightArr = arr[mid:]
  
  leftArr = merge_sort(leftArr)
  rightArr = merge_sort(rightArr)
  
  return merge(leftArr,rightArr)

def merge(leftArr,rightArr):
  temp = []
  left = right = 0
  
  while left < len(leftArr) and right < len(rightArr):
    if(leftArr[left] < rightArr[right]):
      temp.append(leftArr[left])
      left +=1
    else:
      temp.append(rightArr[right])
      right+=1
  
  while left < len(leftArr):
    temp.append(leftArr[left])
    left +=1
    
  while right < len(rightArr):
    temp.append(rightArr[right])
    right+=1
    
  
  return temp
  
# Example usage:
arr = [10, 19, 11, 4, 61, 13,2,8,3]
sorted_arr = merge_sort(arr)
print(sorted_arr)
