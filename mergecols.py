import sys

fileNames = sys.argv[1:]
files = [ open(n, "rt") for n in fileNames ]
numberOfColumns = [ None ] * len(fileNames)
while True:
    newParts = [ ]
    foundEntries = False
    for idx in range(len(files)):
        line = files[idx].readline()
        if line:
            parts = line.strip().split(",")
            if numberOfColumns[idx] is None:
                numberOfColumns[idx] = len(parts)
            else:
                if numberOfColumns[idx] != len(parts):
                    raise Exception("Number of columns in '{}' changed".format(fileNames[idx]))
            newParts += parts
            foundEntries = True
        else:
            if numberOfColumns[idx] is None:
                raise Exception("{} does not appear to contain lines".format(fileNames[idx]))
            newParts += [ "" ] * numberOfColumns[idx]

    if not foundEntries:
        break
    sys.stdout.write(",".join(newParts) + "\n")
