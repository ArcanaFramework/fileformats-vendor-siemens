from fileformats.generic import UnicodeFile


class SyngoMr_Xa_Puls(UnicodeFile):
    """Siemens PMU (Physiological Monitoring Unit) pulse oximetry data.

    Plain-text file containing pulse signal samples followed by
    summary statistics and timing metadata.
    """

    ext = ".puls"
