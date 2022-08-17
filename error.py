def printError(error, line=None, start_index=None):
    if(line!=None and start_index!=None):
        print('\nSemantic Error: ' + error + ' (at line ' + str(line) + ':' + str(start_index) + ')\n')
    elif(line!=None):
        print('\nSemantic Error: ' + error + ' (at line ' + str(line) + ')\n')
    else:
        print('\nSemantic Error: ' + error + '\n')