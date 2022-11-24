#!/usr/bin/bash

set -e

case "$1" in
    test_bot)
        exec python3 ./testbot/echo_bot.py
        ;;
    *)
        exec "$@"
esac