"""
export_atmvars.py, Sam Murphy (2017-04-20)

exports the atmospheric variables that are required by 6S
(and the 6S_emulator) to calculate the coefficients for
atmospheric correction of Sentinel 2 imagery.

"""

from validation.test_sites import Targets

targets = Target.get()

print(targets.keys())