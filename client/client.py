from rpcClient import RPCClient
import os.path

server = RPCClient('127.0.0.1', 8080)

server.connect()

print(server.add(5, 6))
print(server.sub(5, 6))


try:
    Platform=input("Enter Platform : ")
    fileName = input("Enter FileName: ")
    #Platform = 'Netflix'
    #fileName = 'Movie1.txt'
    if not os.path.isdir('Contents'):
        os.mkdir('Contents')
    directory = 'Contents/' + str(Platform) + '/'
    if not os.path.isdir(directory):
        os.mkdir(directory)
        print('directory created')
    file_path  = os.path.join(directory, fileName)
    fullpath = str(Platform) + str('/') + str(fileName)
    print(fullpath)
    handle=open(file_path,"a")
    content = str(server.movefile(str(Platform),str(fileName)))
    print(content)
    handle.write(content)
    handle.close()
except:
    print ('Download failed')

server.disconnect()