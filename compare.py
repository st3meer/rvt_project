def compareCSV(filename):
    # Compare two CSV files
    # Return 0 if they are the same
    # Return new link list if they are different
    file1 = open(filename + ".csv", "r", encoding="utf-16") #open the files
    file2 = open(filename + "Old.csv", "r", encoding="utf-16")

    new_links = [] #list for new links

    file1_lines = file1.readlines() #read the new file
    file1_lines.pop(file1_lines.__len__() - 1)
    for row in file1_lines:
        row = row.split(';') #split the text into 2d array

    file2_lines = file2.readlines() #read the old file
    file2_lines.pop(file2_lines.__len__() - 1)
    for row in file2_lines:
        row = row.split(';') #split the text into 2d array

    if file1_lines == file2_lines: #compare the two files
        return 0 #if they are the same, return 0
    else:
        for i in file1_lines: #if they are different, get the new links
            if i not in file2_lines:
                new_links.append(i) #add the new links to the list

    return new_links #return the new links
