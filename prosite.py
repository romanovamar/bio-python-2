import re

# K-[KR]-C-G-H-[LMQR] pattern from prosite


def active_site_search(file):

    with open(file) as file:
        string = file.read()
    pattern = 'K(K|R)CGH(L|M|Q|R)'
    match = re.search(pattern, string)
    start = match.start()
    return f'Isocitrate_lyase P28240 contains its active site PS00161  starting from  {start}th position: {match.group()}'


# print(active_site_search('Isocitrate_lyase'))
