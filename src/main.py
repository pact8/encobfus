from colorama import init, Fore, Back, Style
import argparse
parser = argparse.ArgumentParser(description='encryption obfuscator')
parser.add_argument('input', type=str, help='path to the input script')
parser.add_argument('output', type=str, help='path to the output script')
parser.add_argument('encmethod', type=str, help='encryption method')
args = parser.parse_args()

banner = """                                 d8b         ,d8888b                 
                                 ?88         88P'                    
                                  88b     d888888P                   
 d8888b  88bd88b  d8888b d8888b   888888b   ?88'    ?88   d8P .d888b,
d8b_,dP  88P' ?8bd8P' `Pd8P' ?88  88P `?8b  88P     d88   88  ?8b,   
88b     d88   88P88b    88b  d88 d88,  d88 d88      ?8(  d88    `?8b 
`?888P'd88'   88b`?888P'`?8888P'd88'`?88P'd88'      `?88P'?8b`?888P' 
                                                                     
                                                                     
                                                                     """

init()


print(Fore.CYAN + banner + Style.RESET_ALL)

if args.encmethod == "fernet":
  #importing the fernet libs(require cryptography)
	from cryptography.fernet import Fernet
	k = Fernet.generate_key()
	ct = Fernet(k)
	print(Fore.GREEN + "[*] Key Generated" + Style.RESET_ALL)
	content_file = ""
	
	with open(args.input, "r") as f:
		content_file = f.read()
		f.close()
	print(Fore.GREEN + "[*] Content Readed" + Style.RESET_ALL)
	content_file = content_file.encode('utf-8')
	cf_encrypted = ct.encrypt(content_file)
	cfe_str = cf_encrypted.decode('utf-8')
	print(Fore.GREEN + "[*] Content Encrypted" + Style.RESET_ALL)
	with open(args.output, "w") as f:
		f.write(f"""
from cryptography.fernet import Fernet
key = {k}
ciphert = Fernet(key)
code = "{cfe_str}"
dec_code = ciphert.decrypt(code)
dec_code_s = dec_code.decode('utf-8')
exec(dec_code_s) 
""")
		f.close()

	print(Fore.GREEN + "[*] Encrypted Content Writed" + Style.RESET_ALL)
	
