from explanation.person.person import Person
from explanation.poi.poi import POI
from explanation.generate_explanation import *

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

poi1 = POI("McDonald")
list_pois.append(poi1)
poi2 = POI("Burger King")
list_pois.append(poi2)
poi3 = POI("Pizza")
list_pois.append(poi3)
poi4 = POI("Gelateria")
list_pois.append(poi4)
poi5 = POI("Fagiolata")
list_pois.append(poi5)
poi6 = POI("Taqueria")
list_pois.append(poi6)

print()

p1.poi_ranking = {'McDonald':8, 'Burger King':9, 'Pizza':7, 'Gelateria':6, 'Fagiolata': 6, 'Taqueria':9}
p2.poi_ranking = {'McDonald':9, 'Burger King':7, 'Pizza':7, 'Gelateria':5, 'Fagiolata': 6, 'Taqueria':10}
p3.poi_ranking = {'McDonald':10, 'Burger King':9, 'Pizza':8, 'Gelateria':8, 'Fagiolata': 6, 'Taqueria':6}
p4.poi_ranking = {'McDonald':6, 'Burger King':6, 'Pizza':8, 'Gelateria':9, 'Fagiolata': 10, 'Taqueria':5}
p5.poi_ranking = {'McDonald':6, 'Burger King':9, 'Pizza':10, 'Gelateria':6, 'Fagiolata': 6, 'Taqueria':9}
p6.poi_ranking = {'McDonald':6, 'Burger King':8, 'Pizza':10, 'Gelateria':4, 'Fagiolata': 5, 'Taqueria':7}

# hard-coded
ordered_recommended_pois = [poi3, poi2, poi4, poi1, poi6, poi5]

print("FINAL ORDER")
for index, place in enumerate(ordered_recommended_pois):
    print(f"{index+1}. {place.name}")
print()
ge = GenerateExplanation(pois=list_pois, ratings=ordered_recommended_pois, people=users,
                         explanation_type=ExplanationType.PERSON_ONLY)

ge.generate_explanation()
print()
for key, explanation in ge.explanations.items():
    print(key + " --> " + explanation)




