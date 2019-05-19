from explanation.scoring import calculate_score


class Score:
    MAX_POI_SCORE = 5

    @staticmethod
    def get_the_highest_other_score_poi(people, poi_name):
        curr_highest_score = 0
        curr_highest_person = ""
        for person in people:
            if curr_highest_score < person.poi_ranking[poi_name]:
                curr_highest_score = person.poi_ranking[poi_name]
                curr_highest_person = person.name

        return curr_highest_score, curr_highest_person

    @staticmethod
    def get_the_lowest_other_score_poi(people, poi_name):
        curr_lowest_score = 0
        curr_lowest_person = ""
        for person in people:
            if curr_lowest_score < person.poi_ranking[poi_name]:
                curr_lowest_score = person.poi_ranking[poi_name]
                curr_lowest_person = person.name

        return curr_lowest_score, curr_lowest_person

    @staticmethod
    def get_the_lowest_score(person):
        poi_ranking = person.poi_ranking
        curr_min_poi = ("", 1000)
        for elem in poi_ranking.keys():
            if curr_min_poi[1] > poi_ranking[elem]:
                curr_min_poi = (elem, poi_ranking[elem])

        return curr_min_poi

    @staticmethod
    def get_highest_score(person):
        poi_ranking = person.poi_ranking
        curr_max_poi = ("", 0)
        for elem in poi_ranking.keys():
            if curr_max_poi[1] < poi_ranking[elem]:
                curr_max_poi = (elem, poi_ranking[elem])

        return curr_max_poi

    @staticmethod
    def calculate_max_score(number_of_poi):
        # TODO: Maybe improve a bit that
        return Score.MAX_POI_SCORE * number_of_poi

    @staticmethod
    def calculate_scores(ranking, person):
        score_list = {}
        for poi in ranking:
            score_list[poi.name] = calculate_score(person, poi)
        return score_list
