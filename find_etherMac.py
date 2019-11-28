import re

def getLinuxMacAddress(): 
    ifname = 'eth0'
    mac_eth=open('/sys/class/net/%s/address' % ifname).read()
    return mac_eth

EuId  = re.sub(':', '', getLinuxMacAddress())[:12]+'1234'
print(EuId)