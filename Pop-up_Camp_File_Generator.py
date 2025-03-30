import json

# load camps file
camps_f = open("Pop-up_Camps.json", "r")
camps = json.load(camps_f)
costs = camps['Camp Costs']

# clear out file
out = open("out.txt", 'w+')
out.write('')
out.close()


# page version #1: table
def ver1_table():
    table_header = '''{| class="wikitable wide sortable mw-collapsible" style="text-align:center; white-space:normal"
    ! colspan=6 | <h4 style="margin:0ox;">[['''
    column_headers = ''']] Pop-Up Camps</h4>
    |-
    !Camp Name
    !Area
    !Safety Level
    !Cost
    !Map Location
    !Picture
    '''

    out = open("out.txt", "a+")
    for map in list(camps.keys())[1:]:
        out.write(table_header + map + column_headers)
        for camp in camps[map]:
            out.write('\n|-\n')
            out.write('| ' + camp["Name"] + '\n')
            out.write('| ' + str(camp["Area"]) + '\n')
            out.write('| ' + camp["Safety Level"] + '\n')
            out.write('| ' + str(costs[camp["Safety Level"]]) + '\n')
            image_uri_code = map + '_' + camp["Name"] + str(camp["Area"])
            image_uri_code = image_uri_code.replace(" ", "_")
            out.write('| [[File:' + image_uri_code + '_map.png]]\n')
            out.write('| [[File:' + image_uri_code + '_pic.png]]\n')
        out.write('\n|}\n\n<br>\n\n')
    out.close()


# page version #2: sections
def ver2_sections():
    out = open("out.txt", "a+")
    for map in list(camps.keys())[1:]:
        out.write('=[[' + map + ']] Pop-up Camp Locations=\n\n')
        for camp in camps[map]:
            out.write('==Area ' + str(camp["Area"]) + ': ' + camp["Name"] + '==\n')
            out.write('\'\'\'Safety Level: ' + camp["Safety Level"] + ' (' + str(costs[camp["Safety Level"]]) + ' pts)\'\'\'\n')
            image_uri_code = map + '_' + camp["Name"] + str(camp["Area"])
            image_uri_code = image_uri_code.replace(" ", "_")
            out.write('<div class=show-on-mobile>\n')
            out.write('  <div class=full-width>[[File:' + image_uri_code + '_map.png|Map Location]]</div>\n')
            out.write('  <div class=full-width>[[File:' + image_uri_code + '_pic.png|Pop-up Camp Picture]]</div>\n')
            out.write('</div>\n')
            out.write('<div class=hide-on-mobile>\n')
            out.write('  <div class=half-width>[[File:' + image_uri_code + '_map.png|Map Location]]</div>\n')
            out.write('  <div class=half-width>[[File:' + image_uri_code + '_pic.png|Pop-up Camp Picture]]</div>\n')
            out.write('</div>\n\n<br>\n')
        out.write('<br>\n')
    out.close()


def ver3_table2():
    table_header = '''{| class="wikitable wide sortable mw-collapsible" style="text-align:center; white-space:normal"
! colspan=4 | <h4 style="margin:0ox;">[['''
    column_headers = ''']] Pop-Up Camps</h4>
|-
!Camp Name
!Area
!Safety Level
!Cost
'''

    out = open("out.txt", "a+")
    for map in list(camps.keys())[1:]:
        out.write(table_header + map + column_headers)
        for camp in camps[map]:
            out.write('\n|-\n')
            out.write('| ' + camp["Name"] + '\n')
            out.write('| ' + str(camp["Area"]) + '\n')
            out.write('| ' + camp["Safety Level"] + '\n')
            out.write('| ' + str(costs[camp["Safety Level"]]) + '\n')
            out.write('|-\n')
            out.write('|colspan=4|<gallery heights=200 mode=packed-hover>\n')
            image_uri_code = map + '_' + camp["Name"] + str(camp["Area"])
            image_uri_code = image_uri_code.replace(" ", "_")
            out.write('File:' + image_uri_code + '_map.png|Map Location\n')
            out.write('File:' + image_uri_code + '_pic.png|Pop-up Camp Picture\n')
            out.write('</gallery>\n')
        out.write('\n|}\n\n<br>\n\n')
    out.close()


def ver4_sections2():
    out = open("out.txt", "a+")
    for map in list(camps.keys())[1:]:
        out.write('==[[' + map + ']] Pop-up Camp Locations==\n\n')
        for camp in camps[map]:
            out.write('===Area ' + str(camp["Area"]) + ': ' + camp["Name"] + '===\n')
            out.write('Safety Level: ' + camp["Safety Level"] + ' (' + str(costs[camp["Safety Level"]]) + ' pts)\n')
            image_uri_code = map + '_' + camp["Name"] + str(camp["Area"])
            image_uri_code = image_uri_code.replace(" ", "_")
            out.write('<gallery heights=200 mode=packed-hover>\n')
            out.write('File:' + image_uri_code + '_map.png|Map Location\n')
            out.write('File:' + image_uri_code + '_pic.png|Pop-up Camp Picture\n')
            out.write('</gallery>\n\n')
    out.close()


option = input('table or sections? ')
if option == 'table':
    ver1_table()
elif option == "table2":
    ver3_table2()
elif option == "sections2":
    ver4_sections2()
else:
    ver2_sections()
