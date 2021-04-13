#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Validacion de dominios con Blockchain - DNS"""

import urllib3
import requests

from auxiliars.constants import url_bdns

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def dns_bdns(domain, threat):
    detected = {}
    try:
        resp = requests.get(url_bdns + domain, verify=False)
    except requests.RequestException:
        return detected

    if resp.status_code == 200:
        detected[threat] = {}
        detected[threat]['report_DoH'] = ''
        detected[threat]['domain'] = domain
        detected[threat]['A'] = [resp.text]
        detected[threat]['MX'] = ''
    else:
        return detected

    return detected
