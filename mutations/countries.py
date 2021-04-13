#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Mutations of countries """

import json

from auxiliars.constants import tlds_json


def countries(base, possibilities):
    with open(tlds_json) as file:
        options = json.load(file)

    part = base.rsplit('.', 1)

    if part[1] in options['tld']['countries']:
        for country in options['tld']['countries']:
            possibilities.append(part[0] + '.' + country)
    else:
        for country in options['tld']['countries']:
            possibilities.append(part[0] + '.' + part[1] + '.' + country)

    return possibilities
