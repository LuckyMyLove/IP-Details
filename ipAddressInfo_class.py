import json
from functions import *

class ipAddressInfo:
    def __init__(self, data):
        self.ip, self.maskShort = data.split("/")[0], int(data.split("/")[1])

        self.ipBin = getIpBin(self.ip)
        self.ipClass = getIpClass(self.ip)
        self.maskFull, self.maskFullBin = getMask(self.maskShort)
        self.netAddress, self.netAddressBin = getNetAddress(self.ipBin, self.maskShort)
        self.broadcast, self.broadcastBin = getBroadcast(self.ipBin, self.maskFullBin)
        self.hostMin, self.hostMinBin, self.hostMax, self.hostMaxBin, self.hostAll = getHostsInfo(self.netAddress,
                                                                                                  self.broadcast)

    def showInfo(self):
        print("\nAddress class: " + self.ipClass)
        print("IP: " + self.ip + " || " + self.ipBin)
        print("Mask: " + self.maskFull + " || " + self.maskFullBin)
        print("Network Address: " + self.netAddress + " || " + self.netAddressBin)
        print("Broadcast: " + self.broadcast + " || " + self.broadcastBin)
        print("First host: " + self.hostMin + " || " + self.hostMinBin)
        print("Last host: " + self.hostMax + " || " + self.hostMaxBin)
        print("All hosts number: %i\n" % self.hostAll)


    def saveToJSON(self):
        ip_details = {
            'ip': self.ip,
            'ipBin': self.ipBin,
            'maskShort': self.maskShort,
            'maskFull': self.maskFull,
            'maskFullBin': self.maskFullBin,
            'class': self.ipClass,
            'netAddress': self.netAddress,
            'netAddressBin': self.netAddressBin,
            'broadcast': self.broadcast,
            'broadcastBin': self.broadcastBin,
            'hostMin': self.hostMin,
            'hostMinBin': self.hostMinBin,
            'hostMax': self.hostMax,
            'hostMaxBin': self.hostMaxBin,
            'hostsAll': self.hostAll
        }

        with open('ip_details.json', 'w') as json_file:
            json.dump(ip_details, json_file)




