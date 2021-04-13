#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" mutations levenshtein's kind """

import json
import Levenshtein

from atpbar import atpbar
from auxiliars.constants import tlds_json


def distance_levenshtein(base, tlds, possibilities):
    with open(tlds_json) as file:
        options = json.load(file)

    for i in atpbar(range(0, len(base)), name='Create Levenshtein words:  '):
        if base[i].isalpha():
            for letter in options['letters']:
                if Levenshtein.distance(base,
                                        base[:i] + letter + base[i + 1:]) == 1:
                    possibilities.append(base[:i] + letter + base[i + 1:]
                                         + "." + tlds)

    for letter in options['letters']:
        if Levenshtein.distance(base, base + letter) == 1:
            possibilities.append(base + letter + '.' + tlds)

    return possibilities
