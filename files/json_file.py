#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json
from datetime import datetime

from auxiliars.constants import reports


def files_json(result, domain):
    results_json = json.dumps(result, ensure_ascii=False)
    if not os.path.isdir(reports):
        os.makedirs(reports)

    with open(reports + domain +
              datetime.utcnow().isoformat() + '.json', 'w') as file:
        file.write(results_json)
