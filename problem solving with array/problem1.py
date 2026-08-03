def find_pair(arr, target):
    left=0
    right=len(arr)-1
    while left<right:
        current_sum=arr[left]+ arr[right]
        if current_sum==target:
            return f"Pair found at index {left} and {right}"
        elif current_sum<target:
            left+=1
        else:
            right-=1
    return "Pair not found"
array=[1,2,3,4,5,6,7,8,9]
target=10
result=find_pair(array,target)  
print(result)
    