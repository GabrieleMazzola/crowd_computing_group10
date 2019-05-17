class Dictionary:
  BEGIN_END_SENTENCES = {
    "but_info": [', Still, ', ', Having said that, ', ', Despite that, '],
    "add_info": ['Additionally, ', 'Furthermore, ', 'Besides, '],
    "plus_to_this": ['As an additional factor, we have also predicted that ',
                   'On top of this, we have also predicted that '],
    "intro_word": ['We have predicted that ', 'We believe that '],
    "consider_word": ['You may also consider ', 'You may also take into account'],
    "stubborn_word": ['resolute ', 'adamant ', 'wilful'],
    "come_on": ['so why not give it a chance', 'so it may be fun for you too'],
    "intro_hi": ['Hi there ', 'Thanks for asking ', 'Hello, ', 'As you wonder '],
    "item": ['this recommendation ', 'this point of interest ', 'our suggestion '],
    "trust_positive_end": ['too ', 'also ', 'as well '],
    "trust_negative_end": ['so you may find something new ', 'and you can normally rely on '],
    "favorite": ['We know <<NAME>> is your favorite ', 'We know you love <<NAME>> '],
    "not_included": ['it is not included in the recommendation '],
    "reason_not_included": ['so it was left out to maximize group satisfaction']
  }

  OPENING_SENTENCES = {
    "very_weak": ['You are likely to detest ', 'You are likely to not really enjoy '],
    "weak": ['You probably will not really like ', 'You will not be really happy with '],
    "indifferent": ['You will be somewhat okay with ', 'You will be just basically okay with '],
    "medium": ['You will like ', 'You will enjoy '],
    "strong": ['You will highly enjoy ', 'You will be really happy with '],
    "very_strong": ['You will love ', 'You will cherish ']
  }

  OTHERS = {
    "very_weak": ['<<NAMES>> will likely to detest ', '<<NAMES>> will likely not really enjoy '],
    "weak": ['<<NAMES>> probably will not really like ', '<<NAMES>> will not be really happy with '],
    "indifferent": ['<<NAMES>> will be somewhat okay with ', '<<NAMES>> will be basically okay with '],
    "medium": ['<<NAMES>> will like ', '<<NAMES>> will enjoy '],
    "strong": ['<<NAMES>> will highly enjoy ', '<<NAMES>> will be really happy with '],
    "very_strong": ['<<NAMES>> would love to see ', '<<NAMES>> would cherish ']
  }
