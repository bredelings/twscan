import re

def draw_graph(sector, ports):
    print('strict digraph G {')
    print('  concentrate=true')
    print('  overlap=false')
    for s1 in warps.keys():
        for s2 in warps[s1]:
            if s1 in warps.get(s2,set()):
                if (s1 < s2):
                    print("  "+s1+" -> "+s2+' [dir="both"]')
            else:
                print("  "+s1+" -> "+s2)
    for s in ports.keys():
        print("  "+s+'[label="'+s+"\\n"+ports[s]+'"]')
    print('}')

def scan(filename):
    f = open(filename,'r',encoding="cp1252")

    ansi_escape = re.compile(r'\x1b[^m]*m')

    sector = "unknown"
    warps = {}
    ports = {}
    for line in f:
        line = ansi_escape.sub('',line)

        m = re.match('Sector  : (\d+) in',line)
        if m:
            sector = m.group(1)
#           print('sector = ' + sector, end='\n')
            continue

        m = re.match('Ports   : .*\((.*)\)',line)
        if m:
            ports[sector] = m.group(1)
            continue

        m = re.match('^Warps to Sector\(s\) :  (.*)$',line)
        if m:
#           print(m.group(1), end='\n')
           for dest in m.group(1).split(' - '):
               m = re.match('\((.*)\)',dest)
               if m:
                   dest = m.group(1)
#               print(sector + " -> " + dest)
               if (sector != "unknown"):
                   warps[sector] = warps.get(sector,set())
                   warps[sector].add(dest)
           continue

    sector = "unknown"
    return (warps,ports)

if __name__ == "__main__":
    import sys
    (warps,ports) = scan(sys.argv[1])
    draw_graph(warps,ports)


