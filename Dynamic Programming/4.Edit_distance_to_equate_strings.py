str1, str2 = "abc", "yabd"

m, n = len(str1), len(str2)
print(m,n)

edits = [[0]*(n+1) for i in range(m+1)]

for i in range(n+1):
    edits[0][i] = i

for j in range(m+1):
    edits[j][0] = j


for i in range(1, m+1):
    for j in range(1, n+1):
        if str1[i-1] == str2[j-1]:
            edits[i][j] = edits[i-1][j-1]
        else:
            edits[i][j] = min(edits[i-1][j-1], min(edits[i-1][j], edits[i][j-1]))+1

for i in range(m+1):
    print(edits[i])

print(edits[-1][-1])