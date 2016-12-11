from sys import argv

script_name, file_name = argv

file = open(file_name)

print file.read()
