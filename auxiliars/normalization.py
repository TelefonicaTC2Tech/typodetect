#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Normalizacion de dominios"""

import tld
import json

from auxiliars.constants import tlds_json


def normalization(domain):
    with open(tlds_json, encoding='utf-8') as file:
        options = json.load(file)
    normalized = options['normalized']

    domain_tld = tld.get_tld(domain, fail_silently=True,
                             fix_protocol=True, as_object=True)
    if domain_tld is None:
        return normalized
    tlds = domain_tld.fld.split('.')
    tlds = tlds[-2:]

    for sections in list(options['tld'].keys()):
        if tlds[0] in options['tld'][sections]:
            new_tld = True
            break
        else:
            new_tld = False

    if (new_tld is False) and (tlds[0] not in (
            options['tld']['inicial'] or options['tld']['countries'])):
        normalized['tld'] = domain_tld.tld
        normalized['tld_2'] = ''
        normalized['domain'] = domain_tld.domain
        normalized['subdomain'] = domain_tld.subdomain
    elif new_tld and (domain_tld.domain == tlds[0]) and \
            (domain_tld.subdomain == ''):
        normalized['tld'] = tlds[1]
        normalized['tld_2'] = ''
        normalized['domain'] = domain_tld.domain
        normalized['subdomain'] = domain_tld.subdomain
    elif new_tld and (domain_tld.domain == tlds[0]) and \
            (domain_tld.subdomain != '') and \
            ((tlds[1] in options['tld']['inicial']) or (
            tlds[1] in options['tld']['countries'])):
        normalized['tld'] = tlds[0]
        normalized['tld_2'] = tlds[1]
        if domain_tld.subdomain.find('.') != -1:
            extras = domain_tld.subdomain.rsplit('.', 1)
            normalized['domain'] = extras[1]
            normalized['subdomain'] = extras[0]
        else:
            normalized['domain'] = domain_tld.subdomain
            normalized['subdomain'] = ''
    elif new_tld and (tlds[0] in (
            options['tld']['inicial'] or options['tld']['countries'])) \
            and tlds[1] != '':
        normalized['tld'] = tlds[0]
        normalized['tld_2'] = tlds[1]
        normalized['domain'] = domain_tld.domain
        normalized['subdomain'] = domain_tld.subdomain
    else:
        return normalized

    return normalized
