import os

def getTasks(name):
    r = os.popen('tasklist /v').read().strip().split('\n')
    print ('# of tasks is %s' % (len(r)))
    #print(r)
    for i in range(len(r)):
        if name in r[i]:
            try:
                os.system("wmic process where name='taskmgr.exe' delete")
                return r[i]
            except:
                pass

if __name__ == '__main__':
    '''
    This code checks tasklist, and will print the status of a code
    '''

    imgName = 'task'

    notResponding = 'Not Responding'

    r = getTasks(imgName)