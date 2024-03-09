from rpcServer import RPCServer

import xmlrpc
#import xmlrpclib
from xmlrpc.server import SimpleXMLRPCServer
import sys

def add(a, b):
    return a+b

def sub(a, b):
    return a-b

def registerFiles(fileName):
    with open("metadataFile.txt", 'a') as file1:
        contentLine = str(fileName)
        file1.write(contentLine + '\n')
        return 'Registered File: ' + str(contentLine)
    

def movefile(Platform, FileName):
    fileFound = 'No'
    print('Inside movefile')
    f = open("metadataFile.txt", "r")
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        if Platform in line and FileName in line:
            fileFound = 'Yes'
            line = line.replace('\\','/')
            print(line)
            finalPath = '../contentServer/' + str(line)
            print(finalPath)
            try:
                with open(finalPath,"r") as handle:
                    resultOutput = str(handle.read())
                    print(resultOutput)
                    handle.close()
                    return resultOutput
            except:
                return 'File Not Found'
    if fileFound == 'No':
        return 'File Not Found'
        ## Get the Content from Another Server   
        


    # try:
    #     path = '../contentServer/Contents/'
    #     path += str(Platform) + '/' + str(FileName)
    #     print(path)
    #     with open(path,"r") as handle:
    #         resultOutput = str(handle.read())
    #         return resultOutput
    #         handle.close()
    # except:
    #     return 'error'


server = RPCServer()

server.registerMethod(add)
server.registerMethod(sub)
server.registerMethod(registerFiles)
server.registerMethod(movefile)

server.run()