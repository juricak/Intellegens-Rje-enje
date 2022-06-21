class Family:
    def __init__(self, familyname, father, mother, children):
        self.familyname = familyname
        self.father = father
        self.mother = mother
        self.children = children

    def toString(self):
        numberofchildren = len(self.children)
        chi = []
        for child in self.children:
            chi.append(child)
        if numberofchildren > 1:
            chi.insert(-1,'and')
        chistr = ' '.join(chi)
        result = 'In the ' + self.familyname + ' family Mother ' + self.mother + ' and Father ' + self.father + ' have ' + str(numberofchildren) + ' children:\n' +  chistr
        return result
