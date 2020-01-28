#!/bin/bash

gcc -no-pie -o section.o -c section.c
gcc -Wl,-T addon.lds section.o -o section -no-pie
./patch.py section newbin
