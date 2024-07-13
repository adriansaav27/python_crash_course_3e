favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
 }

people = [names for names in favorite_languages.keys()]
people.append('willy')
people.append('georgy')

for name in people:
    poll = favorite_languages.get(name, 'none')
    if poll == 'none':
        print(f'{name.title()}, you have to do the survey')
    else:
        print(f'{name.title()}, you already have the survey done')