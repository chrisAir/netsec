#!/usr/bin/env bash

echo "INSTALL python-aprmd5 IN HOME DIRECTORY"
cd python-aprmd5
./setup.py build
./setup.py install --home=~
echo "-----SETUP FINISHED-----"

echo "SETTING PYTHONPATH"
echo "export PYTHONPATH='${PYTHONPATH}:~/lib/python'" >> ~/.bashrc
echo "export PYTHONPATH=$PYTHONPATH:~/lib/python" >> ~/.bash_profile

echo "RELOADING bashrc/bash_profile"
source ~/.bashrc
source ~/.bash_profile

echo "RUNNING DECODEING"
cd ..~
chmod +x ueblerhack.py
./ueblerhack.py
echo "FINISHED"


