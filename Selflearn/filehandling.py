#File Objects


with open("Selflearn/text.txt", "r") as f: #vscode works with the project directory rather than folder, so Selflearn needs to be here. For dynamic use os. example below.
    # print(f.readline()) # this fetch one line from the text.txt file.
    # print(f.readlines()) # this fetches everything but in a list, every line is treated as an item in a list.

    # to get everything lets use the loop
    output = []
    for i in f:
        output.append(i.upper()) #string methods always use parenthesis

with open("output.txt", "w") as f:
    f.writelines(output)