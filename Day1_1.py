f = open("input1_1.txt", "r")
lines = f.readlines()

right_list = []
left_list = []

for line in lines:
    left = int(line.split(' ')[0].strip())
    right = int(line.split(' ')[3].strip())
    right_list.append(right)
    left_list.append(left)

right_list.sort()
left_list.sort()

distances = []

for i, line in enumerate(lines):
    if right_list[i] > left_list[i]:
        distances.append(right_list[i] - left_list[i])
    if right_list[i] < left_list[i]:
        distances.append(left_list[i] - right_list[i])

result = sum(distances)

print(result)