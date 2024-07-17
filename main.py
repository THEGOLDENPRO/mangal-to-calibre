#!/usr/bin/python

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Dict

import json
import shutil
from pathlib import Path
from argparse import ArgumentParser
from subprocess import check_output, Popen, CalledProcessError

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("name", nargs='+')
    parser.add_argument("-c", "--chapters", required = False)
    parser.add_argument("-s", "--scraper", required = False, default = "ComicK")

    args = parser.parse_args()

    query = " ".join(args.name)
    chapters = args.chapters
    scraper = args.scraper

    if query in ["", " "]:
        print("uhhh, enter a manga name you dummy!")
        exit(1)

    args = [
        "mangal", "inline", "--manga", "first", "-S", scraper, "--query", query, "--download", "--format", "cbz"
    ]

    if chapters is not None:
        args.extend(["--chapters", chapters])

    print(f"Downloading manga '{query}' with mangal...")

    cbz_files = None

    for i in range(10):

        try:
            cbz_files = check_output(args, text = True).splitlines()
        except CalledProcessError as e:
            print(f"MANGOL FAILED! Error: '{i}' - Trying again... ({i})")

        if cbz_files is not None:
            break

    cbz_files = [Path(file) for file in cbz_files]

    print(f"Collecting mangal's exported metadata and cbz files...")
    manga_folder_path = cbz_files[0].parent

    cover_image_path = manga_folder_path.joinpath("cover.png")

    if not cover_image_path.exists():
        cover_image_path = manga_folder_path.joinpath("cover.jpg")

    series_json_path = manga_folder_path.joinpath("series.json")

    manga_metadata: Dict[str, str | int] = json.load(series_json_path.open("r"))["metadata"]

    name = manga_metadata["name"]
    author = manga_metadata["publisher"]

    print(f"Adding '{name}' manga to calibre's library...")

    for index, cbz_file in enumerate(sorted(cbz_files, key = lambda x: int(x.name.split("_Chapter_")[1].split("_")[0].split(".")[0]))):
        popen = Popen(
            [
                "calibredb", "add", 
                "--authors", author, 
                "--automerge", "overwrite", 
                "--title", name + f" Chapter {index + 1}", 
                "--cover", cover_image_path, 
                "--series", name,
                cbz_file
            ]
        )

        popen.wait()

    print(f"\nRemoving '{manga_folder_path}'...")
    shutil.rmtree(manga_folder_path)

    print(f"Successfully added '{name}' to Calibre! ✨")