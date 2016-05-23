#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    if not os.path.exists('local_settings.py'):
        raise Exception('missing local_settings.py, start with:\n    cp local_settings.py.dist local_settings.py')
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "local_settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
