#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" creating subdomains"""

import json

from atpbar import atpbar
from auxiliars.constants import tlds_json


def subdomains(base, tlds, possibilities):
    with open(tlds_json) as file:
        options = json.load(file)

    for i in atpbar(range(0, len(base)), name='Creating subdomains:  '):
        new_sub = base[:i] + '.' + base[i:]
        new_div = base[:i] + '-' + base[i:]

        possibilities.append(new_sub + '.' + tlds)
        possibilities.append(new_sub + '.' + tlds)

        for tld in options['tld']['inicial']:
            possibilities.append(new_sub + '.' + tld)
            possibilities.append(new_div + '.' + tld)
            for tld2 in options['tld']['countries']:
                possibilities.append(new_sub + '.' + tld + '.' + tld2)
                possibilities.append(new_div + '.' + tld + '.' + tld2)

    return possibilities
