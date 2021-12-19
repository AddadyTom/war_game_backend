import sys
from getopt import getopt

from config.general import ENV_ARG, COMMAND_LINE_ARGUMENTS, DEFAULT_ENV


class EnvironmentService:
    opts, args = getopt(sys.argv[1:], '', [f'{argument}' for argument in COMMAND_LINE_ARGUMENTS])
    opts = dict(opts)

    @staticmethod
    def get_command_line_argument(arg_name: str) -> str:
        return EnvironmentService.opts[f'--{arg_name}']

    @staticmethod
    def get_environment() -> str:
        try:
            return EnvironmentService.get_command_line_argument(ENV_ARG)
        except KeyError:
            return DEFAULT_ENV

