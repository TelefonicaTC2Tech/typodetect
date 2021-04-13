#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Generador de mutaciones"""

from mutations.replace import replace
from mutations.distance import distance_levenshtein
from mutations.keyboard import keyboard
from mutations.countries import countries
from auxiliars.blockchain import blockchain
from mutations.subdomains import subdomains
from mutations.change_tld import change_tld
from mutations.repetition import repetition
from mutations.subtraction import subtraction
from mutations.integration import integration


def generator(parts):
    possibilities = []
    subposs = []
    if parts['tld_2'] == '':
        fqdn = parts['domain'] + '.' + parts['tld']
        base = parts['domain']
        tlds = parts['tld']
    else:
        fqdn = parts['domain'] + '.' + parts['tld'] + '.' + parts['tld_2']
        base = parts['domain']
        tlds = parts['tld'] + '.' + parts['tld_2']

    possibilities = countries(fqdn, possibilities)
    possibilities = integration(fqdn, possibilities)
    possibilities = subdomains(base, tlds, possibilities)
    possibilities = change_tld(base, possibilities)
    possibilities = subtraction(base, tlds, possibilities)
    possibilities = repetition(base, tlds, possibilities)
    possibilities = keyboard(base, tlds, possibilities)
    possibilities = replace(base, tlds, possibilities)
    possibilities = distance_levenshtein(base, tlds, possibilities)

    deletes = []
    for domain in possibilities:
        if domain[0] == '.' or domain[0] == '-':
            deletes.append(domain)
    for delete in deletes:
        possibilities.remove(delete)

    possibilities = sorted(list(set(possibilities)))

    if parts['subdomain'] != '':
        for poss in possibilities:
            subposs.append(parts['subdomain'] + '.' + poss)
        possibilities += subposs

    possibilities = possibilities + blockchain(possibilities)

    possibilities = sorted(list(set(possibilities)))

    return possibilities
