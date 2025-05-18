import json

items_file = open("itemColors.json", "r")
items = json.load(items_file)
items_file.close()

out_file = open("out.txt", "w+")
out_file.write("")
out_file.close()

out_file = open("out.txt", "a+")

for item in items:
    out_file.write('\t["' + item["Name"] + '"]= {')
    out_file.write('["Icon"]= "' + item["Icon"] + '", ')
    out_file.write('["Color"]= "' + item["Icon Color"] + '", ')
    out_file.write('["OverlayLeft"]= ')
    if item["OverlayLeft"] is None:
        out_file.write('nil, ')
    else:
        out_file.write('"' + item["OverlayLeft"] + '", ')
    out_file.write('["OverlayRight"]= ')
    if item["OverlayRight"] is None:
        out_file.write('nil},')
    else:
        out_file.write('"' + item["OverlayRight"] + '"},')
    out_file.write('\n')

out_file.close()
