"""SCROLL: Automatically generates documentation and unit-tests for python programs"""
# this new verison sleeps for 30 seconds in case of any error/exception and kees retrying infinitely
'''
Main Entry file:
> Used for hooking into a running program using cli and/or a context manager
so that the program can be run as ..
scroll myprogram.py
'''
import sys


class RuntimeContextManager():
    def __init__(self, Tracer):
        self.tracer = Tracer()

    def __enter__(self):
        sys.settrace(self.tracer)
        return self.tracer

    def __exit__(self, type, value, traceback):
        pass
