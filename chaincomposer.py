class ReverbFilter:
    pass


class ChainComposer:
    def __init__(self, view):
        self.view = view
        self.filters = (ReverbFilter,)
        self.chain = ()

    def initialize(self):
        self.view.set_selection(self.filters)

    def add(self, index):
        self.chain = self.chain + (self.filters[index],)
        self.view.set_chain(self.chain)
