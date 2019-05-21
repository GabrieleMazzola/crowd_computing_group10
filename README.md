# Explaining recommendation for groups 

Current code is quite straight forward. Generation of the explanations 
(most important part is in ```generate_explanation.py```) is using ```dictionary.py``` with
predefined phrases. 

Logic of scoring is in scoring.py, however later should be moved to ```scoring_util.py```.
In current implementation Recommender System is expected to return ranking for all POI (Point of Interest).  

We are currently in the need of tests, but should also think of some easy to check tests 
and perhaps some frontend for the final version. 

## Testing ##
You can generate different explanations by setting diferent ```ExplanationType``` based on your needs:

- ```ExplanationType.ANONYMOUS``` fully anononymous to get explanation like "Someone wanted X", "Some members from the group wanted Y"
- ```ExplanationType.ANONYMOUS_GROUP```anononymous with numbers, to get explanation like "5 people wanted X"
- ```ExplanationType.PERSON_ONLY``` only close friends to get explanation like "Adam wanted X", "Eva and Rob wanted Y"
- ```ExplanationType.PERSON_GROUP``` close friends with anonymous to get explanation like "Ana and 3 other people wanted X", "Rob, Ana and 4 other people wanted Y"
