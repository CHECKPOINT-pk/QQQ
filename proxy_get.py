import requests
import os

def get_fresh_proxies():
    # 2026 Updated High-Speed Proxy Sources
    sources = [
        "https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=10000&country=all",
        "https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all",
        "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt",
        "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
        "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks5.txt",
        "https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt",
        "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt",
        "https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks5.txt"
    ]
    
    print("\033[1;36m[!] Scrape Shuru Ho Rahi Hai... Intezar Karein.\033[0m")
    proxy_list = []
    
    for url in sources:
        try:
            r = requests.get(url, timeout=10)
            if r.status_code == 200:
                p = r.text.splitlines()
                proxy_list.extend(p)
                print(f"\033[1;32m[+] Found {len(p)} Proxies from Source.\033[0m")
        except:
            continue

    # Duplicates saaf karna
    proxy_list = list(set(proxy_list))
    
    with open("proxy.txt", "w") as f:
        for proxy in proxy_list:
            if ":" in proxy:
                f.write(proxy + "\n")
                
    print(f"\n\033[1;32m[SUCCESS] Total {len(proxy_list)} Fresh Proxies Saved in proxy.txt\033[0m")

if __name__ == "__main__":
    get_fresh_proxies()
