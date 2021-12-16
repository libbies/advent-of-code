#!python
# coding: future_fstrings
"""advent of code 2021 day 16 part 1"""
from functools import reduce
class Packet():
    """a packet"""
    def __init__(self, bits, hexits=None):
        self._raw = bits if bits else ''.join(f"{int(h, 16):0>4b}" for h in hexits)
        if self.type!=4:
            self.subpackets = self._subpackets()
        assert isinstance(self.value, int)

    def _subpackets(self):
        assert self.type!=4 # operator, self.type!=4
        subpackets = []
        if self.lentype==0: # total length in bits
            self._hdrlen = 22
        elif self.lentype==1: # number of sub-packets immediately contained
            self._hdrlen = 18
        self._len = self._hdrlen
        sublen, subpacketraw = self.sublen, self._raw[self._hdrlen:]
        while sublen:
            subpacket = Packet(subpacketraw)
            subpackets.append(subpacket)
            self._len += len(subpacket)
            sublen -= 1 if self.lentype==1 else len(subpacket)
            assert sublen>=0
            subpacketraw = subpacketraw[len(subpacket):]
        self._subpacketraw = self._raw[:self._len]
        return subpackets

    @property
    def version(self):
        return int("0b" + self._raw[0:0+3], 2)

    @property
    def type(self):
        return int("0b" + self._raw[3:3+3], 2)

    @property
    def lentype(self):
        assert self.type!=4
        return int("0b" + self._raw[6:6+1], 2)

    @property
    def sublen(self):
        assert self.type!=4
        return int("0b" + self._raw[7:7+(15 if self.lentype==0 else 11)], 2)

    @property
    def value(self):
        if self.type==0:   # op:add
            return sum(p.value for p in self.subpackets)
        elif self.type==1: # op:mul
            return reduce(int.__mul__, (p.value for p in self.subpackets))
        elif self.type==2: # op:min
            return min(p.value for p in self.subpackets)
        elif self.type==3: # op:max
            return max(p.value for p in self.subpackets)
        elif self.type==4: # val
            self._groups = []
            for bit in [self._raw[6:][i*5:(i+1)*5] for i in range(len(self._raw[6:])//5)]:
                self._groups.append(bit)
                if bit[0]=="0":
                    break
            assert len(self._groups)>=1
            self._len = 6 + len(self._groups)*5
            return int("0b"+''.join(bit[-4:] for bit in self._groups), 2)
        elif self.type==5: # op:gt
            assert len(self.subpackets)==2
            return self.subpackets[0].value>self.subpackets[-1].value
        elif self.type==6: # op:lt
            assert len(self.subpackets)==2
            return self.subpackets[0].value<self.subpackets[-1].value
        elif self.type==7: # op:cmp
            assert len(self.subpackets)==2
            return self.subpackets[0].value==self.subpackets[-1].value

    def __len__(self):
        return self._len

    def __repr__(self):
        if self.type==4:
            return f"(ver={self.version}, type=lit:4, len={len(self)}, " \
                    f"groups={self._groups}, value={self.value})"
        elif self.type!=4:
            return (f"(ver={self.version}, type=(op:{self.type}:{self.lentype}), " \
                f"len={len(self)}, " \
                f"{'sublen' if self.lentype==0 else 'subpkt'}:{self.sublen}, " \
                f"splen:{len(self._subpacketraw)}), value:{self.value})")

queue = [Packet(bits=None, hexits=open("input.txt").read().strip())]
answer = 0
while queue:
    packet = queue.pop()
    answer += packet.version
    if packet.type!=4:
        queue.extend(packet.subpackets)

print("aoc 2021 day 16 part 1:", answer)
