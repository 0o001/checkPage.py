#!/usr/bin/env python
import requests
import argparse

__author__ = 'mustafauzun0'

'''
      _               _                           
  ___| |__   ___  ___| | ___ __   __ _  __ _  ___ 
 / __| '_ \ / _ \/ __| |/ / '_ \ / _` |/ _` |/ _ \
| (__| | | |  __/ (__|   <| |_) | (_| | (_| |  __/
 \___|_| |_|\___|\___|_|\_\ .__/ \__,_|\__, |\___|
                          |_|          |___/      
'''

def main():
    parser = argparse.ArgumentParser(description='Website Page Checker')
    
    parser.add_argument('-u', '--url', dest='url', type=str, help='Website URL', required=True)
    parser.add_argument('-p', '--page', dest='page', type=str, default='', help='Website Page')

    args = parser.parse_args()

    if args.url:
        args.url = args.url.strip().strip('/')

    if args.page:
        args.page = args.page.strip().strip('/')

    request = requests.get(args.url + '/' + args.page, allow_redirects=False)
    
    print(request)
    
if __name__ == '__main__':
	main()
