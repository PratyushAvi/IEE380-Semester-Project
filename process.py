import json

filename = input('Enter filename: ')

with open(filename, 'r') as f:
    data = json.loads(f.read())

mean = sum(data)/len(data)
minutes, seconds = int(mean // 60000), round((mean / 1000) % 60, 2)

print(f"Mean song duration: {minutes}m {seconds}s")