inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')

lines = inFile.readlines()
lines.sort()

for line in lines:
    lst = list(map(str, line.split()))
    print(f'{lst[0]} {lst[1]} {lst[3]}', file=outFile)

inFile.close()
outFile.close()
