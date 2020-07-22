
#!/bin/sh

pip uninstall scroll -y
flit build
pip install dist/scroll-2020.7.22.tar.gz
scroll demo/demo.py
