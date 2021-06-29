#!/usr/bin/python


class BaseCorporaBuilder(object):
    def __init__(self, *args, **kwargs):
        pass

    def build(self):
        # type: () -> int
        pass

    def export(self, output_file):
        raise NotImplementedError
