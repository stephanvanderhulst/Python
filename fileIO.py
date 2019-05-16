ipsum_file = open('ipsum.txt')

for line in ipsum_file:
    print(line.rstrip())

ipsum_file.seek(0) #resets to the start of the file so we can go through it again

lines = ipsum_file.readlines() #puts every line as a value in an array
print(lines)

#now lets go to character 50 and read 100 chars from that point
ipsum_file.seek(50)
file_text = ipsum_file.read(100)
print(file_text)

#close the file connection to help performance
ipsum_file.close()

print('*******************************************************************')

#function that filters out lines that have olo in it
def filter_line(line):
    return 'olo' not in line

#lets look at a better/different way of accessing the file
#We dont have to close the file, Python does that for us
with open('ipsum.txt') as ipsum_file:
    lines = ipsum_file.readlines()
    print(list(filter(filter_line, lines)))
#we dont have to close this connection

#writing to a file, starting this again will write from the beginning and overwrite existing content
with open('write.txt', 'w') as write_file:
    write_file.write('Testing Python write!!')
    write_file.write('\nThis is the second line') #\n is the newline character


with open('write.txt', 'a') as write_file: #a makes it append instead of write over
    write_file.write('\nAppending some more text on a new line')
    write_file.write('\nBlablabla') #\n is the newline character

quotes = [
    '\noiwfuhewifhuw',
    '\npiwefuhu',
    '\ndksfjnwpifbewfeiwbh'
]

with open('write.txt', 'a') as write_file:
    write_file.writelines(quotes)