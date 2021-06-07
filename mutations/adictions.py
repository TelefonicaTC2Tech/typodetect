#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" reduce letters """

import json

from auxiliars.constants import tlds_json


def adictions(base, tlds, possibilities):
    with open(tlds_json, encoding='utf-8') as file:
        options = json.load(file)

    for mut in options['mutates']:
        possibilities.append(mut + base + '.' + tlds)

        if tlds.find('.') == -1:
            possibilities.append(mut + base + '-' + tlds + '.' + tlds)
            for key in options['tld'].keys():
                for tld in options['tld'][key]:
                    possibilities.append(mut + base + '-' + tlds + '.' + tld)
        else:
            modtlds = tlds.replace('.', '-')
            possibilities.append(mut + base + '-' + modtlds + '.' + tlds)
            for key in options['tld'].keys():
                for tld in options['tld'][key]:
                    possibilities.append(
                        mut + base + '-' + modtlds + '.' + tld)

    return possibilities
