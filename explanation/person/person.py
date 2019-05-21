from explanation.person.closeness import Closeness


class Person:

    def __init__(self, name):
        self.poi_ranking = {}
        self.relationships = {}
        self.name = name

    def __eq__(self, obj):
        return self.name == obj.name

    def add_relationship(self, person, closeness_level=Closeness.VERY_CLOSE):
        self.relationships[person.name] = closeness_level

    def add_dummy_relationships(self, people):
        for person in people:
            self.add_relationship(person)
