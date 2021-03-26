# hackingTools

Simple Ethical hacking tools in Python 3 for personal educative purposes. 

### Network scanner

Automated network scanner with nmap: ```network_scan.py```.

Prerequisites:

- ```nmap``` tool
	- how to install: https://nmap.org/
- ```python-nmap``` library
	- how to install: ```pip install python-nmap```

Run the script with IPv4 address:

- ```python3 ./network_scan.py X.X.X.X ```

Output:

- Status of the host, the open port, the scanning method, the likely OS in a ```X.X.X.X.txt``` file, with a timestamp.

