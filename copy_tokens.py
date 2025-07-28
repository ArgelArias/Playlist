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
final_lines[6] = origin_lines[0] #canal 5
counter = 0
for item in range(1,28):
    line_counter = 25+item+counter
    if line_counter >= 75 and line_counter <= 79:
        continue
    final_lines[line_counter] = origin_lines[item]
    counter+=1

#write on the final file
try:
    with open(final_file_name, "w") as final_file:
        final_file.writelines(final_lines)
except IOError as e:
    print(f"Error while writing on the file '{final_file_name}': {e}")