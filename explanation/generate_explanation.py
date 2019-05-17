class GenerateExplanation:

    # output :explanations
    # attr_accessor :explanations,
    #               :max_score,
    #               :points,
    #               :people,
    #               :person,
    #               :person_name,
    #               :person_score,
    #               :points,
    #               :relative_score,
    #               :scenario
    # Sequence has both scenario and ranking retrieved from RS

    def  __init__(self, sequence, people):
        self.scenario = sequence["scenario"]
        self.ranking = sequence["ranking"]
        self.max_score = len(sequence["ranking"]) * 10
        self.people = people

    def generate_explanation(self):
        for person in self.people:
            self.generate_personal_explanation(person)

    def calculate_scores(self,person):
        # iterate over pois in ranking
        # for each poi compare ranking

    def generate_personal_explanation(self, person):
        person_scores = Score.where(person: person, point_of_interest: points)
        explanation = ''

        person_score = person_scores.sum( &:score)
        relative_score = person_score.to_f / max_score

        explanation += generate_opening(name: person.name)
        explanation += generate_overall_satisfaction(relative_score: relative_score)
        explanation += generate_negative_explanation(person: person)
        explanation += generate_positive_explanation(person: person)

        explanations[person.name] = explanation

    end

    def generate_opening(name: 'person')
        opening = Dictionary::BEGIN_END_SENTENCES[:intro_hi].sample
        opening += name + ', '
        opening + Dictionary::BEGIN_END_SENTENCES[:intro_word].sample.downcase

    end

    def generate_overall_satisfaction(relative_score:)
        sentiment = satisfaction_level(relative_score)
        sentence = Dictionary::OPENING_SENTENCES[sentiment].sample.downcase
        sentence + 'the recommended sequence. '

    end

    def generate_negative_explanation(person:)
        sentence = ''
        lowest_score = Score.where(person: person, point_of_interest: points).order('score ASC').first
        if lowest_score.score > 5
            ''
        else
            relative_lowest = lowest_score.score.to_f / 10
            sentiment = satisfaction_level(relative_lowest)
            sentence += Dictionary::OPENING_SENTENCES[sentiment].sample
            sentence += lowest_score.point_of_interest.name
            sentence += Dictionary::BEGIN_END_SENTENCES[:but_info].sample.downcase

            other_score = Score.where.
            not (person: person)
            .where(point_of_interest: lowest_score.point_of_interest)
            .order('score DESC')
            .first
        other_sentiment = satisfaction_level(other_score.score.to_f / 10)

        sentence += Dictionary::OTHERS[other_sentiment].sample.gsub('<<NAMES>>', other_score.person.name)
        sentence += lowest_score.point_of_interest.name + ', '
        sentence += Dictionary::BEGIN_END_SENTENCES[:come_on].sample + '. '

    end
    sentence


end


def generate_positive_explanation(person:)
    sentence = ''
    highest_score = Score.where(person: person).order('score DESC').first
    favorite_item = highest_score.point_of_interest

    unless
    points.include?(highest_score.point_of_interest.id)
    sentence += Dictionary::BEGIN_END_SENTENCES[:favorite].sample.gsub('<<NAME>>', favorite_item.name)
    sentence += 'and ' + Dictionary::BEGIN_END_SENTENCES[:not_included].sample
    sentence.strip!
    sentence += Dictionary::BEGIN_END_SENTENCES[:but_info].sample.downcase

    other_score = Score.where.
    not (person: person).where(point_of_interest: favorite_item).order('score ASC').first
    other_sentiment = satisfaction_level(other_score.score.to_f / 10)

    sentence += Dictionary::OTHERS[other_sentiment].sample.gsub('<<NAMES>>', other_score.person.name)
    sentence += favorite_item.name + ', '
    sentence += Dictionary::BEGIN_END_SENTENCES[:reason_not_included].sample.downcase


end

sentence
end


def satisfaction_level(score)
    case
    score
    when
    0.00.
    .0
    .17
    :very_weak


when
0.17.
.0
.34
:weak
when
0.34.
.0
.51
:indifferent
when
0.51.
.0
.68
:medium
when
0.68.
.0
.85
:strong
else
:very_strong
end
end
end
end
