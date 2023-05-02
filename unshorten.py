import re
import urllib.parse
import urllib.request

# short_urls_file should be a list of URLs you need to expand, unshortened_urls_file is where the full URLs will be saved
short_urls_file = 'short_urls.txt'
unshortened_urls_file = 'unshortened_urls.txt'

with open(short_urls_file, 'r') as f:
    short_urls = f.readlines()

unshortened_urls = []

for short_url in short_urls:
    try:
        unshortened_url = urllib.request.urlopen(short_url.strip()).geturl()
        unshortened_urls.append(re.match('^(.*?)\?', unshortened_url).group(1))
    except urllib.error.HTTPError as e:
        print(f'Error retrieving URL {short_url.strip()}: {e}')

with open(unshortened_urls_file, 'w') as f:
    for unshortened_url in unshortened_urls:
        f.write(unshortened_url + '\n')