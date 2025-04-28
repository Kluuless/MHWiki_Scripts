import json

items_file = open('TU1_Items.json','r')
items = json.load(items_file)
items_file.close()

out_file = open('out.txt','w+')
out_file.close()


def generate_table_entries():
    out_file = open('out.txt', 'a+')

    item_header = '|-\n'
    for item in items:
        out_file.write(item_header)
        out_file.write('| {{GenericItemLink|MHWilds|' +
                       item['Name'] + '|' +
                       item['Icon'] + '|' +
                       item['Icon Color'] + '}}\n')
        out_file.write('| ' + item['Rarity'] + '\n')
        out_file.write('| ' + item['Sell Price'] + 'z\n')
        out_file.write('| ' + item['Description'] + '\n\n')

    out_file.close()


page_content_header = '''{{GenericNav|MHWilds}}
<br>
{{MHWildsInfobox\n'''
page_content_footer = '''}}

=Crafting Recipes=
{| class="wikitable" style="text-align:center;"
! Number !! Result !! !! Material A !! !! Material B
|-
|}
=Sources=
==Quests==
<div class="threecol" style="clear:both;">
<div>
</div>
</div>
==Monsters==
<div class="threecol">
<div>
</div>
</div>
==Gathering <ref>[[User:Cola|Cola's]] interactive MHWilds map (https://c-ola.github.io/wildsmap/)</ref>==
<div class="threecol">
<div>
</div>
</div>
==Other==
=Forging=
==Weapons==
<div class="threecol">
<div>
</div>
</div>
==Armor==
<div class="threecol">
<div>
</div>
</div>
[[Category:MHWilds Items]]'''
unknown = '???'
invalid = '-'


def generate_page(item_name):
    item_file_name = 'items/' + item_name + '.txt'
    item_file = open(item_file_name, 'w+')
    item_file.close()

    item_file = open(item_file_name, 'a+')
    for item in items:
        if item['Name'] == item_name:
            item_file.write(page_content_header)
            item_file.write('|English Name = ' + replace_if_none(item, 'Name', unknown) + '\n')
            item_file.write('|Japanese Name = ' + replace_if_none(item, 'Japanese Name', unknown) + '\n')
            item_file.write('|Type = ' + replace_if_none(item, 'Category', unknown) + '\n')
            item_file.write('|Image = ' + 'MHWilds-' + replace_if_none(item, 'Icon', unknown) + ' Icon ' + replace_if_none(item, 'Icon Color', unknown) + '.png\n')
            item_file.write('|Description = ' + replace_if_none(item, 'Description', unknown) + '\n')
            item_file.write('|Rarity = ' + replace_if_none(item, 'Rarity', unknown) + '\n')
            item_file.write('|Price = ' + replace_if_none(item, 'Sell Price', invalid) + '\n')
            item_file.write('|Carry Limit = ' + replace_if_none(item, 'Carry Limit', invalid) + '\n')
            item_file.write(page_content_footer)
    item_file.close()


def replace_if_none(dict, key, replace=''): return replace if key not in list(dict.keys()) else dict[key]


def generate_all_pages():
    for item in items:
        item_file_name = 'items/' + item['Name'] + '.txt'
        item_file = open(item_file_name, 'w+')
        item_file.close()

        item_file = open(item_file_name, 'a+')
        item_file.write(page_content_header)
        item_file.write('|English Name = ' + replace_if_none(item, 'Name', unknown))
        item_file.write('|Japanese Name = ' + replace_if_none(item, 'Japanese Name', unknown))
        item_file.write('|Type = ' + replace_if_none(item, 'Category', unknown))
        item_file.write('|Image = ' + 'MHWilds-' + replace_if_none(item, 'Icon', unknown) + ' Icon ' + replace_if_none(item, 'Icon Color', unknown) + '.png')
        item_file.write('|Description = ' + replace_if_none(item, 'Description', unknown))
        item_file.write('|Rarity = ' + replace_if_none(item, 'Rarity', unknown))
        item_file.write('|Price = ' + replace_if_none(item, 'Sell Price', invalid))
        item_file.write('|Carry Limit = ' + replace_if_none(item, 'Carry Limit', invalid))
        item_file.write(page_content_footer)
        item_file.close()


choice = input("Generate table entries ('table'), specific item page ('page'), or all item pages ('all')? ")
if choice == 'page':
    item_choice = input("Which item? ")
    item_names = list(map(lambda x: x['Name'], items))
    if item_choice not in item_names:
        print('Item not found. The following names are accepted:')
        print(*item_names, sep='\n')
    else:
        generate_page(item_choice)
elif choice == 'all':
    generate_all_pages()
else:
    generate_table_entries()