
import json

my_csv_file = open('csv_file.txt','r')
csv_content = [lines.strip('\n') for lines in my_csv_file.readlines()]
my_csv_file.close()

csv_content = csv_content[1:]
list_dictionary = []

for items in csv_content:
    items = items.split(',')
    club = items[0]
    city = items[1]
    country = items[2]
    list_dictionary.append({'club': club, 'country': country, 'city': city })

my_json_file = open('json_file.txt','w')
json.dump(list_dictionary,my_json_file)
my_json_file.close()

##[{"club": "Manchester United", "country": "UK", "city": "Manchester"}, {"club": "Real Madrid", "country": "Spain", "city": "Madrid"}, {"club": "Juventus", "country": "Italy", "city": "Turin"}]