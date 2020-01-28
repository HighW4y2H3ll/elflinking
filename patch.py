#!/usr/bin/python3

import sys
import lief

binary = lief.parse(sys.argv[1])

#for section in binary.sections:
#    if section.name == ".duhh":
#        section.flags = lief.ELF.SECTION_FLAGS.ALLOC | lief.ELF.SECTION_FLAGS.EXECINSTR
for seg in binary.segments:
    if len(seg.sections) == 1 and seg.sections[0].name == ".duhh":
        #seg.sections[0].flags = lief.ELF.SECTION_FLAGS.ALLOC | lief.ELF.SECTION_FLAGS.EXECINSTR
        seg.remove(lief.ELF.SEGMENT_FLAGS.W)
        seg.add(lief.ELF.SEGMENT_FLAGS.R)
        seg.add(lief.ELF.SEGMENT_FLAGS.X)

if len(sys.argv) > 2:
    binary.write(sys.argv[2])
