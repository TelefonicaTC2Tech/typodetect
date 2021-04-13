#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Changing TLD"""

import json

from atpbar import atpbar
from auxiliars.constants import tlds_json


def change_tld(base, possibilities):
    with open(tlds_json) as file:
        options = json.load(file)

    for tlds in atpbar(list(options['tld'].keys()), name="Change TLD:  "):
        for change in options['tld'][tlds]:
            possibilities.append(base + '.' + change)
            if tlds == 'inicial':
                for tld2 in options['tld']['countries']:
                    possibilities.append(base + '.' + change + '.' + tld2)

    return possibilities
