import sys


def check_partition(half, n, arr):
    """
    Function to check if the list is partitionable

    This is achieved with the help of nested loops

    Each element in the list is added with remaining elements one by one to see if the sum is equal to the param 'half'

    :param half: sum of all integers in the list divided by 2
    :param n: length of the list
    :param arr: the list to be partitioned
    :return: True is list can be partitioned
    """
    # outer loop: n times
    for i in range(n - 1, -1, -1):
        count = 0
        # check if half is greater than the element; if yes add the element to count
        if (arr[i]) <= half:
            count += arr[i]
            # return true if count is equal to half
            if count == half:
                return True
            # inner loop: i-1 times
            for j in range(i - 1, -1, -1):
                # check if half is greater than count + element; if yes added the element to existing count
                if (count + arr[j]) <= half:
                    count += arr[j]
                    # return true if count is equal to half
                    if count == half:
                        return True
    return False


try:
    # fetch list from user
    arr = [int(x) for x in input("Enter list of integers separated by comma(ex-1,2,3):").split(",")]
except:
    print("INVALID INPUT")
    sys.exit()

# find sum of the given list
sum = int(sum(arr))

# check if the sum can be divided into two equal halves AND check is the list is partitionable
# using the in-built function sorted() to sort the array
if sum % 2 == 0 and check_partition((sum / 2), len(arr), sorted(arr)):
    print("Given list", arr, " is partitionable")
else:
    print("Given list", arr, " is NOT partitionable")
