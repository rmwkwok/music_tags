import os
import re
import sys
import music_tag
import argparse
from tabulate import tabulate

SUPPORTED_FILE_NAME = re.compile(
    f"^(.*)\-(.*)\.(.*)$", # <artist_name>-<music_name>.<ext>
)

def main(folder: str) -> None:
    '''Main function.

    Args:
    folders: str
        Path to the music folder.
    '''
    for root, subdirs, files in os.walk(folder):
        items = []

        for file in files:
            items.append({
                'file': file,
                'supported': False,
            })
            file_name_check = SUPPORTED_FILE_NAME.search(file)
            if file_name_check:
                try:
                    tags = music_tag.load_file(os.path.join(root, file))
                    items[-1].update({
                        'tags': tags,
                        'cur_artist_name': str(tags['artist']),
                        'cur_music_title': str(tags['title']),
                        # New artist name and title are retrieved from
                        # the filename.
                        'new_artist_name': file_name_check.group(1),
                        'new_music_title': file_name_check.group(2),
                        'supported': True
                    })
                except:
                    pass

        # Keep only items changable
        items = enumerate(filter(_is_changable, items), start=1)
        items = [dict(item, index=index) for index, item in items]

        # Make decisions
        _decisions(root, items)

def _is_changable(item: dict) -> bool:
    '''Check whether an item is changable. It is changable if the file
    is in a supported format and either the file's artist name tag or
    title tag is different from that retrieved from the file name.

    Args:
    items: dict
        An item.

    Returns:
    bool. Whether the item is changable.
    '''
    return item['supported'] and (
        (item['cur_artist_name'] != item['new_artist_name']) or
        (item['cur_music_title'] != item['new_music_title'])
    )

def _print_table(items: list[dict]) -> None:
    '''Pretty print changable items.

    Args:
    items: list[dict]
        List of changable items.
    '''
    items = [
        [
            item['index'],
            item['file'],
            f"'{item['cur_artist_name'] or '<EMPTY>'}' -> '{item['new_artist_name']}'",
            f"'{item['cur_music_title'] or '<EMPTY>'}' -> '{item['new_music_title']}'",
        ] for item in items
    ]

    print(tabulate(
        items,
        headers=['#', 'file', 'artist', 'title'],
        colalign=('left', 'left', 'right', 'right'),
    ))

def _decisions(root: str, items: list[dict]) -> None:
    '''Prompt user for reviewing proposed changes and ask for actions.

    Args:
    root: str
        Subfolder.
    items: list[dict]
        List of changable items.
    '''
    if items:
        print(f"\nFolder: {root}")
        _print_table(items)

        match input(
            '\n'
            'Apply the above change? '
            'y: yes to all. n: no to all. d: decide one by one. q:quit.'
            '\n'
            'y/n/d/q ?: '
        ):
            case 'n':
                pass
            case 'q':
                print('Quitting...')
                sys.exit(0)
            case 'd':
                for item in items:
                    _decisions(root, [item])
            case 'y':
                for item in items:
                    item['tags']['artist'] = item['new_artist_name']
                    item['tags']['title'] = item['new_music_title']
                    item['tags'].save()
            case _:
                print('Invalid option.')
                _decisions(root, items)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=(
            '''Recursively go through supported files in a folder, '''
            '''write artist name and music title into the file's metadata. '''
            '''Supported filename is "<artist_name>-<music_name>.<ext>". '''
        )
    )
    parser.add_argument(
        'folder',
        type=str,
        help='Folder to recursively go through the supported files.'
    )
    args = parser.parse_args()
    main(args.folder)