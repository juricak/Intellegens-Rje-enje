from Family.Person import Person
from Family.Family import Family

def parseFamilies(string):

    familyPersons = string.split(',')

    persons = []

    for i in range(len(familyPersons)):
        person = familyPersons[i].strip()
        params = person.split(' ')
        if len(params)==2:
            persons.append(Person(params[-1], params[-2], None))
        else:
            persons.append(Person(params[-1], params[-2], params[-3]))

    uniqueLastName = []

    for person in persons:
        if person.lastname not in uniqueLastName:
            uniqueLastName.append(person.lastname)

    families = []

    for familyName in uniqueLastName:
        children = []
        for person in persons:
            if person.lastname == familyName:
                if person.title == None:
                    children.append(person)
                elif person.title == 'Mr.':
                    father = person
                else:
                    mother = person
        families.append(Family(familyName, father, mother, children)) 

    return families