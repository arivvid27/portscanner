import socket
import termcolor


termcolor.cprint("""192.168.86.1



 _______  _______  _______ _________ _______  _______  _______  _        _        _______  _______            
(  ____ )(  ___  )(  ____ )\__   __/(  ____ \(  ____ \(  ___  )( (    /|( (    /|(  ____ \(  ____ )    
| (    )|| (   ) || (    )|   ) (   | (    \/| (    \/| (   ) ||  \  ( ||  \  ( || (    \/| (    )|    
| (____)|| |   | || (____)|   | |   | (_____ | |      | (___) ||   \ | ||   \ | || (__    | (____)|   
|  _____)| |   | ||     __)   | |   (_____  )| |      |  ___  || (\ \) || (\ \) ||  __)   |     __)    
| (      | |   | || (\ (      | |         ) || |      | (   ) || | \   || | \   || (      | (\ (       
| )      | (___) || ) \ \__   | |   /\____) || (____/\| )   ( || )  \  || )  \  || (____/\| ) \ \__  
|/       (_______)|/   \__/   )_(   \_______)(_______/|/     \||/    )_)|/    )_)(_______/|/   \__/ 
                                                                                                                        
""", 'cyan')

def scan(target, ports):
	termcolor.cprint('\n' + '[!] Starting Scan For ' + str(target), 'magenta')
	for port in range(1,ports):
		scan_port(target,port)


def scan_port(ipaddress, port):
	try:
		sock = socket.socket()
		sock.connect((ipaddress, port))
		termcolor.cprint(f"[+] Port {port} Opened " , 'green')
		sock.close()
	except:
		if cleanmode.lower() == 'n':
			termcolor.cprint(f"[-] Port {port} Closed " , 'red')
			sock.close()
		elif cleanmode.lower() == 'y':
			pass


targets = input(termcolor.colored("[*] Enter Targets To Scan (Split targets with comma) >>  " , 'blue'))
ports = int(input(termcolor.colored("[*] Enter How Many Ports You Want To Scan >> ", 'blue')))
cleanmode = input(termcolor.colored("[*] Would you like a clean output? (y/n) >> ", 'blue'))
if ',' in targets:
	print(termcolor.colored(("[#] Scanning Multiple Targets"), 'yellow'))
	for ip_addr in targets.split(','):
		scan(ip_addr.strip(' '), ports)
else:
	scan(targets,ports)

termcolor.cprint("[*] Scan finished. Please run program again to do another scan.", "yellow")