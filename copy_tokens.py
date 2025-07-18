origin_file_name = "./new_tokens.txt"
final_file_name = "./Playlist.m3u"

try:
    with open(origin_file_name, "r") as origin_file:
        origin_lines = origin_file.readlines()
        if len(origin_lines) == 0:
            print("The origin file is empty")
except FileNotFoundError:
    print(f"File not found '{origin_file_name}'")

final_lines = []

try:
    with open(final_file_name, "r") as final_file:
        final_lines = final_file.readlines()
except FileNotFoundError:
    print(f"File not found '{final_file_name}'")


#copy the lines to the final lines array
final_lines[6] = origin_lines[0]
final_lines[8] = origin_lines[1]
counter = 0
for item in range(2,28):
    final_lines[27+item+counter] = origin_lines[item]
    counter+=1

#write on the final file
try:
    with open(final_file_name, "w") as final_file:
        final_file.writelines(final_lines)
except IOError as e:
    print(f"Error while writing on the file '{final_file_name}': {e}")