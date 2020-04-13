from checkIfCorrect import checkifCorrect
from ipAddressInfo_class import ipAddressInfo


def main():
    data = input("Enter the ip address together with the shortened mask record (e.g. 192.168.1.1/24): ")

    if checkifCorrect(data):
        address = ipAddressInfo(data)
        address.showInfo()
        address.saveToJSON()

    input("Press any button to finish")

    
if __name__ == "__main__":
    main()
