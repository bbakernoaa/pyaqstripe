"""
pyaqstripe"""

from . import colorbar_module

__version__ = "0.1.0"

__all__ = [
    "__version__",
    "colorbar_module",
]

create_aqstripe_cmap = colorbar_module.create_matplotlib_colorbar