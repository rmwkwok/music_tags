
# Music tag writer for artist names and music titles

------

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

------

## About the project

This program retrieves the artist name and the music title from the file name, and write them to the file's corresponding tags.

1. Filename format: "\<artist_name>-\<music_name>.\<ext>"
2. Supported file formats: refer to [music-tag][musictag-url]

The program will recursively go through all subfolders in "/path/to/folder". For each subfolder, it lists all changable files for review and action ([example](#example)).

Criteria for changable file:

1. In supported file format, and
2. Either the tag's artist or title is different from that retrieved from the filename.

Actions:

1. y - apply changes to all files in the list
2. n - skip all changes to files in the list
3. d - review the changes file-by-file
4. q - quit the program
5. other answers are invalid and the same list will be reviewed again

## Tested environment

![python][python-shield]

## Download and use

1. Clone this repo

```
git clone https://github.com/rmwkwok/music_tags.git
cd music_tags
```

2. (Optional) Setup and activate virtual environment

```
virtualenv music_tags_venv
source music_tags_venv/bin/activate
```

3. Install requirements
```
pip install -r requirements.txt
```

4. Run the program
```
python main.py /path/to/folder
```

## Example

```
$ python3 main.py /path/to/folder

Folder: /path/to/folder/album
#    file                                artist                   title
---  ------------------  ----------------------  ----------------------
1    Artist1-Title1.mp3    Artist1 -> 'Artist1'  asodjWOEHF -> 'Title1'
2    Artist1-Title2.mp3  hfechf8ea -> 'Artist1'     &#H#&#H -> 'Title2'
3    Artist2-Title3.mp3    SD&AD(# -> 'Artist2'      title3 -> 'Title3'

Apply the above change? y: yes to all. n: no to all. d: decide one by one. q:quit.
y/n/d/q ?:
```

![](https://github.com/rmwkwok/music_tags/blob/main/image/music_tags_change.png?raw=true)


[contributors-shield]: https://img.shields.io/github/contributors/rmwkwok/music_tags.svg?style=for-the-badge
[contributors-url]: https://github.com/rmwkwok/music_tags/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/rmwkwok/music_tags.svg?style=for-the-badge
[forks-url]: https://github.com/rmwkwok/music_tags/network/members
[stars-shield]: https://img.shields.io/github/stars/rmwkwok/music_tags.svg?style=for-the-badge
[stars-url]: https://github.com/rmwkwok/music_tags/stargazers
[issues-shield]: https://img.shields.io/github/issues/rmwkwok/music_tags.svg?style=for-the-badge
[issues-url]: https://github.com/rmwkwok/music_tags/issues
[license-shield]: https://img.shields.io/github/license/rmwkwok/music_tags.svg?style=for-the-badge
[license-url]: https://github.com/rmwkwok/music_tags/blob/main/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/rmwkwok
[python-shield]: https://img.shields.io/badge/python-3.10.12-blue.svg?style=for-the-badge
[musictag-url]: https://pypi.org/project/music-tag/