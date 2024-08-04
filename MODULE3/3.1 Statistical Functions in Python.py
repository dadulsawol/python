# GETTING THE MEDIAN
import array as arr

def display_median():
    print("The median is ")

def median(nums):
    nums.sort()
    if len(nums)%2 == 0:
        return int(nums[len(nums)//2-1]+nums[len(nums)//2])/2
    else:
        return nums[len(nums)//2]

n_num = [78, 80, 79, 80, 87, 85]

print("Median: ", median(n_num))


import statistics
import array as arr


friends_usage = [5, 4, 3, 5, 2, 5, 8, 10, 8, 7, 9, 10, 5, 7, 5, 7, 5, 4, 3, 8, 4]
sample_data = arr.array('i', friends_usage)
dataset = sample_data[0:5]
sample_data_list = dataset.tolist()

mean = statistics.mean(friends_usage)
mode = statistics.mode(friends_usage)
median = statistics.median(friends_usage)
pstdev = round(statistics.pstdev(friends_usage), 2)
pvariance = round(statistics.pvariance(friends_usage), 2)
srange = (max(friends_usage)-min(friends_usage))

variance = round(statistics.variance(sample_data_list), 2)
stdev = round(statistics.stdev(sample_data_list), 2)
print("Descriptive Statistics")
print("Mean: ",mean) 
print("Median: ", median)
print("Mode: ", mode) 
print("Range: ", srange)
print("Population Variance: ",pvariance) 
print("Population Standard Deviation: ",pstdev)