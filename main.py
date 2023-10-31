import requests
import os
import json
import aiohttp
import asyncio
import json


response = requests.get("https://jsonplaceholder.typicode.com/posts")
print(response.json())
for r in response.json():
    print(r)
    os.mkdir(str(r["id"]))
    with open(f"{r['id']}/{r['id']}.json", 'w') as f:
        f.write(json.dumps(r, indent=4))

async def main():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    print(response.json())
    for r in response.json():
        print(r)
        os.mkdir(str(r["id"]))
        with open(f"{r['id']}/{r['id']}.json", 'w') as f:
            f.write(json.dumps(r, indent=4))