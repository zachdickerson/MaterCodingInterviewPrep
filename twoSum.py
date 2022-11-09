arr1 = [1,3,5,6]
target1 = 8

arr2 = [4,7,2,6]
target2 = 12

arr3 = [1,3,7,9,2]
target3 = 11

arr4 = [2,7,11,15]
target4 = 9

''' 
Optimal Solution
'''
def two_sum(our_array, target):

    values = dict()

    for i, element in enumerate(our_array):
        numberToFind = target - element

        if numberToFind in values:

            return [values[numberToFind], i]
        
        values[element] = i

    return []

'''
    Brute  Force
    Time   O(n^2)
    Space  O(1)
'''
def two_sum2(nums, target):

    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


def two_sum3(nums, target):

    values = {} # constant time access

    for i, element in enumerate(nums):

        if element in values:

            return [values[element], i]

        values[target - element] = i
    
    return []


# list1 = two_sum(arr1, target1)
# print(list1)

# list2 = two_sum(arr2, target2)
# print(list2)

# list3 = two_sum(arr3, target3)
# print(list3)

list4 = two_sum2(arr4, target4)
print(list4)