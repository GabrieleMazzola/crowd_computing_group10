import copy

from explanation.dictionary import Dictionary
from explanation.util.satisfaction_util import satisfaction_level
from explanation.scoring import calculate_score
import numpy as np

from explanation.util.score_util import Score


class GenerateExplanation:
    # Sequence has both scenario and ranking retrieved from RS

    MAX_POI_SCORE = 10

    def __init__(self, pois, ratings, people):
        self.scenario = pois
        self.ranking = ratings
        self.max_score = Score.calculate_max_score(len(ratings))
        self.people = people
        self.explanations = {}

    def generate_explanation(self):
        for person in self.people:
            self.generate_personal_explanation(person)

    def generate_personal_explanation(self, person):
        person_scores = Score.calculate_scores(self.ranking, person)
        explanation = ''

        person_score = np.sum(person_scores)
        relative_score = calculate_score(person, self.ranking)

        explanation += self.generate_opening(person.name)
        explanation += self.generate_overall_satisfaction(relative_score)
        explanation += self.generate_negative_explanation(person, person_scores)
        explanation += self.generate_positive_explanation(person)

        self.explanations[person.name] = explanation

    def generate_opening(self, name="X"):
        opening = np.random.choice(Dictionary.BEGIN_END_SENTENCES["intro_hi"])
        opening += name + ', '
        opening += np.random.choice(Dictionary.BEGIN_END_SENTENCES["intro_word"])
        return opening

    def generate_overall_satisfaction(self, relative_score):
        sentiment = satisfaction_level(relative_score)
        sentence = np.random.choice(Dictionary.OPENING_SENTENCES[sentiment])
        sentence += 'the recommended sequence. '
        return sentence

    def generate_negative_explanation(self, person, person_scores):
        sentence = ""
        # take the POI which was ranked the lowest by you
        lowest_score_poi, lowest_score = Score.get_the_lowest_score(person)

        if lowest_score > 5:
            return ""
        else:
            relative_lowest = lowest_score / 10
            sentiment = satisfaction_level(relative_lowest)
            sentence += np.random.choice(Dictionary.OPENING_SENTENCES[sentiment])
            sentence += lowest_score_poi
            sentence += np.random.choice(Dictionary.BEGIN_END_SENTENCES["but_info"])

            other_people = copy.deepcopy(self.people)
            other_people.remove(person)
            other_score, other_person = Score.get_the_highest_other_score_poi(other_people, lowest_score_poi)

            # score of the other person who rated highest POI which was rated lowest by you
            other_sentiment = satisfaction_level(other_score / 10)

            sentence += np.random.choice(Dictionary.OTHERS[other_sentiment]).replace('<<NAMES>>',
                                                                                     other_person)
            sentence += lowest_score_poi + ', '
            sentence += np.random.choice(Dictionary.BEGIN_END_SENTENCES["come_on"]) + '. '

        return sentence

    def generate_positive_explanation(self, person):
        sentence = ''
        highest_score, favorite_item = Score.get_highest_score(person)
        ##
        ## TODO: This indicates that in final ranking may not be all POI. discuss with a group
        # unless points.include?(highest_score.point_of_interest.id)
        sentence += np.random.choice(Dictionary.BEGIN_END_SENTENCES["favorite"]).replace('<<NAME>>', favorite_item)
        sentence += 'and ' + np.random.choice(Dictionary.BEGIN_END_SENTENCES["not_included"])
        sentence += np.random.choice(Dictionary.BEGIN_END_SENTENCES["but_info"])

        other_people = copy.deepcopy(self.people)
        other_people.remove(person)
        other_score, other_person = Score.get_the_lowest_other_score_poi(other_people, favorite_item)
        other_sentiment = satisfaction_level(other_score.score.to_f / 10)

        sentence += np.random.choice(Dictionary.OTHERS[other_sentiment]).replace('<<NAMES>>', other_person)
        sentence += favorite_item.name + ', '
        sentence += np.random.choice(Dictionary.BEGIN_END_SENTENCES["reason_not_included"])
