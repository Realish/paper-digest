__version__ = "0.1.0"
__author__ = "Reza Alishahi"

import os
import sys
import warnings
import fitz
import openai
import base64

# check if the PyMuPDF version is at least 1.23.0
if tuple(map(int, fitz.VersionBind.split("."))) < (1, 23, 0):
    warnings.warn(
        "PyMuPDF 1.23.0 or higher is required for pdig to work properly. "
        "Please upgrade PyMuPDF to the latest version."
    )
    
__all__ = ["pdig", "doc_to_img"]



