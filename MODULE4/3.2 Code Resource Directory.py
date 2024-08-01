# MEAN CODE 
 
def get_mean(ave):
    print("The mean of this list is ", ave)

n_num = [78, 80, 79, 80, 87, 85]
n = len(n_num)

get_sum = sum(n_num)
mean = get_sum / n

m = str(mean)

get_mean(m)

# MEDIAN CODE

def median(nums):
    nums.sort()
    if len(nums)%2 == 0:
        return int(nums[len(nums)//2-1]+nums[len(nums)//2])/2
    else:
        return nums[len(nums)//2]
    
n_nums = [78, 80, 79, 80, 87, 85]
print("Median: ", median(n_nums))