import re
# input is the list of usernames, output is the output (duh)
input_file = "caps.txt"
output_file = "lower.txt"

#open the file and load it to memory
with open(input_file, "r", encoding="utf-8") as file:
    text = file.read()
    
# change capital letters to lowercase    
text = text.lower()

#remove the @ and everything on a line before that, also everything that comes after the username
text = re.sub(r'.*?@(\S+).*', r'\1', text)

#write the file
with open(output_file, "w", encoding="utf-8") as file:
    file.write(text)
   