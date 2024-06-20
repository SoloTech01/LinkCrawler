import colorama
import os
import time
colorama.init()
GREEN = colorama.Fore.GREEN
GRAY = colorama.Fore.LIGHTBLACK_EX
RESET = colorama.Fore.RESET
YELLOW = colorama.Fore.YELLOW
BLUE = colorama.Fore.LIGHTBLUE_EX
RED = colorama.Fore.RED
print(f""" {GREEN}

╭╮╱╱╱╱╱╱╭╮╱╱╭━━━╮╱╭━━━┳╮╭╮╭┳╮╱╱╭━━━┳━━━╮
┃┃╱╱╱╱╱╱┃┃╱╱┃╭━╮┃╱┃╭━╮┃┃┃┃┃┃┃╱╱┃╭━━┫╭━╮┃
┃┃╱╱╭┳━╮┃┃╭╮┃┃╱╰╋━┫┃╱┃┃┃┃┃┃┃┃╱╱┃╰━━┫╰━╯┃
┃┃╱╭╋┫╭╮┫╰╯╯┃┃╱╭┫╭┫╰━╯┃╰╯╰╯┃┃╱╭┫╭━━┫╭╮╭╯
┃╰━╯┃┃┃┃┃╭╮╮┃╰━╯┃┃┃╭━╮┣╮╭╮╭┫╰━╯┃╰━━┫┃┃╰╮
╰━━━┻┻╯╰┻╯╰╯╰━━━┻╯╰╯╱╰╯╰╯╰╯╰━━━┻━━━┻╯╰━╯
""")
print(RED)
print("WARNING: REQUESTING A WEBSITE MANY TIMES IN A SHORT PERIOD MAY CAUSE THE WEBSITE TO BLOCK YOUR ADDRESS! \n TOO MUCH REQUESTS CAN CROWD THE SERVER AND I WILL NOT BE RESPONSIBLE FOR ANY MISUSE OF THIS TOOL")
print(".......")
print(RESET)
time.sleep(5)

import os
import bs4
import colorama
import requests
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup
import time
import sys
from pathlib import Path

os.system("clear")

colorama.init()
GREEN = colorama.Fore.GREEN
GRAY = colorama.Fore.LIGHTBLACK_EX
RESET = colorama.Fore.RESET
YELLOW = colorama.Fore.YELLOW
BLUE = colorama.Fore.LIGHTBLUE_EX
RED = colorama.Fore.RED

internal_urls = list()
external_urls = list()

def is_valid(url):
	parsed = urlparse(url)
	return bool(parsed.netloc) and bool(parsed.scheme)
	
def get_all_website_links(url):
	urls = set()
	domain_name = urlparse(url).netloc
	soup = BeautifulSoup(requests.get(url).content, "html.parser")
	for a_tag in soup.findAll("a"):
		href = a_tag.attrs.get("href")
		if href == "" or href is None:
			continue
		href = urljoin(url, href)
		parsed_href = urlparse(href)
		href = parsed_href.scheme + "://" + parsed_href.netloc + parsed_href.path
		
		if not is_valid(href):
			continue
		if href in internal_urls:
			continue
		if domain_name not in href:
			if href not in external_urls:
				print(f"{GRAY}[!] External link: {href} {RESET}")
				external_urls.append(href)
			continue
		print(f"{GREEN} [*] Internal link: {href} {RESET}")
		urls.add(href)
		internal_urls.append(href)
	return urls
	
total_urls_visited = 0

def crawl(url, max_urls):
	global total_urls_visited
	total_urls_visited += 1
	print(f"{YELLOW} [*] Crawling: {url} {RESET}")
	links = get_all_website_links(url)
	for link in links:
		if total_urls_visited > max_urls:
			break
		crawl(link, max_urls = max_urls)
		
