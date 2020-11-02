import json

jo = json.loads(open('../../turn_farm/income_info/income_info.json').read())

for j in jo:
    if j['기준면적'] == '평':
        print(j)
