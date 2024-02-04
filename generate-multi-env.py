#!/usr/bin/python3
# 
# Generate random multi-envelope modulations for UVI Falcon
# Copyright (C) 2024 Paul W. Frields / Fifth Dominion Studios
# License: BSD - https://opensource.org/license/bsd-3-clause/

from random import random
import xml.etree.ElementTree as etree
import xml.dom.minidom as minidom
import sys

STEPS=64

multiEnvelopeAttribs = {
    "Name": "Multi Envelope 1",
    "DisplayName": "Multi Envelope 1",
    "Bypass": "0",
    "SyncToHost": "0",
    "VelocityAmount": "0",
    "VelocitySens": "0.75",
    "Retrigger": "1",
    "NumSteps": str(STEPS),
    "Speed": "0.200",
    "Smooth": "0.050",
    "Bipolar": "1",
    "NoteOffRetrigger": "0",
    "LoopStart": "0",
    "LoopEnd": str(STEPS-1)
}

incTime = 0.02
slewFactor = 0.2

steps = [("0", "0")]
for i in range(STEPS-2):
    slew = (random()-0.5) * incTime * slewFactor
    Time = incTime + slew
    DestLevel = (random() * 2.0) - 1.0
    steps.append(('%.10f' % (Time), '%.10f' % (DestLevel)))

steps.append(('%.10f' % ((random()-0.5) * incTime * slewFactor + incTime), "0"))

root = etree.Element('ModulePreset')
et = etree.ElementTree(root)
multiEnvelope = etree.SubElement(root, 'MultiEnvelope', multiEnvelopeAttribs)
etsteps = etree.SubElement(multiEnvelope, "Steps")
for i in steps:
    etsteps.append(etree.Element("Step",
                              {"Time": i[0], 
                               "DestLevel": i[1],
                               "Curve": "0"}))

#et.dump(root)

xmlstr = minidom.parseString(etree.tostring(root)).toprettyxml(indent="   ")
#et.write(sys.stdout, encoding='unicode')
sys.stdout.write(xmlstr)
