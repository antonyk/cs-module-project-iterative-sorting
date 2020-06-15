# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):

# Note: Original baseline code looked wrong.
# What is the implementation if we use it?

    if len(arr) > 1:
        # loop through n-1 elements
        # for i in range(len(arr)):
        for i in range(0, len(arr)):
            # TO-DO: find next smallest element
            # (hint, can do in 3 loc)
            # Your code here
            cur_index = i
            smallest_index = cur_index
            for x in range(cur_index, len(arr)):
                if  arr[x] < arr[smallest_index]:
                    smallest_index = x

            # TO-DO: swap
            # Your code here
            if smallest_index != cur_index:
                arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Two specific optimizations to improve on the O(n^2) worst case:
    # 1. Stop sorting if no changes were made in a single iteration
    # 2. Shorten length of each iteration because it will always bubble the biggest to the right
    if len(arr) > 1:
        sort_start = 1
        end_offset = 0
        changed = True
        while end_offset < (len(arr) - sort_start) and changed:
            changed = False
            for i in range(sort_start, len(arr)-end_offset):
                if arr[i] < arr[i-1]:
                    arr[i], arr[i-1] = arr[i-1], arr[i] # swaps
                    changed = True

            end_offset += 1 # shorten array to be sorted
            
    # Your code here


    return arr

'''
STRETCH: implement the Count Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here


    return arr




