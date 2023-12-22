from .gen1 import AzureDatalakeFileSystem
from .spec import AzureBlobFile, AzureBlobFileSystem

__all__ = ["AzureBlobFileSystem", "AzureBlobFile", "AzureDatalakeFileSystem"]

try:
    from ._dvc_version import version as __version__  # type: ignore[import]
    from ._dvc_version import version_tuple  # type: ignore[import]
except ImportError:
    __version__ = "UNKNOWN"
    version_tuple = (0, 0, __version__)  # type: ignore[assignment]
