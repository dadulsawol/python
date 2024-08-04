import statistics as stat
import array as arr


final_scores = [89, 90 ,91, 90, 85, 91, 88, 80, 77, 81, 
                76, 85, 87, 88, 83, 95, 88, 82, 85, 84]
# sample_data = arr.array('i', final_scores)
# dataset = sample_data[0:19]
# sample_data_list = dataset.tolist()

mean = stat.mean(final_scores)
mode = stat.mode(final_scores)
median = stat.median(final_scores)

# mean = stat.mean(dataset)
# mode = stat.mode(dataset)
# median = stat.median(dataset)

print("Central Tendency")
print("Mean: ", mean)
print("Mode: ", mode)
print("Median: ", median)