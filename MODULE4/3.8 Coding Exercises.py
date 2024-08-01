import numpy as np
import scipy as sp
import statistics as stat
import array as arr

random = [103, 151, 176, 188, 146, 184, 175, 112, 115, 163]

def display():
    print("Descriptive Statistics using Numpy")
    print("Mean: ",mean) 
    print("Median: ", median)
    print("Mode: ", mode) 
    print("Range: ", srange)
    print("Population Variance: ", variance) 
    print("Population Standard Deviation: ",pstdev)
    print("Sample standard deviation: ", sdeviation)

mean = np.mean(random)
median = np.median(random)
variance = round(np.var(random),2)
pstdev = round(np.std(random), 2)

srange = np.ptp(random)
mode = stat.mode(random)

sample_data = arr.array('i', random)
dataset = sample_data[0:9]
sample_data_list = dataset.tolist()

variance = round(np.var(sample_data_list, ddof=1),2)
sdeviation = round(np.std(sample_data_list, ddof=1))

display()