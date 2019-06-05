class Score:
    MAX_POI_SCORE = 10

    @staticmethod
    def get_the_highest_other_score_poi(people, poi_name):
        curr_highest_score = 0
        highest_people = []

        for person in people:
            if curr_highest_score < person.poi_ranking[poi_name]:
                curr_highest_score = person.poi_ranking[poi_name]
                highest_people = [person.name]

            if curr_highest_score == person.poi_ranking[poi_name]:
                highest_people.append(person.name)

        return curr_highest_score, highest_people

    @staticmethod
    def get_the_lowest_other_score_poi(people, poi_name):
        curr_lowest_score = 300
        lowest_people = []
        for person in people:
            if curr_lowest_score > person.poi_ranking[poi_name]:
                curr_lowest_score = person.poi_ranking[poi_name]
                lowest_people = [person.name]

            if curr_lowest_score == person.poi_ranking[poi_name]:
                lowest_people.append(person.name)

        return curr_lowest_score, lowest_people

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
        score_list = []
        for poi in ranking:
            score_list.append(Score.retrieve_personal_score(person, poi))
        return score_list

    @staticmethod
    def calculate_score(person, poi_list):
        total = 0
        person_preferences_sorted = sorted(person.poi_ranking, key=person.poi_ranking.__getitem__, reverse=True)
        for index_person, place_person in enumerate(person_preferences_sorted):
            for index_chosen, place_chosen in enumerate(poi_list):
                if place_chosen.name == place_person:
                    total = total + abs(index_chosen - index_person)
        return total

    @staticmethod
    def retrieve_personal_score(person, poi):
        return person.poi_ranking[poi.name]