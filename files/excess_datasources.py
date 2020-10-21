#!/usr/bin/env python3

import json

### BREAKDOWN:
# Call Grafana API for current datasources
# OR
# Get list from Ansible if already acquired elsewhere
#
# Compare currently configured datasources with datasources TO configure
#
# Return a list of all datasources that DO exist, but aren't in list TO configure
###

# TEMP: test data
example = [{"name": "hello", "orgId": 1}, {"name": "world", "orgId": 1}]

if __name__ == "__main__":
    print(json.dumps(example))
