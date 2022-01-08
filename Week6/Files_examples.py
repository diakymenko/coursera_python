inFile = open('input.txt', 'r', encoding='utf8') #opens file to read
outFile = open('output.txt', 'w', encoding='utf8') #opens file where to write
lines = inFile.readlines() #variable containing all lines of the file
for line in lines:
    print(line[-2::-1], file=outFile) # reverses each line and writes to file

# or iterate through lines
    # for line in inFile:
    # print(line[-2::-1], file=outFile)

inFile.close() #closes file (each file should be closed after opening it)
outFile.close()

