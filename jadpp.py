"""
Main file for Jad++
"""
import argparse

from cmd_handlers.handler_factory import handle_command, get_handler

LOGO = """
┏┳   ┓  ╻   ╻ 
 ┃┏┓┏┫ ━╋━ ━╋━
┗┛┗┻┗┻  ╹   ╹  """


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="A tool to add a few extra features to Jadx projects.")

    subparsers = parser.add_subparsers(title='Jad++ Actions',
                                       dest='command',
                                       required=True,
                                       help='The command/action to perform.')

    # Merging projects
    merge_cmd = subparsers.add_parser('merge')
    merge_cmd.add_argument('project_files',
                           type=argparse.FileType(),
                           nargs='+',
                           help='The JadX project files to merge together.')
    merge_cmd.add_argument('out_project_file',
                           type=argparse.FileType('w'),
                           help='The output project file to write to after merging.')

    # Updating projects to newer APKs
    update_cmd = subparsers.add_parser('update')
    update_cmd.add_argument('project_file',
                            type=argparse.FileType(),
                            help='The input project file to use.')
    update_cmd.add_argument('apk_file',
                            type=argparse.FileType('rb'),
                            help='The new APK to update the project to.')
    update_cmd.add_argument('out_project_file',
                            type=argparse.FileType('w'),
                            help='The output project file to write to after updating.')

    return parser.parse_args()


def print_header_text() -> None:
    print(LOGO)
    print("Brought to you @ https://github.com/Xiddoc/JadPlusPlus/\n")


def main() -> None:
    args = parse_args()

    try:
        print_header_text()

        print(f"Processing {args.command} operation...")
        handler = get_handler(args)
        handle_command(handler, args)
        print("Done!")

    except ValueError as exc:
        print(f"\nJad++ encountered an error: {exc}")


if __name__ == '__main__':
    main()
