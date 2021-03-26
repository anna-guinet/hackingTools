import nmap # require python-nmap library + nmap
import sys
import time

# Parameters
ip_address = sys.argv[1] # inline variable
port 	   = 80

# Instantiate a scanner
nm_scan = nmap.PortScanner()

print('\nRunning...\n')

# Run the scanner for IP address, port, OS fingerprinting
nm_scanner = nm_scan.scan(ip_address, str(port), arguments='-O')

# State host, port, scanning method, OS
host_is_up  = "The host is: " + nm_scanner['scan'][ip_address]['status']['state'] + ".\n"
port_open   = "The port %s is: " % (port) + nm_scanner['scan'][ip_address]['tcp'][port]['state'] + ".\n"
method_scan = "The method of scanning is: " + nm_scanner['scan'][ip_address]['tcp'][port]['reason'] + ".\n" 
guessed_os  = "There is %s percent chance that the host is running %s" % (nm_scanner['scan'][ip_address]['osmatch'][0]['accuracy'], nm_scanner['scan'][ip_address]['osmatch'][0]['name']) + ".\n"

# Write output in new file
with open("%s.txt" % ip_address, 'w') as file:
	file.write(host_is_up + port_open + method_scan + guessed_os)
	file.write("\nReport generated " + time.strftime("%Y-%m-%d %H:%M:%S GMT", time.gmtime()))

print("\nFinished")