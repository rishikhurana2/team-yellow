from Network import Network

import sys

network = Network()
network.userServer()

count = 1

while True:
    network.setType(str(count))
    network.setAzimuth(str(count + 20.01))
    count += 1
    if count == 400:
        count = 0
