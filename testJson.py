import json


with open('data.json', 'r') as openfile:
    # Reading from json file
    json_object = json.load(openfile)


data = {}
count = 0
#saves the desired data into the data dict
for dataSet in json_object['data']:
    if(dataSet["sites"] == []):
        continue
    elif(dataSet['sites'][0] == []):
        continue
    else:
        teams = dataSet['teams']
        odds = dataSet['sites'][0]['odds']['h2h']
        time = dataSet['commence_time']

        data[tuple(teams)] = tuple([odds, time])

#print(json_object['data'][0]['sites'][0]['odds'])
    
#print(json_object['data'][0]['id'])
print()
print(type(json_object))
print()
print(data)

