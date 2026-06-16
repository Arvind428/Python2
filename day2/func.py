#Insertion sort
#arr == [5 4 2 1 6 3] == [5 5 2 1 6 3]===[4 5 2 1 6 3] - i=1

#arr =  [4 5 5 1 6 3] == [4 4 5 1 6 3]===[2 4 5 1 6 3] - i=2

#arr =  [2 4 5 5 6 3] == [2 4 4 5 6 3]===[1 2 4 5 6 3] - i=3

#arr =  [1 2 4 5 6 3]                                  - i=4

#arr =  [1 2 4 5 6 6] == [1 2 4 5 5 6]===[1 2 4 4 5 6] == [1 2 3 4 5 6]

def insertion_sort(arr):
    n = len(arr)#6
    for i in range(1,n): #1,6 == i=1,2,3,4,5
        key = arr[i] #3
        j = i-1 #j=0 #4

        while j>=0 and arr[j]>key: #arr[1]=2>3
            arr[j+1] = arr[j] #arr[3]=arr[2] #5=4
            j-=1 #j=-1 #1
            
        arr[j+1]=key #arr[1+1]=arr[2]=3
    return arr

n = list(map(int,input().split()))
print(insertion_sort(n))



#inserion sort---
"""
1. consider 1st ele as sorted

2. 2nd ele = key

3. compare key ele with elements before it

4. insert if key<prev ele, shift left

5. repeat

"""



