


class Thing():
    def __init__(self):
        self.corruptable = True
        pass

    ## True encapsulation
    def closure(self):
        private = True

        reader = lambda: private
        def writer(val):
            nonlocal private
            #print(f'private:{private}')
            private = val

        return reader, writer



thing = Thing()
#print(thing)
#print(thing.corruptable)
#thing.corruptable = False
#print(thing.corruptable)

reader, writer = thing.closure()
print(reader())
print(reader())
print(reader())
print(reader())
print(reader())
#
writer(False)
print(reader())
print(reader())
print(reader())





