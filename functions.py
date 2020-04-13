def getIpBin(ip):
    ipBin = ''

    for index, octet in enumerate(ip.split("."), 1):
        ipBin += str(format(int(octet), '08b'))
        if index != 4: ipBin += "."

    return ipBin


def getIpClass(ip):
    octet = ip.split(".")

    if 1 <= int(octet[0]) < 128:
        return 'A'

    elif 128 <= int(octet[0]) < 192:
        return 'B'

    elif 192 <= int(octet[0]) < 224:
        return 'C'

    elif 224 <= int(octet[0]) < 240:
        return 'D'

    elif 240 <= int(octet[0]) <= 255:
        return 'E'


def getMask(maskShort):
    maskFull, maskFullBin = '', ''

    for i in range(1, 33):
        maskFullBin += "1" if i <= int(maskShort) else "0"
        if i % 8 == 0 and i != 32: maskFullBin += "."

    for index, octet in enumerate(maskFullBin.split("."), 1):
        maskFull += str(int(octet, 2))
        if index != 4:  maskFull += "."

    return  maskFull, maskFullBin


def getNetAddress(ip, mask):
    ip = ip.replace('.', '')
    netAddress, netAddressBin = '', ''

    for i in range(1, 33):
        netAddressBin += ip[i-1] if i <= int(mask) else "0"
        if i % 8 == 0 and i != 32: netAddressBin += "."

    for index, octet in enumerate(netAddressBin.split("."), 1):
        netAddress += str(int(octet, 2))
        if index != 4:  netAddress += "."

    return netAddress, netAddressBin


def getBroadcast(ip, mask):
    ip, mask = ip.replace('.', ''), mask.replace('.', '')
    broadcast, broadcastBin = '', ''

    for i in range(1, 33):
        broadcastBin += ip[i - 1] if mask[i-1] == '1' else "1"
        if i % 8 == 0 and i != 32: broadcastBin += "."

    for index, octet in enumerate(broadcastBin.split("."), 1):
        broadcast += str(int(octet, 2))
        if index != 4:  broadcast += "."

    return broadcast, broadcastBin


def getHostsInfo(netAddress, broadcast):
    hostMin, hostMinBin, hostMax, hostMaxBin = '', '', '', ''
    hostAll = 0

    for index, octet in enumerate(netAddress.split("."), 1):
        if index == 4:
            hostMin += str(int(octet)+1)
            hostMinBin += str(format(int(octet)+1, '08b'))
            break
        hostMin += octet + "."
        hostMinBin += str(format(int(octet), '08b')) + "."


    for index, octet in enumerate(broadcast.split("."), 1):
        if index == 4:
            hostMax += str(int(octet)-1)
            hostMaxBin += str(format(int(octet)-1, '08b'))
            break
        hostMax += octet + "."
        hostMaxBin += str(format(int(octet), '08b')) + "."


    for index, (octetMin, octetMax) in enumerate(zip(hostMin.split("."), hostMax.split(".")), 1):
        if index != 4:
            hostAll += 256 * (int(octetMax) - int(octetMin))

        else:
            hostAll += int(octetMax) - int(octetMin)+1
            break


    return hostMin, hostMinBin, hostMax, hostMaxBin, hostAll