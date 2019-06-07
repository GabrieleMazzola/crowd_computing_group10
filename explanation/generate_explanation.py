import copy

from explanation.explanations.dictionary import Dictionary
from explanation.explanations.explanation_type import ExplanationType
from explanation.person.close_person_mode import ClosePersonMode
from explanation.person.relationship import Relationship
from explanation.util.satisfaction_util import satisfaction_level, satisfaction_level_user
import numpy as np

from explanation.util.score_util import Score
from explanation.util.util import prepare_close_people, create_label_person_group, create_label_person_only, \
    create_label_anonymous_group, create_label_anonymous, find_person_by_name


class GenerateExplanation:
    # Sequence has both scenario and ranking retrieved from RS

    MAX_POI_SCORE = 10
    SATISFACTION_CONF_LEVEL = 2

    def __init__(self, pois, ratings, people, explanation_type, close_people_mode):
        self.scenario = pois
        self.ranking = ratings
        self.max_score = Score.calculate_max_score(len(ratings))
        self.people = people
        self.explanations = {}
        self.explanation_type = explanation_type
        self.close_people_mode = close_people_mode

    def generate_explanation(self):
        for person in self.people:
            self.generate_personal_explanation(person)

    def generate_personal_explanation(self, person):
        person_scores = Score.calculate_scores(self.ranking, person)
        explanation = ''

        person_score = np.sum(person_scores)
        relative_score = Score.calculate_score(person, self.ranking)

        explanation += self.generate_opening(person.name)
        explanation += self.generate_overall_satisfaction(relative_score)
        explanation += self.generate_negative_explanation(person, person_scores)
        explanation += self.generate_positive_explanation(person)

        self.explanations[person.name] = explanation

    def generate_opening(self, name="X"):
        opening = np.random.choice(Dictionary.BEGIN_END_SENTENCES["intro_hi"])
        opening += name + ', '
        opening += np.random.choice(Dictionary.BEGIN_END_SENTENCES["intro_word"]).lower()
        return opening

    def generate_overall_satisfaction(self, relative_score):
        sentiment = satisfaction_level_user(relative_score, len(self.ranking), len(self.scenario))
        sentence = np.random.choice(Dictionary.OPENING_SENTENCES[sentiment]).lower()
        sentence += 'the recommended sequence. '
        return sentence

    def generate_negative_explanation(self, person, person_scores):
        sentence = ""

        other_people = copy.deepcopy(self.people)
        other_people.remove(person)

        # take the POI which was ranked the lowest by you
        lowest_score_poi, lowest_score = Score.get_the_lowest_score(person)

        ranking_strings = [elem.name for elem in self.ranking]

        if lowest_score_poi in ranking_strings:
            if lowest_score > 6:
                return ""

            relative_lowest = lowest_score / 10
            sentiment = satisfaction_level(relative_lowest)

            person_label = "You"

            if self.explanation_type == ExplanationType.PERSON_ONLY or self.explanation_type == ExplanationType.PERSON_GROUP:
                other_people_label = self.add_close_people_opinion(person, other_people, lowest_score_poi)
                person_label += other_people_label

            sentence += np.random.choice(Dictionary.OPENING_SENTENCES[sentiment]).replace("You", person_label)
            sentence += lowest_score_poi

            sentence += np.random.choice(Dictionary.BEGIN_END_SENTENCES["but_info"]).lower()

            other_score, other_person = Score.get_the_highest_other_score_poi(other_people, lowest_score_poi)

            other_person = self.possibly_anonymize_person(person, other_person)

            # score of the other person who rated highest POI which was rated lowest by you
            other_sentiment = satisfaction_level(other_score / 10)

            sentence += np.random.choice(Dictionary.OTHERS[other_sentiment]).replace('<<NAMES>>',
                                                                                     other_person)
            sentence += lowest_score_poi + ', '
            sentence += np.random.choice(Dictionary.BEGIN_END_SENTENCES["come_on"]).lower() + '. '

        return sentence

    def generate_positive_explanation(self, person):
        sentence = ''
        favorite_item, highest_score = Score.get_highest_score(person)

        # say something in the case some place is not included
        ranking_strings = [elem.name for elem in self.ranking]

        if favorite_item not in ranking_strings:
            sentence += np.random.choice(Dictionary.BEGIN_END_SENTENCES["favorite"]).replace('<<NAME>>', favorite_item)
            sentence += 'and ' + np.random.choice(Dictionary.BEGIN_END_SENTENCES["not_included"])
            sentence += np.random.choice(Dictionary.BEGIN_END_SENTENCES["but_info"]).lower()

            other_people = copy.deepcopy(self.people)
            other_people.remove(person)
            other_score, other_person = Score.get_the_lowest_other_score_poi(other_people, favorite_item)
            other_sentiment = satisfaction_level(float(other_score) / 10)

            other_person = self.possibly_anonymize_person(person, other_person)

            sentence += np.random.choice(Dictionary.OTHERS[other_sentiment]).replace('<<NAMES>>', other_person)
            sentence += favorite_item + ', '
            sentence += np.random.choice(Dictionary.BEGIN_END_SENTENCES["reason_not_included"]) + "."

        return sentence

    def possibly_anonymize_person(self, target_person, person_name_list):
        close_person_list, num_distant_people = prepare_close_people(target_person, person_name_list,
                                                                     self.close_people_mode)
        num_all_people = len(person_name_list)

        if self.explanation_type == ExplanationType.ANONYMOUS_GROUP:
            return create_label_anonymous_group(num_all_people)

        if self.explanation_type == ExplanationType.PERSON_ONLY:
            return create_label_person_only(close_person_list, num_distant_people)

        # Lastly create explanation having both close persons and anonymized not close ones
        if self.explanation_type == ExplanationType.PERSON_GROUP:
            return create_label_person_group(close_person_list, num_all_people)

        return create_label_anonymous(num_all_people)

    def add_close_people_opinion(self, person, people_list, item_name):
        person_name_list = [p.name for p in people_list]
        close_person_list, num_distant_people = prepare_close_people(person, person_name_list,
                                                                     self.close_people_mode)
        final_label = ""
        label_list = []

        for close_person_name in close_person_list:
            close_person = find_person_by_name(people_list, close_person_name)
            candidate_label = self.add_close_person_opinion(person, close_person, item_name)
            if candidate_label is not "":
                label_list.append(candidate_label)

        if len(label_list) == 1:
            final_label += " and "

        if len(label_list) > 1:
            final_label += ", "

        for i, label in enumerate(label_list):
            if i < len(label_list) - 2:
                final_label += ", "
            if i < len(label_list) - 1:
                final_label += "and"
            final_label += label

        return final_label

    def add_close_person_opinion(self, person, close_person, item_name):
        person_sentiment = satisfaction_level(person.poi_ranking[item_name] / 10)
        close_person_sentiment = satisfaction_level(close_person.poi_ranking[item_name] / 10)
        if abs(close_person_sentiment.value - person_sentiment.value) < self.SATISFACTION_CONF_LEVEL:
            return close_person.name
        return ""
