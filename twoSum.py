arr1 = [1,3,5,6]
target1 = 8

arr2 = [4,7,2,6]
target2 = 12

arr3 = [1,3,7,9,2]
target3 = 11


def two_sum(our_array, target):

    values = dict()

    for i, element in enumerate(our_array):
        numberToFind = target - element

        if numberToFind in values:

            return [values[numberToFind], i]
        
        values[element] = i

    return []

list1 = two_sum(arr1, target1)
print(list1)

list2 = two_sum(arr2, target2)
print(list2)

list3 = two_sum(arr3, target3)
print(list3)