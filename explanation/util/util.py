# Just print the list of preferences of a person in descending order
from explanation.person.close_person_mode import ClosePersonMode
from explanation.person.relationship import Relationship


def print_ordered_list(person):
    ordered_list = sorted(person.poi_ranking, key=person.poi_ranking.__getitem__, reverse=True)
    to_print = person.name + ' -- > '
    for index, place in enumerate(ordered_list):
        to_print += place
        to_print += ':'
        to_print += str(person.poi_ranking[place])
        to_print += ' '
    print(to_print)


def is_last():
    return True


def is_last_but_one(num_all_people, close_person_list_length, i):
    return not (0 < i < close_person_list_length - 1 or i < num_all_people - 1)


def are_more_distant(num_all_people, close_person_list_length):
    return num_all_people - close_person_list_length > 0


def prepare_close_people(target_person, person_name_list, mode=ClosePersonMode.ALL_CLOSE):
    included_relationship_types = [Relationship.MOST_IMPORTANT]
    if mode == ClosePersonMode.ALL_CLOSE:
        included_relationship_types.append(Relationship.CLOSE)
        included_relationship_types.append(Relationship.ROMANTIC)
    if mode == ClosePersonMode.ONLY_ROMANTIC:
        included_relationship_types.append(Relationship.ROMANTIC)
    if mode == ClosePersonMode.ONLY_CLOSE:
        included_relationship_types.append(Relationship.CLOSE)

    close_people = [person for person in person_name_list if
                    target_person.relationships[person] in included_relationship_types]
    return list(set(close_people)), len(person_name_list) - len(close_people)


def create_label_person_group(close_person_list, num_all_people):
    final_label = ""

    for i in range(len(close_person_list)):
        person_name = close_person_list[i]

        if not is_last_but_one(num_all_people, len(close_person_list), i):
            final_label += ", "

        if is_last_but_one(num_all_people, len(close_person_list), i) and not are_more_distant(num_all_people, len(
                close_person_list)):
            final_label += " and "

        final_label += person_name

    if are_more_distant(num_all_people, len(close_person_list)) and len(close_person_list) > 0:
        final_label += " and "

    final_label += create_label_anonymous_group(num_all_people)

    return final_label


def create_label_person_only(close_person_list, distant_people_num):
    people_word_label = ""
    if len(close_person_list) > 1:
        people_word_label = " and "

    if distant_people_num > 1:
        people_word_label += str(distant_people_num) + " other people from a group"
    elif distant_people_num > 0:
        people_word_label += str(distant_people_num) + " other person from a group"

    return (",").join(close_person_list) + people_word_label


def create_label_anonymous(num_all_people):
    if num_all_people > 1:
        return "some people from the group"
    return "someone from the group"


def create_label_anonymous_group(num_all_people):
    if num_all_people > 1:
        return str(num_all_people) + " people from the group"
    return "one person from the group"


def find_person_by_name(people_list, person_name):
    for person in people_list:
        if person.name == person_name:
            return person
