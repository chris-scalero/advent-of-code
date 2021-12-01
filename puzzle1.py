depths_file = open('adventofcode_depths.txt', 'r')
depths = depths_file.readlines()

measurement_change = []
counter = 0
occurrences = 0
for depth in depths:

	if counter == 0:
		measurement_change.append("(n/a) - no previous measurement")

	else:

		previous_depth = int(depths[counter-1])
		current_depth = int(depths[counter])

		if current_depth > previous_depth:
			measurement_change.append("increased")
			occurrences += 1
		elif current_depth < previous_depth:
			measurement_change.append("decreased")
		else:
			measurement_change.append("no change")

	counter += 1


# occurrences = measurement_change.count("increased")
print(occurrences)