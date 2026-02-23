import struct
import typing as ty
from fileformats.core import mtime_cached_property, validated_property, extra
from fileformats.core.exceptions import FormatMismatchError
from fileformats.medimage.raw.mri import Kspace


class SyngoMR_Xa_Twix(Kspace):  # type: ignore[misc]
    """Siemens MRI raw k-space data in twix (.dat) format.

    Version detection follows twixtools.helpers.idea_version_check:
    - VD/VE: first uint32 < 10000 AND second uint32 <= 64
    - VB: otherwise (single measurement)
    """

    ext = ".dat"
    binary = True

    @validated_property
    def version_is_ve(self) -> bool:
        """Check whether the file is VD/VE format (True) or VB format (False).

        Based on twixtools.helpers.idea_version_check — reads the first 8 bytes
        as two little-endian uint32 values.
        """
        header_bytes = self.read_contents(size=8, offset=0)
        if len(header_bytes) < 8:
            raise FormatMismatchError(
                f"File {self.fspath!r} is too small to be a valid twix file "
                f"(need at least 8 bytes, got {len(header_bytes)})"
            )
        first, second = struct.unpack("<II", header_bytes)
        if first < 10000 and second <= 64:
            return True
        return False

    @mtime_cached_property
    def num_measurements(self) -> int:
        """Return the number of measurements in the twix file.

        VD/VE files store the measurement count in the second uint32.
        VB files always contain exactly 1 measurement.
        """
        if self.version_is_ve:
            header_bytes = self.read_contents(size=4, offset=4)
            (num_meas,) = struct.unpack("<I", header_bytes)
            return int(num_meas)
        return 1

    @extra
    def read_twix(self, **kwargs: ty.Any) -> ty.Any:
        """Read the twix file using twixtools.read_twix().

        Parameters
        ----------
        **kwargs : Any
            keyword arguments passed to twixtools.read_twix()

        Returns
        -------
        list
            list of twix measurement objects
        """
        raise NotImplementedError

    @extra
    def map_twix(self, **kwargs: ty.Any) -> ty.Any:
        """Memory-map the twix file using twixtools.map_twix().

        Parameters
        ----------
        **kwargs : Any
            keyword arguments passed to twixtools.map_twix()

        Returns
        -------
        list
            list of mapped twix measurement objects
        """
        raise NotImplementedError
