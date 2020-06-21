
#!/bin/sh

pip uninstall scroll -y
flit build
pip install dist/scroll-2020.6.16.tar.gz
scroll demo.py
