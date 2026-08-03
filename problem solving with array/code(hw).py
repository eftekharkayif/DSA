#Problem 01 : Two-pointer technique to find a pair in a sorted array that sums to a target value

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


# Problem 02 : Sliding window technique to find the maximum sum of k consecutive elements in an array

def max_icecream_scoops(bowls,k):
    current_scoops=sum(bowls[:k])
    max_scoops=current_scoops
    for i in range(k,len(bowls)):
        current_scoops+=bowls[i]-bowls[i-k]
        if current_scoops>max_scoops:
            max_scoops=current_scoops
    return max_scoops
bowls=[1,2,3,4,5,6,7,8,9]
k=3
print(max_icecream_scoops(bowls,k))