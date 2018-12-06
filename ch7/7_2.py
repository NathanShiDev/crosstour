class Filter:
    def init(self):
        self.blocked = []

    def filter(self, sequence):
        return [x for x in sequence if x not in self.blocked]


class SPAMFilter(Filter):
    def init(self):
        self.blocked = ['SPAM']


f = Filter()
f.init()
data = f.filter([1, 2, 3])
print(data)

s = SPAMFilter()
s.init()
data = s.filter(['SPAM', 'SPAM', 'SPAM', 'eggs', 'bacon', 'SPAM'])
print(data)


print('SPAM is the sub class of Filter:', issubclass(SPAMFilter, Filter))
print(SPAMFilter.__bases__, 'is the supper class of SPAM')
print('s is the instance of SPAM', isinstance(s, SPAMFilter))
print('s is the instance of Filter', isinstance(s, SPAMFilter))
print('s is the instance of', s.__class__)
