def maxWater(arr, n) :
    res = 0
    for i in range(1, n - 1) :
        left = arr[i]
        for j in range(i) :
            left = max(left, arr[j])
        right = arr[i]
        for j in range(i + 1 , n) :
            right = max(right, arr[j])
        res = res + (min(left, right) - arr[i])
 
    return res
if __name__ == "__main__" :
    print("Enter the number of blocks :")
    n=int(input())
    print("Enter",n,"blocks heights :")
    arr=[int(a) for a in input().split()]
    print("The amount of water being trapped :",maxWater(arr, n))