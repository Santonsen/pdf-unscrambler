import sys
import os

pdf = str(sys.argv[1])
print(pdf)
cmdString = " ".join(["mutool show",pdf,"trailer/Root/Pages/Count"])
stream = os.popen(cmdString)
output = stream.read()

t = int(output)

left = []
right = []

for i in range(t):
    if(i % 4 == 0):
        left.insert(0,str(i+1))
    elif(i % 4 == 1):
        right.append(str(i+1))
    elif(i % 4 == 2):
        right.append(str(i+1))
    else:
        left.insert(0,str(i+1))

totalList = left + right
joinedString = ",".join(totalList)

outputFile = pdf.replace(".pdf","Output.pdf")
mutoolString = " ".join(["mutool merge -o", outputFile, pdf, joinedString])
print(mutoolString)
os.system(mutoolString)
