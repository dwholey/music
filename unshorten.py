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
    short_url = short_url.strip()
    if not short_url or not short_url.startswith(('http://', 'https://')):
        print(f'Skipping invalid or empty URL: {short_url}')
        continue
    try:
        unshortened_url = urllib.request.urlopen(short_url).geturl()
        unshortened_urls.append(re.match('^(.*?)\?', unshortened_url).group(1))
    except urllib.error.HTTPError as e:
        print(f'Error retrieving URL {short_url}: {e}')
    except Exception as e:
        print(f'Unexpected error: {e}')

with open(unshortened_urls_file, 'w') as f:
    for unshortened_url in unshortened_urls:
        f.write(unshortened_url + '\n')
