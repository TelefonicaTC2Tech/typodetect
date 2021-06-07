#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" integration of domain and tld"""

import json

from auxiliars.constants import tlds_json


def integration(base, possibilities):
    with open(tlds_json, encoding='utf-8') as file:
        options = json.load(file)

    domain_int = base.replace('.', '')

    for tld in options['tld']['inicial']:
        possibilities.append(domain_int + '.' + tld)
        for tld2 in options['tld']['countries']:
            possibilities.append(domain_int + '.' + tld + '.' + tld2)

    return possibilities
