#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Script for create txt file"""

import os

from querys.udp import dns_udp
from auxiliars.constants import b
from auxiliars.constants import reports
from auxiliars.constants import separator


def files_txt(result, domain, mutations):
    if not os.path.isdir(reports):
        os.makedirs(reports)

    with open(reports + domain + '.txt', 'w') as file:
        file.write(b)
        file.write('\n\n')
        file.write('[*] We detected ' + str(mutations) +
                   ' possibles domains mutations of ' + domain + '\n')
        file.write('[*] Of which ' + str(len(list(result.keys()))) +
                   ' domains resolved to an A or MX record' + '\n')
        file.write(separator + '\n\n')

        origin = dns_udp(domain, 0)
        if origin != {}:
            file.write('[*] Inicial Domain:  ' + origin[0]['domain'] + '\n')
            for a_ip in origin[0]['A']:
                file.write('\t[*] Register type A: ' + a_ip + '\n')
            for mx_ip in origin[0]['MX']:
                if mx_ip != '':
                    file.write('\t[*] Register type MX: ' + mx_ip + '\n')

        file.write(separator + '\n\n')

        for threat in list(result.keys()):
            file.write('[*] Detected domain: ' +
                       result[threat]['domain'] + '\n')
            if result[threat]['report_DoH'] == 'Malware':
                file.write('\t[*] DNS over HTTPS of ElevenPaths report this'
                           ' domain is Malware' + '\n')
            else:
                for a_ip in result[threat]['A']:
                    file.write('\t[*] Register type A: ' + a_ip + '\n')
                for mx_ip in result[threat]['MX']:
                    if mx_ip != '':
                        file.write('\t[*] Register type MX: ' + mx_ip + '\n')
            file.write(separator + '\n')
