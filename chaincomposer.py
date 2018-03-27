class ReverbFilter:
    pass


class ChainComposer:
    def __init__(self, view):
        self.view = view
        self.filters = (ReverbFilter,)

    def initialize(self):
        self.view.set_selection(self.filters)
