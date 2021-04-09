#!/usr/bin/env python3

import json


def foo(config: Any):
    pass


def main() -> None:
    config = None
    with open('config.json', 'r') as config_file:
        config = json.load(config_file)

    foo(config)


if __name__ == '__main__':
    main()
