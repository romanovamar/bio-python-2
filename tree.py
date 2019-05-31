import json


tree = json.loads('[{"name": "B", "parents": ["A", "C"]}, '
                  '{"name": "C", "parents": ["A"]}, '
                  '{"name": "A", "parents": []}, '
                  '{"name": "D", "parents":["C", "F"]}, '
                  '{"name": "E", "parents":["D"]}, '
                  '{"name": "F", "parents":[]}]')


def get_childs(parent):
    childs = {parent}
    for child in parents_dict[parent]:
        if child != parent:
            childs.update(get_childs(child))
    return childs


tree = {d['name']: d['parents'] for d in tree}
parents_dict = {child: {child, } for child in tree}

for child, parents in tree.items():
    for parent in parents:
        parents_dict[parent].add(child)

for parent in sorted(parents_dict):
    print(f'{parent} : {len(get_childs(parent))}')
