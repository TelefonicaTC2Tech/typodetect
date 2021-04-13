#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Process Threat"""

import json
import threading

from atpbar import flush
from atpbar import atpbar
from querys.doh import dns_doh
from querys.udp import dns_udp
from querys.bdns import dns_bdns
from auxiliars.constants import tlds_json


def worker(possibilities, start, end, thread, result, doh_server):
    with open(tlds_json) as file:
        options = json.load(file)

    availables = []
    name = 'thread {}'.format(thread)

    for threat in atpbar(range(start, end), name=name):
        if possibilities[threat].rsplit('.')[-1] in options['coins']:
            update = dns_bdns(possibilities[threat], threat)
        elif doh_server == 2:
            update = dns_udp(possibilities[threat], threat)
        else:
            update = dns_doh(possibilities[threat], threat)

        if update != {}:
            result.update(update)
            threat += 1
        else:
            availables.append(possibilities[threat])

    return result


def process(n_threads, possibilities, doh_server):
    sections = len(possibilities) // n_threads
    starts = []
    ends = []
    start = 0
    end = sections
    result = {}
    threads = []

    for i in range(n_threads):
        starts.append(start)
        ends.append(end)
        start += sections
        end += sections

    for i in range(len(starts)):
        t = threading.Thread(target=worker, args=(possibilities, starts[i],
                                                  ends[i], i, result,
                                                  doh_server,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    flush()

    return result
