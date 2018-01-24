import re

class IPAddress:
    str_IP_Adress = str()
    block = list()

    def __init__(self, addr):
        self.str_IP_Adress = addr
        self.block = re.findall(r'(\d{1,3})' ,addr)

    def __eq__(self, other):
        return isinstance(other, IPAddr) and self.str_IP_Adress == other.str_IP_Adress

    def __hash__(self):
        return hash(self.str_IP_Adress)

    def __lt__(self, other):
        return ((self.block[0] != other.block[0]) and
                (self.block[1] != other.block[1]) and
                (self.block[2] != other.block[2]) and
                (self.block[3] < other.block[3]))

ip_regex_pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')

with open('access.log', 'r') as log_File:
    IP_Adress = list({IPAddr(ip_regex_pattern.match(row).group(0)) for row in log_File})

IP_Adress.sort()

for i in range (0, IP_Adress.__len__()):
    print(IP_Adress[i].str_IP_Adress)