def calculate_score(person, poi_list):
    total = 0
    person_preferences_sorted = sorted(person.poi_ranking, key=person.poi_ranking.__getitem__, reverse=True)
    for index_person, place_person in enumerate(person_preferences_sorted):
        for index_chosen, place_chosen in enumerate(poi_list):
            if place_chosen.name == place_person:
                total = total + abs(index_chosen-index_person)
    print(person.name, total)
    return total


def retrieve_personal_score(person, poi):
    return person.poi_ranking[poi.name]
