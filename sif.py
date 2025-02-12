#! python

import os
import re
import argparse
import requests
import json
import sys

# Define ANSI color codes
RED = "\033[91m"
GREEN = "\033[92m"
BLUE = "\033[94m"
CYAN = "\033[96m"
PINK = "\033[95m"
RESET = "\033[0m"

ascii_art = f"""
{PINK}
    ███╗   ███╗██╗██╗  ██╗███████╗
    ████╗ ████║██║██║ ██╔╝██╔════╝
    ██╔████╔██║██║█████╔╝ █████╗  
    ██║╚██╔╝██║██║██╔═██╗ ██╔══╝  
    ██║ ╚═╝ ██║██║██║  ██╗███████╗
    ╚═╝     ╚═╝╚═╝╚═╝  ╚══════╝

    👑 Created by Mike Masanga{RESET}
"""

def get_wayback_urls(domain):
    try:
        url = f"https://web.archive.org/cdx/search/cdx?url=*.{domain}/*&collapse=urlkey&output=text&fl=original"
        response = requests.get(url)
        if response.status_code == 200:
            return response.text.splitlines()
        else:
            print(f"{RED}Error fetching URLs from Wayback Machine.{RESET}")
            return []
    except requests.RequestException as e:
        print(f"{RED}Request error: {e}{RESET}")
        return []

def check_snapshot(url):
    try:
        archive_url = f"https://web.archive.org/cdx/search/cdx?url={url}&output=json"
        response = requests.get(archive_url)
        if response.status_code == 200:
            archive_data = response.json()
            if len(archive_data) > 1:
                timestamp = archive_data[1][1]
                snapshot_link = f"https://web.archive.org/web/{timestamp}/{url}"
                print(f"{CYAN}📁 {url} {GREEN}✅ (Snapshot Available) 🔗 {snapshot_link} {RESET}")
            else:
                print(f"{CYAN}📁 {url} {RED}❌ (No Snapshot){RESET}")
        else:
            print(f"{RED}Error checking snapshot for {url}{RESET}")
    except requests.RequestException as e:
        print(f"{RED}Request error: {e}{RESET}")

def find_files_from_urls(urls, extensions):
    pattern = re.compile(rf".*({extensions})$", re.IGNORECASE)
    
    for url in urls:
        if pattern.match(url):
            check_snapshot(url)

def main():
    try:
        print(ascii_art)
        parser = argparse.ArgumentParser(description="Find files with specific extensions from Wayback Machine.")
        parser.add_argument("-d", "--domain", type=str, help="Domain to search")
        parser.add_argument("-list", "--list", type=str, help="File containing a list of domains")
        args = parser.parse_args()

        if args.list:
            if not os.path.isfile(args.list):
                print(f"{RED}Error: The file {args.list} does not exist.{RESET}")
                return
            with open(args.list, "r") as f:
                domains = [line.strip() for line in f if line.strip()]
        elif args.domain:
            domains = [args.domain]
        else:
            domains = [input(f"{BLUE}Enter the domain: {RESET}")]

        extensions = r'\.xls|\.xml|\.xlsx|\.json|\.pdf|\.sql|\.doc|\.docx|\.pptx|\.txt|\.zip|\.tar\.gz|\.tgz|\.bak|\.7z|\.rar|\.log|\.cache|\.secret|\.db|\.backup|\.yml|\.gz|\.config|\.csv|\.yaml|\.md|\.md5'

        for domain in domains:
            print(f"{BLUE}Fetching URLs from Wayback Machine for {domain}...{RESET}")
            urls = get_wayback_urls(domain)
            print(f"{BLUE}Checking for matching files...{RESET}")
            find_files_from_urls(urls, extensions)
        
        print(f"{GREEN}Done!{RESET}")

    except KeyboardInterrupt:
        print(f"\n{RED}Process interrupted by user. Exiting...{RESET}")
        sys.exit(1)

if __name__ == "__main__":
    main()
