# file = open('data.txt', 'r')
# content = file.read()
# print(content)
# file.close()


# here the issue is that, if that file does not exist, it will raise an error
# or if some error occurs during reading, the file may not be closed properly

# so we need to use context managers to handle file operations safely

with open('data.txt', 'r') as file:
    content = file.read()
    print(content)

# using 'with' statement ensures that the file is properly closed after its suite finishes,
# even if an exception is raised at some point.

# now lets do it while handling file exceptions

try:
    with open('data.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print("Error: The file was not found.")
else:
    print(content)
finally:
    print("Execution completed.")