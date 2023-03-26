# -*- coding: utf-8 -*-
from pathlib import Path, PurePath
from shutil import copytree, ignore_patterns

# filter
exclusions = (
    '*.pyc',
    '*.egg-info/',
    '01_setup_pdm_toml.sh',
    'copy_project.py',
    '.git/',
    'README.md',
    '.pdm.toml',
)


def callbackIgnore(paths):
    """ callback for shutil.copytree """
    def ignoref(directory, contents):
        #print(f"{directory} => {contents}")
        arr = [] 
        for f in contents:
            for p in paths:
                if (PurePath(directory, f).match(p)):
                    arr.append(f)
        return arr

    return ignoref


# current working directory
source = Path()
destination = Path('/home/ubuntu/project/pykind')
if not destination.exists():
    destination.mkdir(parents=True, exist_ok=True)

copytree(
    source, 
    destination, 
    dirs_exist_ok=True,
    ignore=callbackIgnore(exclusions))
    #ignore=ignore_patterns(*exclusions))
