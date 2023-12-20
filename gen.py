import requests, random, threading, time, ctypes, os, uuid
from random import choice 
print("""


  _    _      _    _          _                  
 | |_ (_)__ _| |_ | |__  __ _| |__ _ _ _  __ ___ 
 | ' \| / _` | ' \| '_ \/ _` | / _` | ' \/ _/ -_)
 |_||_|_\__, |_||_|_.__/\__,_|_\__,_|_||_\__\___|
        |___/                                    
                Tool By highbalance
                https://discord.gg/NvSC33D2wq
                https://discord.gg/003
""")
proxy = open("proxy.txt","r").read().splitlines()
class counter:
    count = 0
num_threads = int(input(f"Enter Number Of Threads : "))
def gen(proxy):
    while True:
        prox = random.choice(proxy) 
        url = "https://api.discord.gx.games/v1/direct-fulfillment"
        headers = {
            "Content-Type": "application/json",
            "Sec-Ch-Ua": '"Opera GX";v="105", "Chromium";v="119", "Not?A_Brand";v="24"',
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 OPR/105.0.0.0",
        }

        data = {
            "partnerUserId": str(uuid.uuid4())
        }

        try:
            if proxy is not None:
                response = requests.post(url, json=data, headers=headers, proxies={'http': f'http://{prox}','https': f'http://{prox}'}) 
            else:
                response = requests.post(url, json=data, headers=headers, timeout=5)

            if response.status_code == 200:
                token = response.json().get('token')
                if token:
                    counter.count += 1
                    ctypes.windll.kernel32.SetConsoleTitleW(
                            f"Nitro gen highbalance"
                            f" | Generated : {counter.count}")
                    link = f"https://discord.com/billing/partner-promotions/1180231712274387115/{token}"
                    with open("promos.txt", "a") as f:
                        f.write(f"{link}\n")
                    print(f"Generated Promo Link : {link}")
            elif response.status_code == 429:
                print(f"You are being rate-limited!")
            else:
                 print(f"Bad Proxy")
        except Exception as e:
            print(f"Bad Proxy")

while True:
        while threading.active_count() > num_threads:
            time.sleep(1.0)
        threading.Thread(target=gen, args=(proxy,)).start()
