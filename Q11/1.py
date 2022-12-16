def merge(left, right):
    # create an empty list to store the sorted result
    result = []
    
    # set up two pointers to keep track of the current position in each of the input lists
    left_ptr = 0
    right_ptr = 0
    
    # while there are still elements remaining in both input lists
    while left_ptr < len(left) and right_ptr < len(right):
        # if the element at the current left pointer is smaller than the element at the current right pointer
        if left[left_ptr] < right[right_ptr]:
            # append the left element to the result and advance the left pointer
            result.append(left[left_ptr])
            left_ptr += 1
        # if the element at the current right pointer is smaller than the element at the current left pointer
        else:
            # append the right element to the result and advance the right pointer
            result.append(right[right_ptr])
            right_ptr += 1
    
    # after one of the input lists has been completely traversed, append the remaining elements from the other list to the result
    result += left[left_ptr:]
    result += right[right_ptr:]
    
    # return the sorted result
    return result

def msort(xs):
    if len(xs) <= 1:
        return xs
    
    # divide the list into two smaller lists of (approximately) half the length
    mid = len(xs) // 2
    left = xs[:mid]
    right = xs[mid:]
    
    # recursively sort each of two halves
    left = msort(left)
    right = msort(right)
    
    # merge the two sorted results into a single list using the function merge()
    return merge(left, right)

print(msort([3, 2, 1, 4]))
