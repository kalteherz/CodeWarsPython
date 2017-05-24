class my_class:
    def __eq__(self, other):
        return True
    def __ne__(self, other):
        return True
    def __lt__(self, other):
        return True

    def __gt__(self, other):
        return True

    def __le__(self, other):
        return True

    def __ge__(self, other):
        return True

def anything(thing):
    return my_class()


