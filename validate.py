import glob
count = 0
aCount = 0
bCount = 0
cCount = 0
for xml in glob.glob('./NewDataset/valid/labels/*.txt'):
    # Read the xml file
    with open(xml, 'r') as f:
        txt = f.read()
        count += 1
        # check first char in each line
        for line in txt.splitlines():
            if line[0] == '0':
                aCount += 1
            if line[0] == '1':
                bCount += 1
            if line[0] == '2':
                cCount += 1
print(aCount)
print(bCount)
print(cCount)
print(count)


