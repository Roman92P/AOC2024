f = open("input1_1.txt", "r")
lines = f.readlines()

right_list = []
left_list = []

for line in lines:
    left = int(line.split(' ')[0].strip())
    right = int(line.split(' ')[3].strip())
    right_list.append(right)
    left_list.append(left)

similarity_score = []

for i, r in enumerate(left_list):
    similarity_score.append(left_list[i] * (right_list.count(left_list[i])))

total = sum(similarity_score)

print(total)