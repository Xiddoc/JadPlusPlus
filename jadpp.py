"""
Main file for Jad++
"""
import argparse


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

    # Updating projects to newer APKs
    merge_cmd = subparsers.add_parser('update')
    merge_cmd.add_argument('project_file',
                           type=argparse.FileType(),
                           help='The input project file to use.')
    merge_cmd.add_argument('apk_file',
                           type=argparse.FileType('rb'),
                           help='The new APK to update the project to.')
    merge_cmd.add_argument('out_project_file',
                           type=argparse.FileType('w'),
                           help='The output project file to write to after updating.')

    return parser.parse_args()


def main() -> None:
    args = parse_args()



if __name__ == '__main__':
    main()
