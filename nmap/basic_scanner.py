import nmap

nm = nmap.PortScanner()
nm.scan('54.39.46.56/32', '0-1024')
print(nm.csv())