import json

# load camps file
p_armor_f = open("Palico_Armor.json", "r")
p_sets = json.load(p_armor_f)
all_sets = []
for rank in list(p_sets.keys()):
    all_sets.extend(list(p_sets[rank].keys()))

# load items file
items_f = open("itemColors.json","r")
items = json.load(items_f)
items_f.close()


def get_item_icon(item_name):
    # return '-', '-'
    for item in items:
        if item['Name'] == item_name:
            return item['Icon'], item['Icon Color']
    return None


# clear out file
out = open("out.txt", 'w+')
out.write('')
out.close()


def generate_list():
    out = open("out.txt", "a+")
    current_rarity = 0
    rarity_div = '<div class=rarity-div>\n'
    table_header = '{{GenericPalicoSetListItem\n|Game=MHWilds\n'
    for rank in list(p_sets.keys()):
        out.write('=' + rank + '=\n')
        for set_name in list(p_sets[rank].keys()):
            if p_sets[rank][set_name]["Rarity"] != current_rarity:
                current_rarity += 1
                if current_rarity != 1 and current_rarity != 5:
                    out.write('</div>\n')
                out.write('==Rarity ' + str(current_rarity) + '==\n')
                out.write(rarity_div)
            out.write(table_header)
            out.write('|Rarity=' + str(current_rarity) + '\n')
            out.write('|Set Name=' + set_name + '\n')
            out.write('|Set Image=MHWilds-' + set_name + ' Armor Palico Render.png\n')
            out.write('|Weapon Name=' + (
                'None' if p_sets[rank][set_name]['Weapon']['Name'] is None else p_sets[rank][set_name]['Weapon'][
                    'Name']) + '\n')
            out.write('|Head Armor Name=' + p_sets[rank][set_name]['Headgear']['Name'] + '\n')
            out.write('|Torso Armor Name=' + p_sets[rank][set_name]['Body Armor']['Name'] + '\n')
            out.write('}}\n')
        out.write('</div>\n')
        out.write('\n')
    out.close()


