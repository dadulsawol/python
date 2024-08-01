def get_mean(ave):
    print("The mean of this list is ", ave)

n_num = [78, 90, 80, 89, 87, 90]
n = len(n_num)

get_sum = sum(n_num)
mean = get_sum / n 

m = str(mean)

get_mean(m)

# ARRAY AND LIST
import array as arr

friends_usage = [5, 6, 4, 5, 2, 3, 5, 8, 9, 3, 1, 7, 5, 3, 6, 5, 4, 5, 8, 9, 2]
sample_data = arr.array('i', friends_usage)
print(sample_data[0:5])

from array import * 
sample_data_array = array('i', [5, 4, 3, 2, 1])

sample_data_list = sample_data_array.tolist()
print(sample_data_list)