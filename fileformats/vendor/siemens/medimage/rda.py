from fileformats.core import validated_property
from fileformats.core.exceptions import FormatMismatchError
from fileformats.medimage.raw.mri import Rda

HEADER_START = b">>> Begin of header <<<"


class SyngoMr_Xa_Rda(Rda):  # type: ignore[misc]
    """Siemens MRI spectroscopy data in .rda format.

    The file starts with a plain-text header delimited by
    ``>>> Begin of header <<<`` and ``>>> End of header <<<`` markers,
    followed by binary spectroscopy data.

    Inherits extension and binary classifier.
    """

    @validated_property
    def is_valid_rda(self) -> bool:
        """Validate that the file begins with the expected header marker."""
        first_bytes = self.read_contents(size=len(HEADER_START), offset=0)
        if first_bytes != HEADER_START:
            raise FormatMismatchError(
                f"File {self.fspath!r} does not start with the expected "
                f"RDA header marker (got {first_bytes!r})"
            )
        return True
