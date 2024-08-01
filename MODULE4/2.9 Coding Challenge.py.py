# GETTING THE MEAN IN A DATA

import array as arr

def display_mean():
    print("The mean in the list is ")

def get_mean():
    n = len(dataset)
    get_sum = sum(dataset)
    mean = get_sum / n
    m = str(mean)
    print(m)

friends_usage = [9, 10, 5, 7, 5, 7, 5, 4, 3, 5]

sample_data = arr.array('i', friends_usage)
dataset = sample_data[0:10]
sample_data_list = sample_data.tolist()

print(display_mean(), get_mean())