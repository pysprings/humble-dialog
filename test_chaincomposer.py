from chaincomposer import ChainComposer


class MockChainComposerView:
    def __init__(self):
        self.selection = ()
        self.chain = ()

    def set_selection(self, selection):
        self.selection = selection

    def set_chain(self, chain):
        self.chain = chain


class TestChainComposer:
    def test_initialize(self):

        view = MockChainComposerView()
        composer = ChainComposer(view)
        composer.initialize()
        assert len(view.selection) == 1

    def test_select_filter(self):
        view = MockChainComposerView()
        composer = ChainComposer(view)
        composer.initialize()

        composer.add(0)

        assert len(view.chain) == 1
