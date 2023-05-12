import re

# Open the input and output files
input_file = open('inputURLs.txt', 'r')
output_file = open('outputURLs.txt', 'w')

# Define a regular expression to match URLs
url_regex = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')

# Loop through each line in the input file
for line in input_file:
    # Find all URLs in the line
    urls = re.findall(url_regex, line)

    # Write each URL to the output file
    for url in urls:
        output_file.write(url + '\n')

# Close the input and output files
input_file.close()
output_file.close()
