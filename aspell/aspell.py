#!/usr/bin/env python3

import subprocess
import sys
import os
import pathlib
import json

annotations = []

for file in sys.argv[1:]:
    misspells = subprocess.check_output([pathlib.Path(sys.argv[0]).parent.as_posix() + '/aspell.bash', file], text=True)

    for line in misspells.split('\n'):
        if len(line) != 0:
            [line_n, misspell] = line.split(':')
            annotations.append({
                "file": file,
                "line": line_n,
                "title": "Misspell " + misspell,
                "body": "The word `" + misspell + "` was misspelled.",
                "annotation_level": "warning",
            })

print(json.dumps(annotations))


