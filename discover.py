import requests
import json, io

bootstrap = "152.228.155.120:8765"

try:
    with io.open("nodes.json", "r") as f:
        nodes = set(json.load(f))
except:
    nodes = set()

while True:
    try:
        peers = requests.get(
            "http://{}/peers".format(bootstrap),
            headers={"X-ZEEKA-NETWORK-NAME": "debug"},
            timeout=2,
        ).json()
        for peer in peers["peers"]:
            if peer["address"] not in nodes:
                nodes.add(peer["address"])
        with io.open("nodes.json", "w") as f:
            json.dump(list(sorted(nodes)), f, indent=3)
    except KeyboardInterrupt:
        break
