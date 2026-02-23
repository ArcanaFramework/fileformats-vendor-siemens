import struct
import pytest
from fileformats.core.exceptions import FormatMismatchError
from fileformats.vendor.siemens.medimage import SyngoMR_Xa_Twix


def _make_dat(tmp_path, name, first, second, pad=100):
    """Helper to create a synthetic .dat file with a given header."""
    p = tmp_path / name
    p.write_bytes(struct.pack("<II", first, second) + b"\x00" * pad)
    return p


def test_vdve_detection(tmp_path):
    dat = _make_dat(tmp_path, "vdve.dat", first=3, second=5)
    t = SyngoMR_Xa_Twix(dat)
    assert t.version_is_ve is True


def test_vdve_num_measurements(tmp_path):
    dat = _make_dat(tmp_path, "vdve.dat", first=3, second=5)
    t = SyngoMR_Xa_Twix(dat)
    assert t.num_measurements == 5


def test_vb_detection(tmp_path):
    dat = _make_dat(tmp_path, "vb.dat", first=20000, second=0)
    t = SyngoMR_Xa_Twix(dat)
    assert t.version_is_ve is False


def test_vb_num_measurements(tmp_path):
    dat = _make_dat(tmp_path, "vb.dat", first=20000, second=0)
    t = SyngoMR_Xa_Twix(dat)
    assert t.num_measurements == 1


def test_wrong_extension(tmp_path):
    bad = tmp_path / "test.txt"
    bad.write_bytes(struct.pack("<II", 2, 1) + b"\x00" * 100)
    with pytest.raises(FormatMismatchError):
        SyngoMR_Xa_Twix(bad)
