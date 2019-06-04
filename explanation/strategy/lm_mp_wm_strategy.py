from explanation.poi.poi import POI


class LmMpWmStrategy:
    THRESHOLD = 4
    STRATEGY = 'Least Misery + Most Pleasure + Without Misery'

    @staticmethod
    def call(people_list):
        least_misery_list = LmMpWmStrategy.without_misery(people_list)

        # TODO: add most pleasure and least misery

        return least_misery_list

    @staticmethod
    def without_misery(people_list):
        final_list_poi_names = list(people_list[0].poi_ranking.keys())
        for person in people_list:
            for key, value in person.poi_ranking.items():
                if value < LmMpWmStrategy.THRESHOLD and key in final_list_poi_names:
                    final_list_poi_names.remove(key)

        final_list_poi_names = set(final_list_poi_names)

        return_list = [POI(name) for name in final_list_poi_names]

        return return_list
