#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from querys.doh import dns_doh
from querys.udp import dns_udp
from querys.bdns import dns_bdns


class TestTypoDetect(unittest.TestCase):
    maxDiff = None

    def setUp(self):
        self.domain = 'elevenpaths.com'
        self.threat = 0

    def test_dns_doh(self):
        domain = ['northnovacable.ca', 'telefonica.com']
        result = [{
            0: {
                'report_DoH': 'Malware',
                'domain': 'northnovacable.ca',
                'A': '',
                'MX': ''}}, {
            1: {
                'report_DoH': 'Good',
                'domain': 'telefonica.com',
                'A': ['212.170.36.79'],
                'MX': ['telefonicacorp.mail.protection.outlook.com.']}}]

        for d in domain:
            self.assertDictEqual(dns_doh(d, domain.index(d)),
                                 result[domain.index(d)])

    def test_dns_udp(self):
        result = {
            0: {
                'report_DoH': 'Good',
                'domain': self.domain,
                'A': ['52.212.36.140'],
                'MX': ['elevenpaths-com.mail.protection.outlook.com.']}}

        self.assertDictEqual(dns_udp(self.domain, self.threat), result)

    def test_dns_bdns(self):
        domain = ['eagletv.coin', self.domain]
        result = [{
            0: {
                'report_DoH': '',
                'domain': 'eagletv.coin',
                'A': ['192.243.100.192'],
                'MX': ''}}, {}]

        for d in domain:
            self.assertEqual(dns_bdns(d, self.threat), result[domain.index(d)])


if __name__ == "__main__":
    unittest.main()
