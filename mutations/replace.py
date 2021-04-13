#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" replace letters """

import json

from atpbar import atpbar
from auxiliars.constants import tlds_json


def replace(base, tlds, possibilities):
    with open(tlds_json) as file:
        options = json.load(file)

    for i in atpbar(range(0, len(base)), name='Replace letters:  '):
        if base[i].isalpha():
            for change in options['replace'][base[i]]:
                possibilities.append(
                    base[:i] + change + base[i + 1:] + '.' + tlds)

                for tld in options['tld']['inicial']:
                    possibilities.append(base[:i] + change +
                                         base[i + 1:] + '.' + tld)
                    for tld2 in options['tld']['countries']:
                        possibilities.append(base[:i] + change +
                                             base[i + 1:] + '.' + tld
                                             + '.' + tld2)

    return possibilities
