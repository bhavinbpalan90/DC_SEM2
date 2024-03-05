from rpcContentServer import RPCContentServer
import pathlib

server = RPCContentServer('127.0.0.1', 8080)

server.connect()

Content = pathlib.Path('Contents')

for files in Content.rglob('*.*'):
    print(files)
    print(server.registerFiles(str(files)))


server.disconnect()