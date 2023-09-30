disks = [[4, 6, 7], [1, 2, 3], [4, 5, 6], [10, 12, 32]]
disks = [ [2,2,1], [2,1,2], [3,2,3], [2,3,4], [4,4,5], [2,2,8] ]
sequences = [0 for disk in disks]
max_height = 0
max_heights = [disk[2] for disk in disks]

for i in range(1, len(disks)):
    for j in range(i):
        if disks[j][0] < disks[i][0] and disks[j][1] < disks[i][1]:
            print("Comparing other disk : {} and current disk : {}".format(disks[j], disks[i]))
            max_heights[i] = max(max_heights[i], max_heights[j] + disks[i][2])
            sequences[i] = j
print(max_heights)
print(sequences)
