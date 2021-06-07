#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" repeating letters """

import json

from atpbar import atpbar
from auxiliars.constants import tlds_json


def repetition(base, tlds, possibilities):
    with open(tlds_json, encoding='utf-8') as file:
        options = json.load(file)

    for i in atpbar(range(0, len(base)), name='Repetitions letters:  '):
        possibilities.append(base[:i] + base[i] + base[i]
                             + base[i + 1:] + '.' + tlds)

        for tld in options['tld']['inicial']:
            possibilities.append(base[:i] + base[i]
                                 + base[i] + base[i + 1:] + '.' + tld)
            for tld2 in options['tld']['countries']:
                possibilities.append(base[:i] + base[i] + base[i]
                                     + base[i + 1:] + '.' + tld + '.' + tld2)

    return possibilities
