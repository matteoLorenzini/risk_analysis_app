import re

files = [
    'c:/Users/matte/Repo/risk_analysis_app/data/templates/http%3A%2F%2Fwww.researchspace.org%2Fresource%2FResourceContentInsert.html',
    'c:/Users/matte/Repo/risk_analysis_app/data/templates/http%3A%2F%2Fwww.researchspace.org%2Fresource%2FResourceContentEditE18.html'
]

for p in files:
    with open(p, 'r', encoding='utf-8') as f:
        content = f.read()

    # Scales replace
    old_str = '{ ?event base:P39i_was_measured_by ?m .'
    new_str = '{ fix.pysubject base:P31i_was_modified_by ?event . ?event a base:E5_Event ; base:P39i_was_measured_by ?m .'
    
    # NARA replace
    old_nara1 = '{ ?analysis a base:E89_Propositional_Object ; base:P2_has_type <https://w3id.org/sirius/nara-grid> ; base:P129_is_about fix.pysubject ; base:P148_has_component ?va . ?va a base:E89_Propositional_Object ; base:P129_is_about fix.pysubject ;'
    new_nara1 = '{ fix.pysubject base:P129i_is_subject_of ?analysis, ?va . ?analysis a base:E89_Propositional_Object ; base:P2_has_type <https://w3id.org/sirius/nara-grid> ; base:P148_has_component ?va . ?va a base:E89_Propositional_Object ;'

    # Ensure python replaces literal $
    new_str = new_str.replace('fix.py', '$')
    old_nara1 = old_nara1.replace('fix.py', '$')
    new_nara1 = new_nara1.replace('fix.py', '$')

    content = content.replace(old_str, new_str)
    content = content.replace(old_nara1, new_nara1)
    
    with open(p, 'w', encoding='utf-8') as f:
        f.write(content)

print('Done')
