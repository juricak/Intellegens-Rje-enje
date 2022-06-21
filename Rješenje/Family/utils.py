from Family.Family import Family
from Family.Person import Person


def parseFamilies(string):

    familyPersons = string.split(',')

    persons = []

    for i in range(len(familyPersons)):
        person = familyPersons[i].strip()
        params = person.split(' ')
        if len(params)==2:
            persons.append(Person(params[-1], params[-2], None))
        elif len(params)==3:
            persons.append(Person(params[-1], params[-2], params[-3]))
        else:
            message = print('Malformed input, check input values!')
            return message

    uniqueLastName = []

    for person in persons:
        if person.lastname not in uniqueLastName:
            uniqueLastName.append(person.lastname)

    families = []

    for familyName in uniqueLastName:
        children = []
        mother = 'MISSING!'
        father = 'MISSING!'
        for person in persons:
            if person.lastname == familyName:
                if person.title == 'Mrs.':
                    mother = person.firstname
                elif person.title == 'Mr.':
                    father = person.firstname
                else:
                    children.append(person.firstname)
        try:
            families.append(Family(familyName, father, mother, children))
        except Exception as e:
            print(e)
    return families
