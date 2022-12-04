# MCJavaServerScanner
small tool used with masscan output to determine if a given address is a minecraft server. 

# masscan (if on windows, requires WSL 2)
https://github.com/robertdavidgraham/masscan
install and use the following command to find servers that are listening on port 25565: 
masscan 0.0.0.0/0 -p0-25565 --excludefile exclude.conf -oL output.txt --max-rate 64000

the excludefile contains masscan's recommended exclusions ;; instutions that do not wish to be scannned. 
for the max rate, choose something you're comfortable with. 64000 may freeze up your machine. 
It is also important to keep in mind that you don't *need* to scan the entire internet, I found thousands of servers in a masscan of only 30,000 ip addresses.

# mcstatus
install mcstatus: https://github.com/py-mine/mcstatus
you may have to change some variables before running my code ;; like in_file and desired out_file, I was too lazy to parameterize them.
