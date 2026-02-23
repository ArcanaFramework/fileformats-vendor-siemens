import pytest
from fileformats.core.exceptions import FormatMismatchError
from fileformats.vendor.siemens.medimage import SyngoMr_Xa_Rda

HEADER_START = b">>> Begin of header <<<"
HEADER_END = b">>> End of header <<<"


def _make_rda(
    tmp_path, name, header_lines=None, start_marker=True, binary_tail=b"\x00" * 64
):
    """Helper to create a synthetic .rda file."""
    parts = []
    if start_marker:
        parts.append(HEADER_START + b"\n")
    if header_lines is not None:
        for line in header_lines:
            parts.append(line.encode("latin-1") + b"\n")
    parts.append(HEADER_END + b"\n")
    parts.append(binary_tail)
    p = tmp_path / name
    p.write_bytes(b"".join(parts))
    return p


def test_valid_rda(tmp_path):
    rda_file = _make_rda(tmp_path, "test.rda", header_lines=["PatientName: John"])
    rda = SyngoMr_Xa_Rda(rda_file)
    assert rda.is_valid_rda is True


def test_wrong_extension(tmp_path):
    rda_file = _make_rda(tmp_path, "test.txt", header_lines=["PatientName: John"])
    with pytest.raises(FormatMismatchError):
        SyngoMr_Xa_Rda(rda_file)


def test_missing_header_marker(tmp_path):
    rda_file = _make_rda(
        tmp_path, "test.rda", header_lines=["PatientName: John"], start_marker=False
    )
    with pytest.raises(FormatMismatchError):
        SyngoMr_Xa_Rda(rda_file)


def test_metadata_parsing(tmp_path):
    header_lines = [
        "PatientName: James",
        "PatientID: 12345",
        "TR: 2000",
        "TE: 30",
    ]
    rda_file = _make_rda(tmp_path, "test.rda", header_lines=header_lines)
    rda = SyngoMr_Xa_Rda(rda_file)
    metadata = rda.read_metadata()
    assert metadata["PatientName"] == "James"
    assert metadata["PatientID"] == "12345"
    assert metadata["TR"] == "2000"
    assert metadata["TE"] == "30"


def test_metadata_empty_header(tmp_path):
    rda_file = _make_rda(tmp_path, "test.rda", header_lines=[])
    rda = SyngoMr_Xa_Rda(rda_file)
    metadata = rda.read_metadata()
    assert metadata == {}


def test_metadata_colon_in_value(tmp_path):
    header_lines = ["ScanTime: 10:30:00"]
    rda_file = _make_rda(tmp_path, "test.rda", header_lines=header_lines)
    rda = SyngoMr_Xa_Rda(rda_file)
    metadata = rda.read_metadata()
    assert metadata["ScanTime"] == "10:30:00"
