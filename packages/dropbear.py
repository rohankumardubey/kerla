from . import Package

LOCALOPTIONS_H = """\
#define DEBUG_TRACE 1
#define DEBUG_NOFORK 1
"""


class Dropbear(Package):
    def __init__(self):
        super().__init__()
        self.name = "dropbear"
        self.version = "2020.81"
        self.url = f"https://matt.ucc.asn.au/dropbear/releases/dropbear-{self.version}.tar.bz2"
        self.host_deps = ["musl-tools"]
        self.files = {
            "/bin/dropbear": "dropbear",
            "/bin/dropbearkey": "dropbearkey",
        }

    def build(self):
        self.add_file("localoptions.h", LOCALOPTIONS_H)
        self.run(
            "./configure CC=musl-gcc --enable-static --disable-largefile --disable-zlib --disable-syslog")
        self.make()
