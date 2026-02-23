import pytest
from fileformats.core.exceptions import FormatMismatchError
from fileformats.vendor.siemens.medimage import SyngoMr_Xa_Puls


def _make_puls(tmp_path, name, content):  # codespell:ignore puls
    p = tmp_path / name
    p.write_text(content)
    return p


MINIMAL_PULS = (
    "1 4 40 280 5003\n"
    "ECG  Freq Per: 0 0\n"
    "PULS Freq Per: 72 830\n"
    "LogStartMDHTime:  49470570\n"
    "LogStopMDHTime:   49583052\n"
    "6003\n"
)


def test_valid_puls(tmp_path):
    p = _make_puls(tmp_path, "test.puls", MINIMAL_PULS)
    puls = SyngoMr_Xa_Puls(p)
    assert puls.fspath == p


def test_wrong_extension(tmp_path):
    p = _make_puls(tmp_path, "test.txt", MINIMAL_PULS)
    with pytest.raises(FormatMismatchError):
        SyngoMr_Xa_Puls(p)


def test_metadata_parsing(tmp_path):
    p = _make_puls(tmp_path, "test.puls", MINIMAL_PULS)
    puls = SyngoMr_Xa_Puls(p)
    metadata = puls.read_metadata()
    assert metadata["PULS Freq Per"] == "72 830"
    assert metadata["LogStartMDHTime"] == "49470570"
    assert metadata["LogStopMDHTime"] == "49583052"
