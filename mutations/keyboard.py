#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" typosquatting with differents keyboards """

import json

from atpbar import atpbar
from auxiliars.constants import tlds_json


def keyboard(base, tlds, possibilities):
    with open(tlds_json, encoding='utf-8') as file:
        options = json.load(file)

    for i in atpbar(range(0, len(base)), name='Proximity of keyboard:  '):
        for keys in options['keyboards']:
            if base[i] in options['keyboards'][keys]:
                for c in options['keyboards'][keys][base[i]]:
                    possibilities.append(
                        base[:i] + c + base[i] + base[i + 1:] + '.' + tlds)
                    possibilities.append(
                        base[:i] + base[i] + c + base[i + 1:] + '.' + tlds)
                    possibilities.append(
                        base[:i] + c + base[i + 1:] + '.' + tlds)
                    for tld in options['tld']['inicial']:
                        possibilities.append(
                            base[:i] + c + base[i] + base[i + 1:] + '.' + tld)
                        possibilities.append(
                            base[:i] + base[i] + c + base[i + 1:] + '.' + tld)
                        possibilities.append(
                            base[:i] + c + base[i + 1:] + '.' + tld)

                        for tld2 in options['tld']['countries']:
                            possibilities.append(
                                base[:i] + c + base[i] +
                                base[i + 1:] + '.' + tld + '.' + tld2)
                            possibilities.append(
                                base[:i] + base[i] + c +
                                base[i + 1:] + '.' + tld + '.' + tld2)
                            possibilities.append(
                                base[:i] + c + base[i + 1:]
                                + '.' + tld + '.' + tld2)

    return possibilities
