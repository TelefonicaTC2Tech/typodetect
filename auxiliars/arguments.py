#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" argumentos para procesar"""

import argparse


def arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-u',
                        "--update",
                        dest='update',
                        type=str,
                        help='(Y/N) for update TLD\'s database (default:N)',
                        default='N')
    parser.add_argument('-t',
                        "--threads",
                        dest='n_threads',
                        type=int,
                        help='Number of threads for processing (default:5)',
                        default=5)
    parser.add_argument('-d',
                        "--doh",
                        dest='doh_server',
                        type=int,
                        help='Section DoH for use:\n'
                             '\t[1] ElevenPaths (default)\n'
                             '\t[2] Cloudfare',
                        default=1)
    parser.add_argument('-o',
                        "--output",
                        dest='output',
                        type=str,
                        help='JSON or TXT, options of filetype (default:JSON)',
                        default='JSON')
    parser.add_argument("domain",
                        type=str,
                        help='specify domain to process')
    args = parser.parse_args()
    if args.domain is None:
        print(parser.print_usage)
        exit(0)
    else:
        return [args.domain, args.update, args.output,
                args.n_threads, args.doh_server]
