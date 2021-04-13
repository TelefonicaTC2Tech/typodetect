#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

from auxiliars.constants import tlds_json


def blockchain(possibilities):
    with open(tlds_json) as file:
        options = json.load(file)

    bases = []

    for possibility in possibilities:
        if possibility.count('.') == 1:
            bases.append(possibility.split('.', 1)[0])
        else:
            for key in options['tld']:
                if possibility.rsplit('.', 2)[-1] in options['tld'][key]:
                    bases.append(possibility.rsplit('.', 2)[0]
                                 + '.' + possibility.rsplit('.', 2)[1])
                    break
                elif possibility.rsplit('.', 2)[-2] in options['tld'][key]:
                    bases.append(possibility.rsplit('.', 2)[0])
                    break
                elif key == 'updated':
                    bases.append(possibility.rsplit('.', 2)[0]
                                 + '.' + possibility.rsplit('.', 2)[1])

    bases = sorted(list(set(bases)))
    bdomains = []

    for base in bases:
        for coin in options['coins']:
            bdomains.append(base + '.' + coin)

    return bdomains
