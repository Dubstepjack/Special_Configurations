#!/usr/bin/python

# ------------------------------------------------------------------------------
# Configurations generator script for the Professional Firmware
# Standard Volcano All Metal with thermistor #05 upto 300°C
# Author: Miguel A. Risco Castillo
# URL: https://github.com/mriscoc/Marlin_Configurations
# ------------------------------------------------------------------------------
import CreateConfigs

CreateConfigs.Generate('', ['422','ManualMesh','Volcano'])
CreateConfigs.Generate('', ['422','BLTouch','Volcano'])
CreateConfigs.Generate('', ['427','ManualMesh','Volcano'])
CreateConfigs.Generate('', ['427','BLTouch','Volcano'])


