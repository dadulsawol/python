import array as arr

def display_average():
    print("The average online buys for the past 5 weeks is ")

def average_calc():
    ###
    ave = len(average_buys)
    get_sum = sum(average_buys)

    # computation
    average = get_sum / ave
    print(average)

average_buys = [19, 27, 17, 24, 16]

#####
sample_data = arr.array('i', average_buys)
items = sample_data[0:5]
sample_data_list = sample_data.tolist()

## displaying 
display_average()
average_calc()

