# Just print the list of preferences of a person in descending order

def print_ordered_list(person):
    ordered_list = sorted(person.poi_ranking, key=person.poi_ranking.__getitem__, reverse=True)
    to_print = person.name + ' -- > '
    for index, place in enumerate(ordered_list):
        to_print += place
        to_print += ':'
        to_print += str(person.poi_ranking[place])
        to_print += ' '
    print(to_print)