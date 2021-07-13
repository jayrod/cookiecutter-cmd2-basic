from cmd2 import with_default_category, CommandSet, Statement

@with_default_category('Other Commands')
class FirstCommandSet(CommandSet):

    def __init__(self):
        super().__init__()

    def do_hello(self, _: Statement):
        self._cmd.poutput('Hello')

    def do_world(self, _: Statement):
        self._cmd.poutput('World')
