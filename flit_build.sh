
#!/bin/sh

pip uninstall scroll -y
flit build
pip install dist/scroll-2020.6.25.tar.gz
scroll demo/demo.py
