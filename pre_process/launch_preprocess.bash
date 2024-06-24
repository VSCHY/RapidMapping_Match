#/bin/bash

source activate APIRISK

event="EMSR728"

python 1_process.py ${event}
python 2_postal_code.py ${event}