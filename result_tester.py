"""
Charlie Schuck 2022.
This program takes a masscan result text file and uses mcstatus to check and see whether each of the resulting servers (open on port 25565) are really minecraft servers or not.
"""
from mcstatus import JavaServer
import multiprocessing
import os


def check(ip):
    try:
        minecraft = JavaServer(ip, 25565)
        server_info = minecraft.status()

    except Exception as e:
        print(e)
        print(ip)

    else:
        with open(out_file, 'a', encoding='utf-8') as out:
            out.write("ip:" + str(ip) + " ver: " + str(server_info.version.name) + " players: " + str(server_info.players.online) + "\n")
            out.write("players: " + str(server_info.players.sample) + "\n")
        out.close()


in_file = os.path.join(os.getcwd(), 'scan_merge')
out_file = os.path.join(os.getcwd(), 'out.txt')

ip_addresses = []

with open(in_file, 'r', encoding='utf-8') as scan:
    in_list = scan.readlines()
    scan.close()

processes = []
force_join = 0
for line in in_list:
    if not line[0] == '#':
        ip_addresses.append(line.strip().split(' ')[3])

processes = []

for ip in ip_addresses:
    x = multiprocessing.Process(target=check, args=(ip,))
    processes.append(x)
    x.start()

    if len(processes) > 64:
        processes[force_join].join()
        processes[force_join].close()
        force_join += 1

for process in processes:
    process.join()
    process.close()
