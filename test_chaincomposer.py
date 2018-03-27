from chaincomposer import ChainComposer


class TestChainComposer:
    def test_initialize(self):

        view = MockChainComposerView()
        composer = ChainComposer(view)
        composer.initialize()
        assert len(view.selection) == 1
