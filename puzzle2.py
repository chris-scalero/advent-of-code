depths_file = open('adventofcode_depths.txt', 'r')
depths = depths_file.readlines()

# print(depths)
# print(int(depths[0:3]))

formatted_depths = []
for depth in depths:
    formatted_depths.append(int(depth))

# print(formatted_depths[0:3])
"""
len(depths)-3
start_idx
end_idx
sum[start_idx:end_idx]
start_idx, end_idx +=1
previous_sum
current_sum
current_sum > previous_sum
occurrences += 1
print(occurrences)
"""
start_idx = 0
end_idx = 3
occurrences = 0
for depth in range(0,len(formatted_depths)-2):

    previous_sum = sum(formatted_depths[start_idx:end_idx])
    current_sum = sum(formatted_depths[start_idx+1:end_idx+1])

    if current_sum > previous_sum:
        occurrences += 1

    start_idx += 1
    end_idx += 1


print(occurrences)