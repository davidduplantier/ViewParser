import json
import os
import sys
from jsonviewparser import JSONViewParser

parser = JSONViewParser("viewhierarchy.json")

assert len(parser.find("class", "Input")) == 26, "'Input' failed"
