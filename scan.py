import re

def draw_graph(sector, ports):
    for s1 in warps.keys():
        for s2 in warps[s1]:
            print(s1+" -> "+s2)
    for s in ports.keys():
        print(s+": "+ports[s])

def scan(filename):
    f = open(filename,'r')
    location = "unknown"
    sector = "unknown"
    warps = {}
    ports = {}
    for line in f:
        m = re.match('.*arping to sector (\d+)$',line)
        if m:
            location = m.group(1)
#            print('sector = ' + location, end='\n')
        m = re.match('Sector  : (\d+) in',line)
        if m:
            sector = m.group(1)
#            print('sector = ' + location, end='\n')

        m = re.match('Ports   : .*\((.*)\)',line)
        if m:
            ports[sector] = m.group(1)


        m = re.match('^Warps to Sector\(s\) :  (.*)$',line)
        if m:
#           print(m.group(1), end='\n')
           for dest in m.group(1).split(' - '):
               m = re.match('^\((.*)\)$',dest)
               if m:
                   dest = m.group(1)
#               print(location + " -> " + dest)
               if (location != "unknown"):
                   warps[location] = warps.get(location,set())
                   warps[location].add(dest)

    return (warps,ports)

if __name__ == "__main__":
    import sys
    (warps,ports) = scan(sys.argv[1])
    draw_graph(warps,ports)


