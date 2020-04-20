#!/bin/bash

debuild -k"gpg_key_id" -S -i -I
cd ..
dput ppa:launchpad_id/ppa package_name_$1_source.changes
rm package_name_*