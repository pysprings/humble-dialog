from chaincomposer import ChainComposer


class MockChainComposerView:
    def __init__(self):
        self.selection = ()

    def set_selection(self, selection):
        self.selection = selection


class TestChainComposer:
    def test_initialize(self):

        view = MockChainComposerView()
        composer = ChainComposer(view)
        composer.initialize()
        assert len(view.selection) == 1
