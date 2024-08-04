import numpy as np
import array as arr 
from scipy import stats

f_usage = [5, 4, 3, 5, 2, 5, 8, 10, 8, 7, 9, 10, 5, 7, 5, 7, 5, 4, 3, 8, 4]

def display_usage():
    print("Descriptive Statistics")
    print("Mean: ",mean) 
    print("Median: ", median)
    print("Mode: ", mode) 
    print("Range: ", srange)
    print("Population Variance: ", variance) 
    print("Population Standard Deviation: ",pstdev)
    print("Sample standard deviation: ", sdeviation)

mean = np.mean(f_usage)
median = np.median(f_usage)
variance = round(np.var(f_usage),2)
pstdev = round(np.std(f_usage),2)

srange = np.ptp(f_usage)
mode = stats.mode(f_usage)

sample_data = arr.array('i', f_usage)
dataset = sample_data[0:5]
sample_data_list = dataset.tolist()

variance = round(np.var(sample_data_list, ddof=1),2)
sdeviation = round(np.std(sample_data_list, ddof=1))

display_usage()