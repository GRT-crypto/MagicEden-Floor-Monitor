from ast import parse
from time import sleep
import requests
import json

def parse_floor(unparsed_amount):
    unparsed = str(unparsed_amount)

    #.01 value
    if len(unparsed) == 8:
        amount = "." + unparsed[0:2]
        return float(amount)
    #.1 value
    elif len(unparsed) == 9:
        amount = "." + unparsed[0:3]
        return float(amount)
    #1 value
    elif len(unparsed) == 10:
        amount = unparsed[0] + "." + unparsed[1:3]
        return float(amount)
    #10 value
    elif len(unparsed) == 11:
        amount = unparsed[0:2] + "." + unparsed[3:5]
        return float(amount)
    #100 value
    elif len(unparsed) == 12:
        amount = unparsed[0:3] + "." + unparsed[4:6]
        return float(amount)
    #1000 value (lol)
    elif len(unparsed) == 13:
        amount = unparsed[0:4] + "." + unparsed[5:7]
        return float(amount)
    else:
        print("MagicEden Timeout or Malformatted API Response")

def main():

  headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',}
  
  print("  ██████  ▒█████   ██▓      ██████  █    ██  ██▓▄▄▄█████▓▓█████ \n▒██    ▒ ▒██▒  ██▒▓██▒    ▒██    ▒  ██  ▓██▒▓██▒▓  ██▒ ▓▒▓█   ▀ \n░ ▓██▄   ▒██░  ██▒▒██░    ░ ▓██▄   ▓██  ▒██░▒██▒▒ ▓██░ ▒░▒███   \n  ▒   ██▒▒██   ██░▒██░      ▒   ██▒▓▓█  ░██░░██░░ ▓██▓ ░ ▒▓█  ▄ \n▒██████▒▒░ ████▓▒░░██████▒▒██████▒▒▒▒█████▓ ░██░  ▒██▒ ░ ░▒████▒\n▒ ▒▓▒ ▒ ░░ ▒░▒░▒░ ░ ▒░▓  ░▒ ▒▓▒ ▒ ░░▒▓▒ ▒ ▒ ░▓    ▒ ░░   ░░ ▒░ ░\n░ ░▒  ░ ░  ░ ▒ ▒░ ░ ░ ▒  ░░ ░▒  ░ ░░░▒░ ░ ░  ▒ ░    ░     ░ ░  ░\n░  ░  ░  ░ ░ ░ ▒    ░ ░   ░  ░  ░   ░░░ ░ ░  ▒ ░  ░         ░ \n        ░      ░ ░      ░  ░      ░     ░      ░              ░  ░\n                                                                ")
  print("Enter Collection Name:")
  project_name = input()

  while True:
    me_page = requests.get(url=f"https://api-mainnet.magiceden.io/rpc/getCollectionEscrowStats/{project_name}", headers=headers).text
    me_json = json.loads(me_page)
    unparsed_key = me_json['results']['floorPrice']
    parsed_key = parse_floor(unparsed_key)
    print(f"[{project_name}] - {parsed_key}")
    sleep(2)

if __name__ == "__main__":
    main()
