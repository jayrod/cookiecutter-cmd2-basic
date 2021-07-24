from cmd2 import with_default_category, CommandSet, Statement, Cmd2ArgumentParser, with_argparser
    
    

@with_default_category('Other Commands')
class FirstCommandSet(CommandSet):

    def __init__(self):
        super().__init__()

    def do_hello(self, _: Statement):
        self._cmd.poutput('Hello')


    parser = Cmd2ArgumentParser(description="CHANGE ME")
    parser.add_argument(
        "text", choices_provider=['one', 'two'], help="HELP TEXT"
    )

    @with_argparser(parser)
    def do_world(self, parms: Statement):

        self._cmd.poutput(f'{parms.text}')
