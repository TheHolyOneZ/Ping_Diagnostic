import platform
import subprocess
import time
import sys
from datetime import datetime

def clear():
    subprocess.run(["cls" if platform.system() == "Windows" else "clear"], shell=True)

def banner():
    print("""
    \033[92m
    ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
    █     PING DIAGNOSTIC     █
    ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
          Made by TheZ
    \033[0m""")

def ping_target(address):
    cmd = ["ping", "-n" if platform.system() == "Windows" else "-c", "4", address]
    
    print(f"\033[93m[*] Address: {address}")
    print(f"[*] Time: {datetime.now().strftime('%H:%M:%S')}\033[0m")
    
    try:
        result = subprocess.run(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            encoding='cp437' if platform.system() == "Windows" else 'utf-8'
        )

        if result.returncode == 0:
            print("\033[92m[+] Success\033[0m")
            for line in result.stdout.split('\n'):
                if any(x in line.lower() for x in ["time=", "zeit="]):
                    print(f"\033[96m{line}\033[0m")
                else:
                    print(f"\033[97m{line}\033[0m")
        else:
            print(f"\033[91m[-] Failed\n{result.stderr}\033[0m")
            
    except Exception as e:
        print(f"\033[91m[-] Error: {e}\033[0m")

def main():
    while True:
        clear()
        banner()
        
        address = input("\033[95m[>] Enter address: \033[0m").strip()
        
        if address.lower() == 'exit':
            print("\033[92m[+] Exiting\033[0m")
            time.sleep(0.5)
            break
        
        if address:
            ping_target(address)
            input("\n\033[93mPress Enter\033[0m")
        else:
            print("\033[91m[-] Invalid input\033[0m")
            time.sleep(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\033[92m[+] Stopped\033[0m")
