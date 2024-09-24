#        - the pcap starts with the 3 way handshake as the first 3 packets
def findMaxBytesInFlight(pcapfile):   
    maxBytesInFlight = 0
    inFlightBytes = 0 

    packets = rdpcap(pcapfile)
    flow = readHandShake(packets)
    currAck = flow.ackNumReceived
    highestSeq = flow.startSeqNum

    seenPackets = set() 

    for packet in packets:
        if TCP in packet and isFlowEgress(packet, flow):
            seqNum = packet[TCP].seq
            payload_len = len(packet[TCP].payload)
            
            if (seqNum, payload_len) not in seenPackets:
                seenPackets.add((seqNum, payload_len))
                if seqNum + payload_len > highestSeq:
                    highestSeq = seqNum + payload_len
            
            inFlightBytes = highestSeq - currAck
            maxBytesInFlight = max(maxBytesInFlight, inFlightBytes)
        
        elif TCP in packet and not isFlowEgress(packet, flow):
            if packet[TCP].ack > currAck:
                currAck = packet[TCP].ack
                inFlightBytes = highestSeq - currAck
                maxBytesInFlight = max(maxBytesInFlight, inFlightBytes)

    return maxBytesInFlight



if __name__ == '__main__':
   # pcap is a server side capture
   maxBytesInFlight = findMaxBytesInFlight("simple-tcp-session.pcap")
   print("Max: " + str(maxBytesInFlight))
   print()

   maxBytesInFlight = findMaxBytesInFlight("out_10m_0p.pcap")
   print("Max: " + str(maxBytesInFlight))
   print()
