import socket

UDP_IP = "192.168.38.102"
UDP_PORT = 5005

print UDP_IP, UDP_PORT

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((UDP_IP, UDP_PORT))

connections = []
declinedConnections = []

sendConnected = False
gameStarted = False

print "Waiting for a connection..."

while True:
     data, addr = s.recvfrom(1024)

     if len(connections) == 0:
          gameStarted = False
          
     if data == "connected":
              if gameStarted == False:
                   connections.append(addr)
                   print "Connected: ", addr
                   s.sendto("Connected!", addr)
                   for c in connections:
                           s.sendto("Connected: "+ str(len(connections)), c)
              else:
                   s.sendto("Cannot connect: Game has alreasy started", addr)

     if addr in connections:
          if data == "k":
                  gameStarted = True
          if data == "y":
                  gameStarted = False
          if data == "disconnected":
                  connections.remove(addr)
                  print "Disconnected: ", addr
                  sendConnected = True

          if data != "connected":
                     if data != "disconnected":
                             print addr, ": ", data
                     for c in connections:
                             if sendConnected == True:
                                     s.sendto("Connected: " + str(len(connections)), c)
                             s.sendto(data, c)
                     sendConnected = False
