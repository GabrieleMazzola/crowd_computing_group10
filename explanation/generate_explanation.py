import copy

from explanation.dictionary import Dictionary
from explanation.explanation_type import ExplanationType
from explanation.person.closeness import Closeness
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

        relative_lowest = lowest_score / 10
        sentiment = satisfaction_level(relative_lowest)
        sentence += np.random.choice(Dictionary.OPENING_SENTENCES[sentiment])
        sentence += lowest_score_poi
        sentence += np.random.choice(Dictionary.BEGIN_END_SENTENCES["but_info"])

        other_people = copy.deepcopy(self.people)
        other_people.remove(person)
        other_score, other_person = Score.get_the_highest_other_score_poi(other_people, lowest_score_poi)

        other_person = self.possibly_anonymize_person(other_person)

        # score of the other person who rated highest POI which was rated lowest by you
        other_sentiment = satisfaction_level(other_score / 10)

        sentence += np.random.choice(Dictionary.OTHERS[other_sentiment]).replace('<<NAMES>>',
                                                                                 other_person)
        sentence += lowest_score_poi + ', '
        sentence += np.random.choice(Dictionary.BEGIN_END_SENTENCES["come_on"]) + '. '

        return sentence


def generate_positive_explanation(self, person):
    sentence = ''
    favorite_item, highest_score = Score.get_highest_score(person)
    ##
    ## TODO: This indicates that in final ranking may not be all POI. discuss with a group
    # unless points.include?(highest_score.point_of_interest.id)
    sentence += np.random.choice(Dictionary.BEGIN_END_SENTENCES["favorite"]).replace('<<NAME>>', favorite_item)
    sentence += 'and ' + np.random.choice(Dictionary.BEGIN_END_SENTENCES["not_included"])
    sentence += np.random.choice(Dictionary.BEGIN_END_SENTENCES["but_info"])

    other_people = copy.deepcopy(self.people)
    other_people.remove(person)
    other_score, other_person = Score.get_the_lowest_other_score_poi(other_people, favorite_item)
    other_sentiment = satisfaction_level(float(other_score) / 10)

    other_person = self.possibly_anonymize_person(other_person)

    sentence += np.random.choice(Dictionary.OTHERS[other_sentiment]).replace('<<NAMES>>', other_person)
    sentence += favorite_item + ', '
    sentence += np.random.choice(Dictionary.BEGIN_END_SENTENCES["reason_not_included"])

    return sentence


def possibly_anonymize_person(self, target_person, person_name_list, explanation_type=ExplanationType.ANONYMOUS):
    close_person_list, num_distant_people = self.prepare_close_people(target_person, person_name_list)
    num_all_people = len(person_name_list)

    if explanation_type == ExplanationType.ANONYMOUS:
        if num_all_people > 1:
            return "Some people from the group"
        return "Someone from the group"

    if explanation_type == ExplanationType.ANONYMOUS_GROUP:
        if num_all_people > 1:
            return str(num_all_people) + " people from the group"
        return "One person from the group"
    if explanation_type == ExplanationType.PERSON_ONLY:
        return self.create_label_person_group(close_person_list, num_distant_people, person_only=True)

    # Lastly create explanation having both close persons and anonymized not close ones
    return self.create_label_person_group(close_person_list, num_distant_people, person_only=False)


def prepare_close_people(self, target_person, person_name_list):
    close_people = [person for person in person_name_list if
                    target_person.relationships[person] == Closeness.VERY_CLOSE]
    return close_people, len(person_name_list) - len(close_people)


def create_label_person_group(self, close_person_list, distant_people_num, person_only=False):
    people_word_label = ""

    if len(close_person_list) > 0:
        people_word_label = "and "

    if distant_people_num > 1:
        people_word_label += str(distant_people_num) + " other people"
    else:
        people_word_label += str(distant_people_num) + " other person"

    if not person_only:
        return close_person_list.join(",") + people_word_label

    final_label = ""

    if person_only:
        for i in range(len(close_person_list)):
            person_name = close_person_list[i]

            if 0 < i < len(close_person_list) - 1:
                final_label += ", "

            if i == len(close_person_list) - 1:
                final_label += " and "

            final_label += person_name
        return final_label
