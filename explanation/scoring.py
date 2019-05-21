def calculate_score(person, poi_list):
    total = 0
    for index_person, place_person in enumerate(person.poi_ranking):
        for index_chosen, place_chosen in enumerate(poi_list):
            tmp = place_chosen.name
            if place_chosen.name == place_person:
                total = total + abs(index_chosen-index_person)
    return 1/(total + 1)

def retrieve_personal_score(person, poi):
    return person.poi_ranking[poi.name]
