#!/usr/bin/env python
# coding: utf-8

# # In this lab, we will learn to use a python packet manipulation library to modity Ethernet frames.
# 
# # Scapy
# 
# Scapy (https://scapy.net/) is a python library that enables manipulating packets.  Recall that network communication is more than just the ability to send 1s and 0s. We need structure so that both sides of the communication can understand each other.  In Ethernet, this was: 
# 
# \[ dst \]\[ src \]\[ type \]\[ payload \]\[ FCS \]
# 
# This naturally can translate to a data structure in a programming language like Python.  With Scapy, you can read packets from a file, read live traffic from the network interface, or generate packets from scratch.  
# 
# For a full tutorial, you can visit the scapy website.  Here, we'll go through just enough to complete this lab.
# 
# Useful cheat sheet for scapy:
# https://wiki.sans.blue/Tools/pdfs/ScapyCheatSheet_v0.2.pdf
# 

# First, you need to import the library.  We'll just import everything.  Then, we'll read in a trace of packets from a file.

# In[ ]:


from scapy.all import *

pkts = rdpcap("intro-wireshark-trace1.pcap")


# pkts is an array of the Packet data structure.  

# In[ ]:


pkt = pkts[1]

# Do checks on what types are in the packet
eth = Ether in pkt
print(eth)

# You can get the name of the layers in the packet (requesting a specific one)
layer = pkt.getlayer(0)
print(layer)

# or, there's a variable within the pkt structure indicating the name of the type
exp = pkt.name
print (exp)

# You can list all the available protocols - won't, since it's large
#ls()

# Or list the fields in a particular layer
ls(Ether)


# In[ ]:


# Dump the packet contents in hex
hexdump(pkt)


# In[ ]:


# Dump the packet in a nice format
pkt.show()


# In[ ]:


# You can manipulate the packet through fields

pkt.dst = "11:22:33:44:55:66"

pkt.show()


# Your task in this lab is to iterate over all packets we just read in (into the variable pkts), and if it is of type Ether, change it's source address to 11:11:11:11:11:11, and its destination address to 22:22:22:22:22:22

# In[ ]:


# your code here
for pkt in pkts:
    if Ether in pkt:  # Check if the packet is an Ethernet packet
        pkt[Ether].src = "11:11:11:11:11:11"  # Update source address
        pkt[Ether].dst = "22:22:22:22:22:22"  # Update destination address

# In[ ]:


"""Check that you successfully modified all Ether type packets in pkts"""



