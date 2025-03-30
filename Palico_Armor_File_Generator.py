import json

# load camps file
p_armor_f = open("Palico_Armor.json", "r")
p_sets = json.load(p_armor_f)
all_sets = []
for rank in list(p_sets.keys()):
    print(p_sets[rank])
    all_sets.extend(list(p_sets[rank].keys()))

# clear out file
out = open("out.txt", 'w+')
out.write('')
out.close()


def generateList():
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
            out.write('|Weapon Name=' + ('None' if p_sets[rank][set_name]['Weapon']['Name'] is None else p_sets[rank][set_name]['Weapon']['Name']) + '\n')
            out.write('|Head Armor Name=' + p_sets[rank][set_name]['Headgear']['Name'] + '\n')
            out.write('|Torso Armor Name=' + p_sets[rank][set_name]['Body Armor']['Name'] + '\n')
            out.write('}}\n')
        out.write('</div>\n')
        out.write('\n')
    out.close()


def generatePage(monster):
    pass


choice = input('Which rank (or all to generate the list of all)? ')
if choice != 'low' and choice != 'high':
    generateList()
else:
    monster = input('which set? ')
    if monster != 'Athos': monster = 'Felyne ' + monster
    if choice == 'high': monster += ' α'

    if monster in all_sets: generatePage(monster)
    else:
        print('set not found: ' + monster)
        print('all available sets are listed here: ')
        print(*all_sets, sep='\n')
