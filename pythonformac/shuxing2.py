class party:
    number = 0
    def __init__(self,name):
        party.number += 1
        self.name = name
        print('join a person called %s' % self.name)
    def __del__(self):
        party.number += -1
        if party.number == 0:
            print('There is only one person here.')
        else:
            print('We have %d person here.' % party.number)
    def sayhi(self):
        print('hi I am %s' % self.name)
    def howmany(self):
        print('here are %d' % self.number)
        
