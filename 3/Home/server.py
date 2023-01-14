import socket

HEADER = 16
PORT =  5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = 'End'

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(ADDR)

server.listen()
print('Server is listening')
conn, addr = server.accept()
connected = True

while connected:
  msg_length = conn.recv(HEADER).decode(FORMAT)
  if msg_length:
    msg_length = int(msg_length)
    msg = conn.recv(msg_length).decode(FORMAT)
    if msg == DISCONNECT_MESSAGE:
      connected = False
      conn.send('Goodbye'.encode(FORMAT))
    else:
      salary = 0
      msg = int(msg)
      if msg<=40:
        salary = msg*200
      else:
        salary = 40*200+(msg-40)*300+8000
      print(f'Salary = {salary}')
      conn.send(f'Salary = {salary}'.encode(FORMAT))
  
conn.close()