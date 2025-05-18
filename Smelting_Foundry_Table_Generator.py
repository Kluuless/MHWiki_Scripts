import json

points_file = open("smelting_foundry_points.json", "r")
points = json.load(points_file)
points_file.close()

icons_file = open("itemColors.json", "r")
icons = json.load(icons_file)
icons_file.close()

out_file = open("out.txt", "w+")
out_file.write("")
out_file.close()

out_file = open("out.txt", "a+")


def get_icon(item):
    for monster_part in icons:
        if monster_part["Name"] == item:
            return monster_part["Icon"], monster_part["Icon Color"]
    return None


for part in points:
    out_file.write('| {{IconPickerUniversalAlt|MHWilds|')
    icon_dets = get_icon(part["Material"])
    if icon_dets is None:
        print(part)
    out_file.write(icon_dets[0] + '|')
    out_file.write(part["Material"] + '|')
    out_file.write("Color=" + icon_dets[1] + "}}\n")
    out_file.write("| " + str(part["Points"]))
    out_file.write(" pt")
    if part["Points"] > 1:
        out_file.write("s")
    out_file.write("\n|-\n")

out_file.close()