#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Validacion de dominios con tradicional"""

import dns.resolver as dns

from auxiliars.constants import dnssec


def dns_udp(domain, threat):
    detected = {}
    server = dns.Resolver(configure=False)
    server.timeout = 10.0
    server.lifetime = 8.0
    server.nameservers = [dnssec['couldfare']['server']]

    try:
        a_response = server.query(domain, 'A', tcp=True)
        ips = []
        mxs = []
        for ip in a_response:
            if ip.address == dnssec['couldfare']['malware_ip']:
                detected[threat] = {}
                detected[threat]['report_DoH'] = 'Malware'
                ips.append(ip.to_text())
            else:
                detected[threat] = {}
                detected[threat]['report_DoH'] = 'Good'
                ips.append(ip.to_text())
        detected[threat]['domain'] = domain
        detected[threat]['A'] = ips

        try:
            mx_response = server.query(domain, 'MX', tcp=True)
            for mx in mx_response:
                mxs.append(mx.to_text().split(' ')[1])
            detected[threat]['MX'] = mxs
        except:
            detected[threat]['MX'] = ['']

    except:
        pass

    return detected