def generate_page(monster, outpage='out.txt'):
    out = open(outpage, 'w+')
    out.write('')
    out.close()
    out = open(outpage, 'a+')
    out.write('{{GenericNav|MHWilds}}\n\n')
    out.write(
        'The ' + monster + ' set is a set of [[MHWilds/Palico Equipment|Palico Equipment]] in [[Monster Hunter Wilds]].\n')
    out.write('{{GenericPalicoArmorSet\n')
    set_info = p_sets['High Rank' if monster.endswith('Î±') else 'Low Rank'][monster]
    weapon_mats = list(map(lambda x: [x, *get_item_icon(x)], set_info['Weapon']["Forging Materials"]))
    helm_mats = list(map(lambda x: [x, *get_item_icon(x)], set_info['Headgear']["Forging Materials"]))
    body_mats = list(map(lambda x: [x, *get_item_icon(x)], set_info['Body Armor']["Forging Materials"]))
    set_info_key = {'Front Image': 'MHWilds-' + monster + ' Armor Palico.png',
                    'Game': 'MHWilds',
                    'Name': monster,
                    'Rarity': set_info['Rarity'],
                    'Weapon Name':
                        '<!-- No ' + monster + ' Weapon -->'
                        if set_info['Weapon']['Name'] is None
                        else set_info['Weapon']['Name'],
                    'Weapon Attack Type':
                        ''
                        if set_info['Weapon']['Attack Type'] is None
                        else set_info['Weapon']['Attack Type'],
                    'Weapon Defense':
                        ''
                        if set_info['Weapon']['Defense Bonus'] is None
                        else set_info['Weapon']['Defense Bonus'],
                    'Weapon Melee Attack':
                        ''
                        if set_info['Weapon']['Attack']['Melee'] is None
                        else set_info['Weapon']['Attack']['Melee'],
                    'Weapon Affinity':
                        ''
                        if set_info['Weapon']['Affinity'] is None
                        else set_info['Weapon']['Affinity'],
                    'Weapon Ranged Attack':
                        ''
                        if set_info['Weapon']['Attack']['Ranged'] is None
                        else set_info['Weapon']['Attack']['Ranged'],
                    'Weapon Description':
                        ''
                        if set_info['Weapon']['Description'] is None
                        else set_info['Weapon']['Description'],
                    'Weapon Forge Cost':
                        ''
                        if set_info['Required Cost'] is None
                        else str(set_info['Required Cost']) + 'z',
                    'Weapon Ailment Type':
                        ''
                        if set_info['Weapon']['Element'] is None
                           or list(set_info['Weapon']['Element'].keys())[0] == '-'
                        else list(set_info['Weapon']['Element'].keys())[0],
                    'Weapon Ailment Damage':
                        ''
                        if set_info['Weapon']['Element'] is None
                           or list(set_info['Weapon']['Element'].keys())[0] == '-'
                        else set_info['Weapon']['Element'][list(set_info['Weapon']['Element'].keys())[0]],
                    'Weapon Material 1 Name': weapon_mats[0][0] if len(weapon_mats) > 0 else '',
                    'Weapon Material 1 Icon Type': weapon_mats[0][1] if len(weapon_mats) > 0 else '',
                    'Weapon Material 1 Icon Color': weapon_mats[0][2] if len(weapon_mats) > 0 else '',
                    'Weapon Material 1 Quantity': 1 if len(weapon_mats) > 0 else '',
                    'Weapon Material 2 Name': weapon_mats[1][0] if len(weapon_mats) > 1 else '',
                    'Weapon Material 2 Icon Type': weapon_mats[1][1] if len(weapon_mats) > 1 else '',
                    'Weapon Material 2 Icon Color': weapon_mats[1][2] if len(weapon_mats) > 1 else '',
                    'Weapon Material 2 Quantity': 1 if len(weapon_mats) > 1 else '',
                    'Head Name': set_info['Headgear']['Name'],
                    'Head Defense': set_info['Defenses']['Defense'],
                    'Head Fire Res': set_info['Defenses']['Fire Res'],
                    'Head Water Res': set_info['Defenses']['Water Res'],
                    'Head Thunder Res': set_info['Defenses']['Thunder Res'],
                    'Head Ice Res': set_info['Defenses']['Ice Res'],
                    'Head Dragon Res': set_info['Defenses']['Dragon Res'],
                    'Head Description': set_info['Headgear']['Description'],
                    'Head Forge Cost': str(set_info['Required Cost']) + 'z',
                    'Head Material 1 Name': helm_mats[0][0] if len(helm_mats) > 0 else '',
                    'Head Material 1 Icon Type': helm_mats[0][1] if len(helm_mats) > 0 else '',
                    'Head Material 1 Icon Color': helm_mats[0][2] if len(helm_mats) > 0 else '',
                    'Head Material 1 Quantity': 1 if len(helm_mats) > 0 else '',
                    'Head Material 2 Name': helm_mats[1][0] if len(helm_mats) > 1 else '',
                    'Head Material 2 Icon Type': helm_mats[1][1] if len(helm_mats) > 1 else '',
                    'Head Material 2 Icon Color': helm_mats[1][2] if len(helm_mats) > 1 else '',
                    'Head Material 2 Quantity': 1 if len(helm_mats) > 1 else '',
                    'Torso Name': set_info['Body Armor']['Name'],
                    'Torso Defense': set_info['Defenses']['Defense'],
                    'Torso Fire Res': set_info['Defenses']['Fire Res'],
                    'Torso Water Res': set_info['Defenses']['Water Res'],
                    'Torso Thunder Res': set_info['Defenses']['Thunder Res'],
                    'Torso Ice Res': set_info['Defenses']['Ice Res'],
                    'Torso Dragon Res': set_info['Defenses']['Dragon Res'],
                    'Torso Description': set_info['Body Armor']['Description'],
                    'Torso Forge Cost': str(set_info['Required Cost']) + 'z',
                    'Torso Material 1 Name': body_mats[0][0] if len(body_mats) > 0 else '',
                    'Torso Material 1 Icon Type': body_mats[0][1] if len(body_mats) > 0 else '',
                    'Torso Material 1 Icon Color': body_mats[0][2] if len(body_mats) > 0 else '',
                    'Torso Material 1 Quantity': 1 if len(body_mats) > 0 else '',
                    'Torso Material 2 Name': body_mats[1][0] if len(body_mats) > 1 else '',
                    'Torso Material 2 Icon Type': body_mats[1][1] if len(body_mats) > 1 else '',
                    'Torso Material 2 Icon Color': body_mats[1][2] if len(body_mats) > 1 else '',
                    'Torso Material 2 Quantity': 1 if len(body_mats) > 1 else '',
                    }
    format_length = max(map(len, list(set_info_key.keys()))) + 1
    for info in list(set_info_key.keys()):
        if set_info_key[info] != '':
            out.write(('|{:<' + str(format_length) + '}').format(info) + ' = ')
            out.write(str(set_info_key[info]) + '\n')
    out.write('}}\n')
    out.write('[[Category: MHWilds Palico Equipment]]')
    out.close()

choice = input('Which rank (or all to generate the list of all)? ')
if choice == 'every':
    for monster in all_sets:
        outpage = str(monster)
        if outpage.endswith('Î±'):
            outpage = 'p_armor/high/' + outpage[:-3] + '.txt'
        else:
            outpage = 'p_armor/low/' + outpage + '.txt'
        try:
            generate_page(monster, outpage)
        except:
            print("couldn't generate " + monster)
elif choice != 'low' and choice != 'high':
    generate_list()
else:
    monster = input('which set? ')
    if monster != 'Athos': monster = 'Felyne ' + monster
    if choice == 'high': monster += ' Î±'  # for some reason, alpha becomes those symbols

    if monster in all_sets:
        generate_page(monster)
    else:
        print('set not found: ' + monster)
        print('all available sets are listed here: ')
        print(*all_sets, sep='\n')
