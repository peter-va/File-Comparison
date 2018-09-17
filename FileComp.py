import os

def filePairs(dtree, nBytes):
    '''main function for ProblemB'''
    masterlist = [] #set up lists for all files and returned pairs
    returnlist = []
    os.path.walk(dtree, getfiles, masterlist)
    for i in masterlist:
        if os.path.isfile(i) is False: #avoid hidden dirs, counted as files in path.walk
            continue
        file1 = open(i, "r")
        string1 = file1.read(nBytes)
        for j in masterlist:
            if i != j: #avoid checking file agains itself
                if os.path.isfile(j) is False: #avoiding hidden dirs again
                    continue
                file2 = open(j, "r")
                string2 = file2.read(nBytes)
                if string1 == string2 and (j, i) not in returnlist: #no repeating same files
                    returnlist.append((i, j))
                file2.close()
        file1.close()
    return returnlist

def getfiles(arg, directory, filelist): #function call from os.path.walk
    '''helper function for getting file list of dtree'''
    for i in filelist:
        arg.append(directory+'/'+i) #get full path of file (dir + file)
