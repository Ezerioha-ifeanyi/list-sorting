#solution sorting
#this method of sorting sorts a given list without having to swap index(s) multiple times

def sort(nums):
   

    for i in range(len(nums) - 1):
        minpos = i
        for j in range(i,len(nums)):
            if nums[minpos] > nums[j]:
                minpos = j
        temp = nums[i]
        nums[i] = nums[minpos]
        nums[minpos] = temp
        print(nums) #this prints the pattern it takes for solution sorting to complete



nums = [10, 2, 8, 5, 1, 3]

sort(nums)

print(nums)

