import datetime
def editDistanceWordDynamic(x, y):
    matrix = []

    xWords = x.split()
    yWords = y.split()
    
    # Make |x| by |y| matrix
    for i in range(len(xWords) + 1):
        matrix.append([0]* (len(yWords) +1))

    for i in range(len(xWords)+1):
        matrix[i][0] = i

    for i in range(len(yWords)+1):
        matrix[0][i] = i
        
        
    for i in range(1, len(xWords) + 1):
        for j in range(1, len(yWords) + 1):
            distanceHor = matrix[i][j-1] + 1
            distanceVer = matrix[i-1][j] + 1
            # Discrete Metric
            if xWords[i-1] == yWords[j-1]:
                distanceDia = matrix[i-1][j-1]
            else:
                distanceDia = matrix[i-1][j-1] + 1
            matrix[i][j] = min(distanceHor, distanceVer, distanceDia)
    return matrix[-1][-1]

with open('MobyDick.txt', 'r') as myfile:
    mobyDick=myfile.read().replace('\n', '')
    
with open('PrideAndPrejudice.txt', 'r') as myfile:
    prideAndPrejudice=myfile.read().replace('\n', '')

print("The number of words in Moby Dick:\t\t", len(mobyDick.split()))
print("The number of words in Pride and Prejudice:\t", len(prideAndPrejudice.split()))
print("Entries in matrix:\t\t\t\t", len(mobyDick.split()) * len(prideAndPrejudice.split()))

before = datetime.datetime.now()
plagiarism = editDistanceWordDynamic(mobyDick, prideAndPrejudice)

after = datetime.datetime.now()

print("Time taken: ", after-before)
print("Difference: ", plagiarism)