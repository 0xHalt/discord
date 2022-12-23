import base64
import hashlib
import json
import math
import os
import random
import urllib

import httpx

from datetime import datetime

def compute_hash(req: str) -> str:
    x = "0123456789/:abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    req = req.split(".")
    payload = json.loads(base64.b64decode(req[1] + "=====").decode("utf-8"))

    def increment(r):
        for t in range(len(r) - 1, -1, -1):
            if r[t] < len(x) - 1:
                r[t] += 1
                return True
            r[t] = 0
        return False

    def to_string(r):
        t = ""
        for n in range(len(r)):
            t += x[r[n]]
        return t

    def hash_matches(r, e):
        n = e
        hashed = hashlib.sha1(e.encode())
        o = hashed.hexdigest()
        t = hashed.digest()
        e = None
        n = -1
        o = []
        for n in range(n + 1, 8 * len(t)):
            e = t[math.floor(n / 8)] >> n % 8 & 1
            o.append(e)
        a = o[:r]

        def index2(x, y):
            if y in x:
                return x.index(y)
            return -1
        return 0 == a[0] and index2(a, 1) >= r - 1 or -1 == index2(a, 1)

    def get():
        for e in range(25):
            n = [0 for i in range(e)]
            while increment(n):
                u = payload["d"] + "::" + to_string(n)
                if hash_matches(payload["s"], u):
                    return to_string(n)

    result = get()
    hsl = ":".join([
        "1",
        str(payload["s"]),
        datetime.now().isoformat()[:19]
        .replace("T", "")
        .replace("-", "")
        .replace(":", ""),
        result
    ])
    return hsl

headers = {
    "Host": "hcaptcha.com",
    "Connection": "keep-alive",
    "sec-ch-ua": 'Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92',
    "Accept": "application/json",
    "sec-ch-ua-mobile": "?0",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
    "Content-type": "application/json;charset=utf-8",
    "Origin": "https://newassets.hcaptcha.com",
    "Sec-Fetch-Site": "same-site",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://newassets.hcaptcha.com/",
    "Accept-Language": "en-US,en;q=0.9"
}

def N_Data(req: str) -> str:
    try:
        return compute_hash(req)
    except Exception:
        return ""

      
# HCaptcha bypass for a discord token gen maybe 
