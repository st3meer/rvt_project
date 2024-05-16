path = "saveddata/" #path to save folder
def compareCSV(filename):
    # Compare two CSV files
    # Return 0 if they are the same
    # Return new link list if they are different
    file1 = open(path + filename + ".csv", "r", encoding="utf-16") #open the files
    file2 = open(path + filename + "Old.csv", "r", encoding="utf-16")

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

def get_task_list():
    # Get the list of tasks from the config file
    file = open(path + "general.config", "r") #open the file
    tasks = [] #list for tasks
    for line in file: #read the file
        tasks.append(line) #add the tasks to the list
    return tasks #return the list of tasks

def get_task_config(taskname):
    # Get the configuration of the task
    file = open(path + taskname + ".config", "r", encoding="utf-16") #open the file
    config = [] #list for the configuration
    for line in file: #read the file
        config.append(line) #add the configuration to the list
    return config #return the list of configuration