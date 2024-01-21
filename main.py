import requests
import sys
sublist = open("subdomain.txt").read()
subdoms = sublist.splitlines()

for sub in subdoms:
    sub_domains = f"https://{sub}.{sys.argv[1]}"

    try:
        requests.get(sub_domains)
    except requests.ConnectionError:
        pass
    else:
        print("valid domains", sub_domains)

