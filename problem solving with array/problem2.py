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