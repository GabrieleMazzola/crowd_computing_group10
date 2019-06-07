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
    included_relationship_types = []
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
    if num_all_people - len(close_person_list) == 0:
        return create_label_person_only(close_person_list, num_all_people)

    if len(close_person_list) == 0:
        return create_label_anonymous_group(num_all_people)

    to_return_label = ""
    for i, close_person in enumerate(close_person_list):
        to_return_label += close_person
        if i == len(close_person_list)-1:
            to_return_label += " and "
        else:
            to_return_label += ", "

    return to_return_label + create_label_anonymous_group(num_all_people - len(close_person_list))


def create_label_person_only(close_person_list, distant_people_num):
    if len(close_person_list) == 0:
        return create_label_anonymous(len(close_person_list) + distant_people_num)

    to_return_label = ""

    for i, close_person in enumerate(close_person_list):
        to_return_label += close_person
        if if_last_but_one(close_person_list, i):
            to_return_label += " and "
        elif i < len(close_person_list) - 2:
            to_return_label += ", "
    return to_return_label


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


def if_last_but_one(label_list, i):
    return i == len(label_list) - 2
