import json


lines = []
with open('alice.txt', mode="r", encoding='utf-8') as file:
    text = file.read().lower()
    text = text.replace(' ', '').replace('\n', '')


character_count = dict()
for character in text:
    if character in character_count:
        character_count[character] += 1
    else:
        character_count[character] = 1

character_count = dict(sorted(character_count.items()))


with open('hw01_output.json', 'w', encoding='utf-8') as json_file:
    json.dump(character_count, json_file, ensure_ascii=False, indent=4)