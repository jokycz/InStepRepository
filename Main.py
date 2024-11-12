import re

in_text_file = "c:\\courseFiles\\testin.txt"
out_text_file = "c:\\courseFiles\\testout.txt"

file_in = open(in_text_file, "r")
file_out = open(out_text_file, "w")
for line in file_in:
    for words in re.split(r'[\s.,!?;:]+', line):
        if len(words) >= 7 :
            file_out.write(words + "\n")

file_in.close()
file_out.close()

with open(out_text_file, "r") as file_out:
    print("Obsah výstupního souboru:")
    print(file_out.read())

