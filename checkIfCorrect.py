import re


def checkifCorrect(data):
    data = data.strip()

    if re.search(r"[\d.]+/[\d]+$", data):
        ip, mask = data.split("/")[0], data.split("/")[1]

        if 4 != len(ip.split(".")):
            print("An IP address does not only consist of 4 octets.\n")
            return False

        for index, octet in enumerate(ip.split("."), 1):
            if int(octet) < 0 or int(octet) > 255:
                print("Octet %i is out of range.\n" % index)
                return False

        if int(mask) < 0 or int(mask) > 32:
            print("The specified abbreviated mask record is not between 0 and 32.\n")
            return False

        return True

    else:
        print("The address provided does not only contain numbers, periods, and a slash.\n")
        return False
