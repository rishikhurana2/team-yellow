import socket
import sys
import threading

class Network(object):

    sendType = None
    sendAzimuth = None

    portNumber = 0
    isInitialized = False
    s = None
    connection = None

    def __init__(self):
        global portNumber
        portNumber = 3341
        global isInitialized
        isInitialized = False

    class myThread (threading.Thread):
        network = None
        def __init__(self, threadID, name, counter, network):
            threading.Thread.__init__(self)
            self.threadID = threadID
            self.name = name
            self.counter = counter
            self.network = network

        def run(self):
            print ("Starting " + self.name)
            Network.startServer(self.network)
            print ("Exiting " + self.name)

    def setType(self, message):
        self.sendType = message
        #print (self.sendString)

    def setAzimuth(self, message):
        self.sendAzimuth = message
        #print (self.sendString)

    def waitForPing(self): #wait for something to be sent
        if(s != None):
            receive = s.recv(1024)
        if receive == None or receive == ' ' :
            print ("Hasn't received ping")

    def sendMessage(self, message): # send message to NTable client
        if(isInitialized !=  False):
            connection.send(message + b'\n')

    def userServer(self):
        global s

        thread1 = self.myThread(1, "Thread-1", 1, self)
        thread1.start()
        print("thread started")

    def startServer(self): #startServer

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = "localhost"
        s.bind((host, portNumber))

        global connection
        print ("in startServer")
        s.listen(5)
        #while True:

        connection, addr = s.accept()
        print ("accepted")
        global isInitialized
        isInitialized = True

        while True:
            if(self.sendType != None):

                self.sendMessage(self.sendType.encode('utf-8') + b";" + self.sendAzimuth.encode('utf-8'))
                self.sendType = None
                self.sendAzimuth = None
