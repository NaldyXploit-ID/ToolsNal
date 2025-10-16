#!/usr/bin/env python3
# realistic sample...
import argparse, json, random, string
def gen(n=8): return ''.join(random.choice(string.ascii_letters+string.digits) for _ in range(n))
if __name__=='__main__':
    p=argparse.ArgumentParser(); p.add_argument('action', choices=['demo','token']); a=p.parse_args()
    if a.action=='demo': print(json.dumps({'sample':gen(8)})); else: print('token')
