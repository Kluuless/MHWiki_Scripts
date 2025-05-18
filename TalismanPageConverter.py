from json import load

numerals = ('O', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII')


def convert_page_to_json():
    in_file = open('TalismanPage.txt', 'r')
    charms = {}
    charm = 'INVALID CHARM NAME'
    level = 0
    line = in_file.readline()
    while line != '':
        if line.startswith('| {{GenericArmorLink'):
            charm_name = line[29:line.find('|Talisman')]
            if charm_name.startswith(charm):
                level += 1
            else:
                charm = charm_name[:charm_name.find('Charm')-1]
                level = 0
                charms[charm] = {}
                charms[charm]['Skills'] = []
            charms[charm][level] = {}
            charms[charm][level]['Name'] = charm_name
            charms[charm][level]['Rarity'] = line[line.find('Talisman|') + 9]
            in_file.readline()
            skill = in_file.readline()
            skill = skill[21:skill.find('|', 23)]
            if skill not in charms[charm]['Skills']:
                charms[charm]['Skills'].append(skill)
            charms[charm][level]['Cost'] = int(in_file.readline()[2:-6])
            charms[charm][level]['Materials'] = []
            line = in_file.readline()
            while line.startswith('{{IconPickerOverlayAlt'):
                charms[charm][level]['Materials'].append({
                    'Material': line[line.find('(MHWilds)|') + 10:line.find('|Color=')],
                    'Amount': int(line[line.find('}} x') + 4:line.find('<br>')])
                    }
                )
                line = in_file.readline()
        else:
            line = in_file.readline()
    in_file.close()
    return charms


def convert_json_to_page(charms):
    out_file = open('out.txt', 'w+')
    out_file.write('')
    out_file.close()

    items_file = open('itemColors.json', 'r')
    items = load(items_file)
    items_file.close()

    def get_icon(item_name):
        for monster_part in items:
            if monster_part["Name"] == item_name:
                return monster_part["Icon"], monster_part["Icon Color"], monster_part["OverlayLeft"], monster_part["OverlayRight"]
        return None

    skills_file = open('skill_icons.json', 'r')
    skills = load(skills_file)
    skills_file.close()

    out_file = open('out.txt', 'a+')
    out_file.write('''{{#css:
}}
Link back to user page: [[User:Kluuless]]

{| class="wikitable wide" style="text-align:center; white-space:normal;"
! Name, <br class="show-on-mobile">Skills Granted
! Forging Cost
|-
''')

    for charm_type in charms.keys():
        out_file.write('| ' + charm_type + ' Charm<br>')
        out_file.write('{{Dropdown')
        for level in charms[charm_type].keys():
            charm = charms[charm_type][level]
            if level != 'Skills':
                out_file.write('|Level ' + str(int(level)+1))
                out_file.write('|{{GenericArmorLink|MHWilds|' + charm['Name'] + '|Talisman|' +
                               str(charm['Rarity']) + '|' + charm['Name'] + '}}')
                out_file.write(' <br class<nowiki>=</nowiki>"show-on-mobile">')
                out_file.write('Cost: <span style<nowiki>=</nowiki>"color:#E6C445">' + str(charm["Cost"]) + 'z</span>')
                for mat in charm['Materials']:
                    item = get_icon(mat['Material'])
                    out_file.write('<br>{{IconPickerUniversalAlt|MHWilds|' + item[0] + '|' + mat['Material'] +
                                   '|Color=' + item[1])
                    if item[2] is not None:
                        out_file.write('|TL=' + item[2])
                    if item[3] is not None:
                        out_file.write('|TR=' + item[3])
                    out_file.write('}} x' + str(mat['Amount']))
        charm_id = charm_type.lower().replace(' ', '-').replace("'",'')
        out_file.write('|id=' + charm_id + '}}')
        for skill in charms[charm_type]['Skills']:
            out_file.write('<br>{{MHWildsSkillLink|' + skill + '|' + skills[skill] + '}}')
        out_file.write('\n| {{Dropdown|id=' + charm_id + '|dest=yes}}\n')
        out_file.write('\n|-\n')
    out_file.write('\n|}\n')


convert_json_to_page(convert_page_to_json())
