
import json

lis = []

with open ('ptt_0726_s.json', 'r+') as f:
    data = json.load(f)

for i in range(0, len(data)):
    try :
        data[i]['h_推文總數']['推']
    except KeyError:
        continue
    else :
        push = [data[i]['h_推文總數']['推'], i]
        lis.append(push)
        
lis.sort()
lis.reverse()
print(lis)

for i in range (0, len(lis)):
    # print(lis[i][1])
    print(json.dumps(data[lis[i][1]]['h_推文總數'], ensure_ascii = False, indent = 4))

# print(json.dumps(data, ensure_ascii = False, indent = 4))
