import re
def extract_tiktok_usernames(input_file, output_file):
    usernames = []

#open list of usernames and read line by line    
    with open(input_file, 'r', encoding='utf-8') as file:
        urls = file.readlines()
        
    for url in urls:
        url = url.strip() #remove spaces and newlines
        url = url.split('?')[0] #remove query parameters if they exist

#change tiktok here to facebook or instagram or whatever usernames you're trying to scrape
        
        if "tiktok" in url:
            match = re.search(r'@([^/]+)', url)
            if match:
                username = match.group(1).split('/')[0]
                usernames.append(username.lower())
#take nice and clean usernames and export them to a new list                
    with open(output_file, 'w', encoding='utf-8') as file:
        for username in usernames:
            file.write(username + '\n')
#input_filename is your list of URLs, output can be whatever            
input_filename = "rawusers.txt"
output_filename = "pureusers.txt"

extract_tiktok_usernames(input_filename, output_filename)

print(f"Processed usernames have been saved to {output_filename}")