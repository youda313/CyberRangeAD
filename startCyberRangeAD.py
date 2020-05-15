import os
import sys
import argparse
from modules import logger
from pathlib import Path
from modules.CustomConfigParser import CustomConfigParser
from modules.TerraformController import TerraformController
from modules.VagrantController import VagrantController
from modules.PackerController import PackerController

controller = VagrantController(config, log)
controller.build()
