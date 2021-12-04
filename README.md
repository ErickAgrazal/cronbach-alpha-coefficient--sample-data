# cronbach-alpha-coefficient--sample-data

This is a project that aims to generate a valid set of answers of a given poll. That sample set of answers will also have an alpha of cronbach higher than a set threshold.

The approach is basically a brute force, generating different set of answers until it finds one that has a alpha of cronbach higher than the threshold.

## Develop

1. Setup virtualenv: `virtualenv -p python3 .venv`
1. Initialize environment: `source ./.venv/bin/activate`
1. Install dependencies: `pip install -r requirements.txt`