def calculate_score(person, poi):
    # TODO: MATTEO magics
    return len(person.poi_ranking)- person.poi_ranking.index(poi.name)