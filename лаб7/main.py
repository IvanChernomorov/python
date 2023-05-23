import xmltodict

def find_schools(dct, schools, schools_types):
    for node in dct:
        name = ''
        school_type = ''
        address = 'unknown'
        if 'tag' in node and isinstance(node['tag'], list):
            for tag in node['tag']:
                if tag['@k'] == 'name':
                    name = tag['@v']
#                 elif tag['@k'] == 'addr:street':
#                     address = tag['@v']
                elif tag['@k'] == 'amenity' and 'school' in tag['@v'].lower():
                    school_type = tag['@v']
            if(name != '' and school_type != ''):
                #schools.append({'name': name, 'address': address})
                schools.append(name)
                schools_types.add(school_type)
    

f = open('2 - 2.osm', 'r', encoding='utf-8')
dct = xmltodict.parse(f.read())

schools = []
schools_types = set()

find_schools(dct['osm']['node'], schools, schools_types)
find_schools(dct['osm']['way'], schools, schools_types)
find_schools(dct['osm']['relation'], schools, schools_types)


for school in sorted(schools):
    print(school)
print(schools_types)



