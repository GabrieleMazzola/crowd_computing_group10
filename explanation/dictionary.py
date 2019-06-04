from explanation.satisfaction.satisfaction import Satisfaction


class Dictionary:
    BEGIN_END_SENTENCES = {
        "but_info": [', Still, ', ', Having said that, ', ', Despite that, '],
        "add_info": ['Additionally, ', 'Furthermore, ', 'Besides, '],
        "plus_to_this": ['As an additional factor, we have also predicted that ',
                         'On top of this, we have also predicted that '],
        "intro_word": ['we have predicted that ', 'we believe that ', 'we think that ', 'our algorithm suggested that '],
        "consider_word": ['You may also consider ', 'You may also take into account'],
        "stubborn_word": ['resolute ', 'adamant ', 'wilful'],
        "come_on": ['so why not give it a chance', 'so it may be fun for you too'],
        "intro_hi": ['Hi there ', 'Thanks for asking ', 'Hello ', 'As you wonder ', 'Hi ', 'Hey ', 'Yoooo '],
        "item": ['this recommendation ', 'this point of interest ', 'our suggestion '],
        "trust_positive_end": ['too ', 'also ', 'as well '],
        "trust_negative_end": ['so you may find something new ', 'and you can normally rely on '],
        "favorite": ['We know <<NAME>> is your favorite ', 'We know you love <<NAME>> ',
                     'We know your top choice has been <<NAME>> '],
        "not_included": ['it is not included in the recommendation'],
        "reason_not_included": ['so it was left out to maximize group satisfaction']
    }

    OPENING_SENTENCES = {
        Satisfaction.VERY_WEAK: ['You are likely to detest ', 'You are likely to not really enjoy '],
        Satisfaction.WEAK: ['You probably will not really like ', 'You will not be really happy with '],
        Satisfaction.INDIFFERENT: ['You will be somewhat okay with ', 'You will be just basically okay with '],
        Satisfaction.MEDIUM: ['You will like ', 'You will enjoy '],
        Satisfaction.STRONG: ['you will highly enjoy ', 'you will be really happy with ', 'you will for sure enjoy ',
                              'you will strongly agree with '],
        Satisfaction.VERY_STRONG: ['You will love ', 'You will cherish ']
    }

    OTHERS = {
        Satisfaction.VERY_WEAK: ['<<NAMES>> will likely to detest ', '<<NAMES>> will likely not really enjoy '],
        Satisfaction.WEAK: ['<<NAMES>> probably will not really like ', '<<NAMES>> will not be really happy with '],
        Satisfaction.INDIFFERENT: ['<<NAMES>> will be somewhat okay with ', '<<NAMES>> will be basically okay with '],
        Satisfaction.MEDIUM: ['<<NAMES>> will like ', '<<NAMES>> will enjoy '],
        Satisfaction.STRONG: ['<<NAMES>> will highly enjoy ', '<<NAMES>> will be really happy with '],
        Satisfaction.VERY_STRONG: ['<<NAMES>> would love to see ', '<<NAMES>> would cherish ']
    }
