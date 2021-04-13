#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Validacion de dominios con DoH"""

import base64
import requests
import dns.message as doh

from auxiliars.constants import ct
from auxiliars.constants import dnssec


def dns_doh(domain, threat):
    detected = {}
    message = doh.make_query(domain, 'A')
    dns_req = base64.urlsafe_b64encode(message.to_wire()).\
        decode("UTF8").rstrip("=")

    try:
        resp = requests.get(
            dnssec['elevenpaths']['url'], params={"dns": dns_req},
            headers={"Content-type": ct})
    except requests.RequestException:
        return detected

    if ct not in resp.headers["Content-Type"]:
        detected = {}
        return detected

    ips = []
    answers = []
    for response in doh.from_wire(resp.content).answer:
        answers = response.to_text().split("\n")

    for answer in answers:
        output = answer.split()
        ips.append(output[len(output) - 1])

    if dnssec['elevenpaths']['malware_ip'] in ips:
        detected[threat] = {}
        detected[threat]['report_DoH'] = 'Malware'
        detected[threat]['domain'] = domain
        detected[threat]['A'] = ''
        detected[threat]['MX'] = ''
    elif not ips:
        detected = ()
    else:
        detected[threat] = {}
        detected[threat]['report_DoH'] = 'Good'
        detected[threat]['domain'] = domain
        detected[threat]['A'] = ips

        mess_mx = doh.make_query(domain, 'MX')
        dns_mx = base64.urlsafe_b64encode(mess_mx.to_wire()).\
            decode("UTF8").rstrip("=")
        try:
            res_mx = requests.get(
                dnssec['elevenpaths']['url'], params={"dns": dns_mx},
                headers={"Content-type": ct})
        except requests.RequestException:
            detected[threat]['MX'] = ''
            return detected

        if ct not in res_mx.headers["Content-Type"]:
            detected[threat]['MX'] = ''
            return detected

        detected[threat]['MX'] = []
        ans = []
        for response in doh.from_wire(res_mx.content).answer:
            ans = response.to_text().split("\n")

        for ans_mx in ans:
            output = ans_mx.split()
            detected[threat]['MX'].append(output[len(output) - 1])

    return detected
