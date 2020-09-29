filename = 'demo.py'                                                                                 #0
with open(filename, 'r') as fp:                                                                      #1
    lines = fp.readlines()                                                                           #2
    maxLength = len(max(lines, key=len))                                                             #3
    lines = [line.rstrip().ljust(maxLength)+'#'+str(index)+'\n' for index, line in enumerate(lines)] #4
with open(filename[:-3]+'_new.py', 'w') as fp:                                                       #5
    fp.writelines(lines)                                                                             #6
