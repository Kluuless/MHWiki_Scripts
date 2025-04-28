import json

out_file = open('out.txt','w+')
out_file.write('')
out_file.close()

item_file = open('itemColors.json', 'r')
items = json.load(item_file)
item_file.close()


def get_icon(item_name):
    for item in items:
        if item['Name'] == item_name:
            return item["Icon"]
    return ''


def get_color(item_name):
    for item in items:
        if item['Name'] == item_name:
            return item["Icon Color"]
    return ''


skill_icon_file = open('skill_icons.json', 'r')
skill_icons = json.load(skill_icon_file)
skill_icon_file.close()

talisman_file = open('Talismans.csv', 'r')
out_file = open('out.txt', 'w+')

out_file.write('{| class="wikitable wide sortable mw-collapsible" style="text-align:center; white-space:normal;"\n')
header = talisman_file.readline().split(',')


def get_attr_name(t: list, a: str):
    #print(t, t.index(a))
    return header[t.index(a)]


for talisman_attr in header:
    if talisman_attr == 'Skill Name':
        out_file.write('! Skills Granted\n')
    elif talisman_attr == 'Forging Price':
        out_file.write('! Forging Cost\n')
    elif talisman_attr == 'Skill Pts.' or talisman_attr.startswith('Forg'):
        pass
    else:
        out_file.write('! ' + talisman_attr + '\n')
out_file.write('|-\n')

while True:
    talisman = talisman_file.readline().split(',')
    if len(talisman) <= 1:
        out_file.write('|}\n')
        out_file.close()
        talisman_file.close()
        break
    else:
        line = ''
        for talisman_attr in talisman:
            if get_attr_name(talisman, talisman_attr) == 'Name':
                line = '| <L>GenericArmorLink|MHWilds|' + talisman_attr + '|Talisman|{0}|' + talisman_attr + '<R>\n'
            elif get_attr_name(talisman, talisman_attr) == 'Rarity':
                line += '| ' + talisman_attr + '\n'
                line = line.format(talisman_attr)
            elif get_attr_name(talisman, talisman_attr) == 'Description':
                line += '| ' + talisman_attr + '\n'
            elif get_attr_name(talisman, talisman_attr) == 'Skill Name':
                line += '| <L>MHWildsSkillLink|' + talisman_attr + '|' + skill_icons[talisman_attr] + '<R> x{0}\n'
            elif get_attr_name(talisman, talisman_attr) == 'Skill Pts.':
                line = line.format(talisman_attr)
            elif get_attr_name(talisman, talisman_attr) == 'Forging Price':
                line += '| ' + talisman_attr + 'z'
            elif get_attr_name(talisman, talisman_attr).rstrip().endswith('Qty'):
                line = line.format(talisman_attr.rstrip())
            else:
                line += ('<br>\n<L>GenericItemOverlay|MHWilds|' + talisman_attr + '|' + get_icon(talisman_attr) + '|' +
                         get_color(talisman_attr) + '<R> x{0}')
        out_file.write(line.replace('<L>', '{{').replace('<R>', '}}'))
        out_file.write('\n\n|-\n')
print('done')
