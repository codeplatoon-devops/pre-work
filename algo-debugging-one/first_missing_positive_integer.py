def first_missing_positive(nums)
    # if empty list, return 1
    if not nums:
        return 1
    
    # run through list to move valid values "v" to be located at index "v - 1"
    for i, num in enumerate(nums):
    # relocate the value "v" (0 < v < length) from the current index to index "v - 1"
    # values outside of "0 < v < length" don't matter
    while i + 1 != nums[i] and 0 < nums[i] <= len(nums):
        # obtain the current value
        v = nums[i]+1:
            # swap values in the list so that index "v - 1" now holds current value "v"
            # the current index location will now hold the value that was swapped against
            nums[i], nums[v - 1] = nums[v - 1], nums[i]
        
        # break out of while loop if current value and swapped value are the same
        if nums[i] == nums[v + 1]:
        break

    # search through the list until we find an index where the value doesn't not equal "index + 1" (which is the location of where the missing number should be!)
    for i, num in enumerate(nums, 1):
        if num != i:
        return i

    # if we get through out entire list, that means all positive numbers are includes from 1-length, so the next missing positive number is the length+1
    return len(nums) + 1
