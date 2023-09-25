"""
Not exactly a factory, more of a switch case.

Executes the relevant handler based on the selected command.
"""
import argparse
from typing import Callable, Dict

from cmd_handlers import merge_handler

HandlerFunction = Callable[[argparse.Namespace], None]

COMMANDS: Dict[str, HandlerFunction] = {
    'merge': merge_handler.merge_handler,
}


def get_handler(args: argparse.Namespace) -> HandlerFunction:
    """
    Searches for the proper handler function that matches the arguments given through the command line.
    """
    for command, handler in COMMANDS.items():
        if args.command == command:
            return handler

    raise ValueError(f"Argument {args.command} could not be processed for some reason.")


def handle_command(handler: HandlerFunction, args: argparse.Namespace) -> None:
    """
    Sends the arguments off to the relevant handler, based on the command.

    :param handler: The function to operate on the input arguments.
    :param args: The parsed command line arguments.
    """
    handler(args)
