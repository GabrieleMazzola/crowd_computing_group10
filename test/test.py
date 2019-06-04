from explanation.person.person import Person
from explanation.poi.poi import POI
from explanation.generate_explanation import *
from explanation.strategy.lm_mp_wm_strategy import LmMpWmStrategy

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
p1.poi_ranking = {'Stadium': 10, 'Technical Museum': 3, 'HB Brewery': 8, 'Alte Pinokotek': 9, 'Eisbach Surfspot': 5}
# NICK
p2.poi_ranking = {'Stadium': 8, 'Technical Museum': 5, 'HB Brewery': 10, 'Alte Pinokotek': 7, 'Eisbach Surfspot': 5}
# CAROLINA
p3.poi_ranking = {'Stadium': 7, 'Technical Museum': 3, 'HB Brewery': 9, 'Alte Pinokotek': 10, 'Eisbach Surfspot': 8}
# THOMAS
p4.poi_ranking = {'Stadium': 5, 'Technical Museum': 10, 'HB Brewery': 9, 'Alte Pinokotek': 6, 'Eisbach Surfspot': 10}
# MIKE
p5.poi_ranking = {'Stadium': 6, 'Technical Museum': 10, 'HB Brewery': 9, 'Alte Pinokotek': 4, 'Eisbach Surfspot': 9}
# VANESSA
p6.poi_ranking = {'Stadium': 10, 'Technical Museum': 9, 'HB Brewery': 8, 'Alte Pinokotek': 10, 'Eisbach Surfspot': 5}

ordered_recommended_pois = LmMpWmStrategy.call(users)
# hard-coded
# ordered_recommended_pois = [poi3, poi2, poi4, poi1, poi5]

print("FINAL ORDER")
for index, place in enumerate(ordered_recommended_pois):
    print(f"{index + 1}. {place.name}")
print()
ge_po = GenerateExplanation(pois=list_pois, ratings=ordered_recommended_pois, people=users,
                            explanation_type=ExplanationType.PERSON_ONLY)

ge_pg = GenerateExplanation(pois=list_pois, ratings=ordered_recommended_pois, people=users,
                            explanation_type=ExplanationType.PERSON_GROUP)
ge_a = GenerateExplanation(pois=list_pois, ratings=ordered_recommended_pois, people=users,
                           explanation_type=ExplanationType.ANONYMOUS)
ge_ag = GenerateExplanation(pois=list_pois, ratings=ordered_recommended_pois, people=users,
                            explanation_type=ExplanationType.ANONYMOUS_GROUP)

ge_po.generate_explanation()
ge_pg.generate_explanation()
ge_a.generate_explanation()
ge_ag.generate_explanation()

print()
for key, explanation in ge_po.explanations.items():
    print(key + " --> " + explanation)

print()
for key, explanation in ge_pg.explanations.items():
    print(key + " --> " + explanation)
print()
for key, explanation in ge_a.explanations.items():
    print(key + " --> " + explanation)
print()
for key, explanation in ge_ag.explanations.items():
    print(key + " --> " + explanation)