def program_intro():
	os.system("clear")
	print(f""" {GREEN}

╭╮╱╱╱╱╱╱╭╮╱╱╭━━━╮╱╭━━━┳╮╭╮╭┳╮╱╱╭━━━┳━━━╮
┃┃╱╱╱╱╱╱┃┃╱╱┃╭━╮┃╱┃╭━╮┃┃┃┃┃┃┃╱╱┃╭━━┫╭━╮┃
┃┃╱╱╭┳━╮┃┃╭╮┃┃╱╰╋━┫┃╱┃┃┃┃┃┃┃┃╱╱┃╰━━┫╰━╯┃
┃┃╱╭╋┫╭╮┫╰╯╯┃┃╱╭┫╭┫╰━╯┃╰╯╰╯┃┃╱╭┫╭━━┫╭╮╭╯
┃╰━╯┃┃┃┃┃╭╮╮┃╰━╯┃┃┃╭━╮┣╮╭╮╭┫╰━╯┃╰━━┫┃┃╰╮
╰━━━┻┻╯╰┻╯╰╯╰━━━┻╯╰╯╱╰╯╰╯╰╯╰━━━┻━━━┻╯╰━╯
""")
	print(RESET)
	print(YELLOW)
	print(f"""{GREEN}IMPORTANT{RESET}: {YELLOW}I CAN'T EMPHASIZE THIS ENOUGH,AFTER EXTRACTING LINKS USING THIS TOOL,CHECK YOUR CURRENT WORKING DIRECTORY FOR THE INTERNAL AND EXTERNAL URLs FILES: {Path.cwd()}""")
	print(RESET)
	print(YELLOW)
	print(f""""[+]Author: Solomon Adenuga
[+] Github: https://github.com/SoloTech01
[+] Whatsappp: +2348023710562""")
	print("=====" * 6)
	print(f"""
[1] Website link Extractor
[2] About the tool
[3] Exit the tool
{RESET}""")
	print(GREEN)
	response = input('=====' * 6 + 'Enter a number:' + '=====' * 6 + RESET)
	if response.strip() == "1":
		valid = False
		while not valid:
			try:
				url = input(f"{BLUE}Enter website to extract links from (example = https://www.google.com) : {RESET}")
				print(BLUE)
				max_urls = int(input(f"Enter number of urls to crawl: {RESET}"))
				
				crawl(url, max_urls)
				print("\n")
				print(f"{YELLOW} [+] Total internal links: {len(internal_urls)} {RESET}")
				print(f"{YELLOW} [+] Total External links: {len(external_urls)} {RESET}")
				print(f"{YELLOW} [+] Total Urls: {len(external_urls) + len(internal_urls)} {RESET}")
				print(f"{YELLOW} [+] Total crawled URLs: {max_urls} {RESET}")
				internals = "\n".join(internal_urls)
				with open("Internal_urls.txt", "w") as file:
					file.write(internals)
				externals = "\n".join(external_urls)
				with open("External_urls.txt", "w") as file:
					file.write(externals)
				print(GREEN)
				print(f"Internal and External URLs have been stored in the following paths: {Path.cwd()/'Internal_urls.txt'} \n {Path.cwd()/'External_urls.txt'}")
				print(RESET)
				print("Refreshing in 10 secs.... ")
				time.sleep(10)
				valid = True
			except requests.exceptions.MissingSchema as mis:
				print(RED)
				print("An error occured!")
				print(GREEN)
				print("Detecting error.....")
				time.sleep(2)
				print(RED)
				print(f"Error: {mis} \nConfirm that you entered a valid url and a valid integer for number of crawls!")
				print(RESET)
			except ValueError:
				print(RED)
				print("An error occured!")
				print(GREEN)
				print("Detecting error.....")
				time.sleep(2)
				print(RED)
				print("Enter a valid integer!\nConfirm that you entered a valid url too")
				print(RESET)
			except requests.exceptions.ConnectionError as con:
				print(RED)
				print("An error occured!")
				print(GREEN)
				print("Detecting error.....")
				time.sleep(2)
				print(RED)
				print(f"Error: {con} \nConfirm that you entered a valid url and a valid integer for number of crawls!")
				print(RESET)
			except requests.exceptions.TimeoutError as tim:
				print(RED)
				print("An error occured!")
				print(GREEN)
				print("Detecting error.....")
				time.sleep(2)
				print(RED)
				print(f"Error: {tim} \nConfirm that you entered a valid url and a valid integer for number of crawls!")
				print(RESET)
			except requests.exceptions.HTTPError as htp:
				print(RED)
				print("An error occured!")
				print(GREEN)
				print("Detecting error.....")
				time.sleep(2)
				print(RED)
				print(f"Error: {htp} \nConfirm that you entered a valid url and a valid integer for number of crawls!")
				print(RESET)
			except requests.exceptions.TooManyRedirects as too:
				print(RED)
				print("An error occured!")
				print(GREEN)
				print("Detecting error.....")
				time.sleep(2)
				print(RED)
				print(f"Error: {too} \nConfirm that you entered a valid url and a valid integer for number of crawls!")
				print(RESET)
			except requests.exceptions.RequestException as req:
				print(RED)
				print("An error occured!")
				print(GREEN)
				print("Detecting error.....")
				time.sleep(2)
				print(RED)
				print(f"Error: {req} \nConfirm that you entered a valid url and a valid integer for number of crawls!")
				print(RESET)
			except requests.exceptions.URLRequired as yul:
				print(RED)
				print("An error occured!")
				print(GREEN)
				print("Detecting error.....")
				time.sleep(2)
				print(RED)
				print(f"Error: {yul} \nConfirm that you entered a valid url and a valid integer for number of crawls!")
				print(RESET)
			except requests.exceptions.InvalidSchema as inv:
				print(RED)
				print("An error occured!")
				print(GREEN)
				print("Detecting error.....")
				time.sleep(2)
				print(RED)
				print(f"Error: {inv} \nConfirm that you entered a valid url and a valid integer for number of crawls!")
				print(RESET)
			except requests.exceptions.InvalidURL as lit:
				print(RED)
				print("An error occured!")
				print(GREEN)
				print("Detecting error.....")
				time.sleep(2)
				print(RED)
				print(f"Error: {lit} \nConfirm that you entered a valid url and a valid integer for number of crawls!")
				print(RESET)
			except requests.exceptions.StreamConsumedError as ste:
				print(RED)
				print("An error occured!")
				print(GREEN)
				print("Detecting error.....")
				time.sleep(2)
				print(RED)
				print(f"Error: {ste} \nConfirm that you entered a valid url and a valid integer for number of crawls!")
				print(RESET)
			except requests.exceptions.ChunkedDecodingError as chu:
				print(RED)
				print("An error occured!")
				print(GREEN)
				print("Detecting error.....")
				time.sleep(2)
				print(RED)
				print(f"Error: {chu} \nConfirm that you entered a valid url and a valid integer for number of crawls!")
				print(RESET)
			except requests.exceptions.ContentDecodingError as bic:
				print(RED)
				print("An error occured!")
				print(GREEN)
				print("Detecting error.....")
				time.sleep(2)
				print(RED)
				print(f"Error: {bic} \nConfirm that you entered a valid url and a valid integer for number of crawls!")
				print(RESET)
			except requests.exceptions.ProtocolError as pro:
				print(RED)
				print("An error occured!")
				print(GREEN)
				print("Detecting error.....")
				time.sleep(2)
				print(RED)
				print(f"Error: {pro} \nConfirm that you entered a valid url and a valid integer for number of crawls!")
				print(RESET)
	elif response.strip() == "2":
			print(f""" {YELLOW}Link Crawler is a tool that extracts links from a website saving you time and effort
Benefits:
	Saves time and effort
	Accurate and reliable info
	Autosaves URLs files to your device {RESET}""")
			print(GREEN)
			print("Refreshing in 10 secs......")
			print(RESET)
			time.sleep(10)
	elif response.strip() == "3":
			time.sleep(2)
			print(f"{RED}PROGRAM TERMINATED!{RESET}")
			sys.exit()

while True:
	program_intro()