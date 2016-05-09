#!/usr/bin/env bash

echo "install python-aprmd5 in home directory"

cd python-aprmd5
./setup.py build
./setup.py install --home=~

echo "setting PYTHONPATH"
echo "export PYTHONPATH='${PYTHONPATH}:/usr/local/lib/python2.7/site-packages'" >> ~/.bashrc

echo "reloading bashrc"
source ~/.bashrc

echo "running password decoding"
cd ..
./ueblerhack.py


