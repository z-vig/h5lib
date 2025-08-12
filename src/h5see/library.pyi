from .reader import Page
from .reader import Bookshelf
from pathlib import Path
import os

PathLike = str | os.PathLike | Path


def add_file_to_library(file_path: PathLike) -> None: ...


class Georeference:
    data: Page
    obs: Page
    wavelengths: Page


class Cropped_data:
    data: Page
    obs: Page
    wavelengths: Page


class Thermal_correction:
    data: Page
    obs: Page
    photometric_coefficients: Page
    temp: Page
    wavelengths: Page


class Terrain_model:
    data: Page
    obs: Page
    wavelengths: Page


class Statistical_polishing:
    data: Page
    obs: Page
    wavelengths: Page


class Solar_spectrum_removal:
    data: Page
    obs: Page
    solar_spectrum: Page
    wavelengths: Page


class Pipeline_cache:
    cropped_data: Cropped_data
    georeference: Georeference
    solar_spectrum_removal: Solar_spectrum_removal
    statistical_polishing: Statistical_polishing
    terrain_model: Terrain_model
    thermal_correction: Thermal_correction


class Pds_terrain_pipeline_cache:
    cropped_data: Cropped_data
    georeference: Georeference
    solar_spectrum_removal: Solar_spectrum_removal
    statistical_polishing: Statistical_polishing
    terrain_model: Terrain_model
    thermal_correction: Thermal_correction


class H5LibraryClass:
    pipeline_cache: Pipeline_cache
    pds_terrain_pipeline_cache: Pds_terrain_pipeline_cache
    def add_bookshelf(self, p: PathLike | Bookshelf) -> None: ...


H5Library: H5LibraryClass


libcache = [
    "D:\\moon_data\\m3\\M3_stripes\\M3G20090208T175211\\pipeline_cache.hdf5",
    "D:\\moon_data\\m3\\M3_stripes\\M3G20090208T175211\\pds_terrain_pipeline_cache.hdf5",
]
