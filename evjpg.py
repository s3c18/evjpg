import engine, sys

class colors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'

def banner():
	b = """\t         _nnnn_
	        dGGGGMMb
	       @p~qp~~qMb
	       M|@||@) M|
	       @,----.JM|
	      JS^\__/  qKL
	     dZP        qKRb
	    dZP          qKKb
	   fZP            SMMb
	   HZM            MMMM
	   FqM            MMMM
	 __| ".        |\dS"qML
	 |    `.       | `' \Zq
	_)      \.___.,|     .'
	\____   )MMMMMP|   .'
	     `-'       `--' hjm"""
	print(b)
def main():
	print(colors.WARNING)
	banner()
	print(colors.ENDC)
	ip = input(colors.OKBLUE + '[---] IP : ' + colors.ENDC)
	port = int(input(colors.OKBLUE + '[---] PORT : ' + colors.ENDC))
	victim = input(colors.OKBLUE + '[---] IP OF VICTIM : ' + colors.ENDC)
	engine.run(ip, port, victim)
main()
