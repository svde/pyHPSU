#! /bin/bash
python3 /usr/share/pyHPSU/bin/pyHPSU.py -d PYCAN -c flow_rate -c mode -c bpv -c posmix -c t_v1 -c t_dhw1 -c t_vbh -c t_r1 -c tliq2 -c ehs -c pump -o CLOUD -u EMONCMS -g /var/log/hpsu.fast.log -v 1
