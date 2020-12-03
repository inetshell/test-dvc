file = open("data.txt","r")

# Count lines
nonempty_lines = [line.strip("\n") for line in file if line != "\n"]
line_count = len(nonempty_lines)

# Count words
file.seek(0)
data = file.read().split()
words_count = len(data)

# Close file and print output
file.close()
print("lines: {}".format(line_count))
print("words: {}".format(words_count))

