import re

# Define the regular expression pattern for matching ISRCs
pattern = re.compile(r'[A-Z]{2}[A-Z0-9]{3}\d{7}')

# Open the input and output files
with open('ISRClist.txt', 'r', encoding='iso-8859-1') as input_file, open('outputISRCs.txt', 'w') as output_file:
    # Loop through each line in the input file
    for line in input_file:
        # Search for any ISRCs in the line using the regular expression
        matches = pattern.findall(line)
        # If any matches are found, write them to the output file
        for match in matches:
            output_file.write(match + '\n')
