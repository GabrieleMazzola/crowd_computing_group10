from explanation.person.person import Person
from explanation.poi.poi import POI
from explanation.generate_explanation import *
from explanation.strategy.lm_mp_wm_strategy import LmMpWmStrategy
from explanation.util.util import print_ordered_list


def print_explanations(ge):
    print()
    print(ge.explanation_type, ge.close_people_mode)
    for key, explanation in ge.explanations.items():
        print(key + " --> " + explanation)


users = []

p1 = Person("Stacey")
users.append(p1)
p2 = Person("Nick")
users.append(p2)
p3 = Person("Carolina")
users.append(p3)
p4 = Person("Thomas")
users.append(p4)
p5 = Person("Mike")
users.append(p5)
p6 = Person("Vanessa")
users.append(p6)

for u in users:
    u.add_dummy_relationships(users)

list_pois = []

poi1 = POI("Stadium")
list_pois.append(poi1)
poi2 = POI("Technical Science Museum")
list_pois.append(poi2)
poi3 = POI("HB Brewery")
list_pois.append(poi3)
poi4 = POI("Alte Pinokotech")
list_pois.append(poi4)
poi5 = POI("Eisbach Surfspot")
list_pois.append(poi5)

print()

# STACY
p1.poi_ranking = {'Stadium': 10, 'Technical Museum': 7, 'HB Brewery': 8, 'Alte Pinokotek': 9, 'Eisbach Surfspot': 5}
# NICK
p2.poi_ranking = {'Stadium': 8, 'Technical Museum': 7, 'HB Brewery': 10, 'Alte Pinokotek': 7, 'Eisbach Surfspot': 5}
# CAROLINA
p3.poi_ranking = {'Stadium': 5, 'Technical Museum': 3, 'HB Brewery': 9, 'Alte Pinokotek': 10, 'Eisbach Surfspot': 8}
# THOMAS
p4.poi_ranking = {'Stadium': 5, 'Technical Museum': 10, 'HB Brewery': 9, 'Alte Pinokotek': 6, 'Eisbach Surfspot': 10}
# MIKE
p5.poi_ranking = {'Stadium': 6, 'Technical Museum': 10, 'HB Brewery': 9, 'Alte Pinokotek': 3, 'Eisbach Surfspot': 9}
# VANESSA
p6.poi_ranking = {'Stadium': 10, 'Technical Museum': 9, 'HB Brewery': 8, 'Alte Pinokotek': 10, 'Eisbach Surfspot': 5}

ordered_recommended_pois = LmMpWmStrategy.call(users)

# ORGANIZE RELATIONSHIPS
# Vanessa and Stacy are bffs
p1.add_relationship(p6, Relationship.CLOSE)
p6.add_relationship(p6, Relationship.CLOSE)

# Thomas is good friends with all
for u in users:
    if u.name != "Thomas":
        u.add_relationship(p4, Relationship.CLOSE)
        p4.add_relationship(u, Relationship.CLOSE)

# Thomas and Carolina are a couple
p4.add_relationship(p3, Relationship.ROMANTIC)
p3.add_relationship(p4, Relationship.ROMANTIC)

# Mike and Thomas are bffs ( BROS before hoes!)
p4.add_relationship(p5, Relationship.MOST_IMPORTANT)
p5.add_relationship(p4, Relationship.MOST_IMPORTANT)

print("FINAL ORDER")
for index, place in enumerate(ordered_recommended_pois):
    print(f"{index + 1}. {place.name}")
print()

for u in users:
    print_ordered_list(u)
explanations = [e for e in ExplanationType]
modes = [m for m in ClosePersonMode]
explanations_personalized = [ExplanationType.PERSON_ONLY, ExplanationType.PERSON_GROUP]

for explanation in explanations:
    if explanation in explanations_personalized:
        for mode in modes:
            ge = GenerateExplanation(pois=list_pois, ratings=ordered_recommended_pois, people=users,
                                     explanation_type=explanation, close_people_mode=mode)
            ge.generate_explanation()
            print_explanations(ge)
    else:
        ge = GenerateExplanation(pois=list_pois, ratings=ordered_recommended_pois, people=users,
                                 explanation_type=explanation, close_people_mode=ClosePersonMode.ALL_CLOSE)
        ge.generate_explanation()
        print_explanations(ge)