from collections import defaultdict
import pprint

yankees_1927 = [
    {'position': 'P', 'name': 'Walter Beall'},
    {'position': 'C', 'name': 'Benny Bengough'},
    {'position': 'C', 'name': 'Pat Collins'},
    {'position': 'OF', 'name': 'Earle Combs'},
    {'position': '3B', 'name': 'Joe Dugan'},
    {'position': 'OF', 'name': 'Cedric Durst'},
    {'position': '3B', 'name': 'Mike Gazella'},
    {'position': '1B', 'name': 'Lou Gehrig'},
    {'position': 'P', 'name': 'Joe Giard'},
    {'position': 'C', 'name': 'Johnny Grabowski'},
    {'position': 'P', 'name': 'Waite Hoyt'},
    {'position': 'SS', 'name': 'Mark Koenig'},
    {'position': '2B', 'name': 'Tony Lazzeri'},
    {'position': 'OF', 'name': 'Bob Meusel'},
    {'position': 'P', 'name': 'Wilcy Moore'},
    {'position': '2B', 'name': 'Ray Morehart'},
    {'position': 'OF', 'name': 'Ben Paschal'},
    {'position': 'P', 'name': 'Herb Pennock'},
    {'position': 'P', 'name': 'George Pipgras'},
    {'position': 'P', 'name': 'Dutch Ruether'},
    {'position': 'OF', 'name': 'Babe Ruth'},
    {'position': 'P', 'name': 'Bob Shawkey'},
    {'position': 'P', 'name': 'Urban Shocker'},
    {'position': 'P', 'name': 'Myles Thomas'},
    {'position': '3B', 'name': 'Julie Wera'}
]

dict_position_list = defaultdict(list)
for line in yankees_1927:
    dict_position_list[line["position"]].append(line["name"])

pprint.pprint(dict_position_list)