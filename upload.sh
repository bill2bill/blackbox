#!/bin/bash

for (( ; ; ))
do
    if hostname -I ; then
        # gsutil cp -r /home/volvo/blackbox/log/* gs://volvo_blackbox/
        gsutil rsync -r -C /home/volvo/blackbox/log/ gs://volvo_blackbox/log
    fi
done