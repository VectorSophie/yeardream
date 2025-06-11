import json

def create_dict(filename):
    with open(filename) as file:
        json_string = file.read()
        
        return json.loads(json_string)
    
def create_json(dictionary, filename):
    with open(filename, 'w') as file:

        return json.dump(dictionary, file)

src = 'netflix.json'
dst = 'new_netflix.json'

netflix_dict = create_dict(src)
print('원래 데이터: ' + str(netflix_dict))

netflix_dict['Dark Knight'] = 39217
create_json(netflix_dict, dst)
updated_dict = create_dict(dst)
print('수정된 데이터: ' + str(updated_dict))