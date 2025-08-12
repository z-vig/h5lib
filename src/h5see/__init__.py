"""
## HDF5 Reader

An object-oriented reader for HDF5 files in python.
"""

from .reader import HDF5Reader
# from .library_v0 import H5Library, add_to_library, empty_library
from .library import H5Library

__all__ = [
    "HDF5Reader",
    "H5Library"
    # "H5Library",
    # "add_to_library",
    # "empty_library"
]
