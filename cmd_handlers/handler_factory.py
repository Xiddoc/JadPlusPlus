"""
Not exactly a factory, more of a switch case.

Executes the relevant handler based on the selected command.
"""
import argparse

from cmd_handlers import merge_handler

COMMANDS = {
    'merge': merge_handler.merge_handler,
}


def handle_command(args: argparse.Namespace) -> None:
    """
    Sends the arguments off to the relevant handler, based on the command.

    :param args: The parsed command line arguments.
    """

    for command, handler in COMMANDS.items():
        if args.command == command:
            handler(args)
            return

    raise ValueError(f"Argument {args.command} could not be processed for some reason.")
