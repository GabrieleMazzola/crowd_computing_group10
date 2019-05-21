class Person:

    # sorted ranking of points
    poi_ranking = {}
    relationships = {}
    # TODO: implement the relationship as defined in the end

    def __init__(self, name):
        self.name = name
    def __eq__(self,obj):
        return self.name == obj.name