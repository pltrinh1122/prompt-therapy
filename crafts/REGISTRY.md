# Craft registry (instance state in the craft zone, Rule-11 property 2; #156)

One row per *installed* craft, never written by hand: a Tended craft's by `dyad craft install`, the core
craft's (`dyad-operator`, tree `dyad/`) by `dyad install` (#199). A craft authored in this system has no row
(`dyad craft list` shows it as `authored`). `sha256` is `distribute.archive_sha256` of the installed tree —
the proof it is unmodified, and what lets the push gate skip its test root (Rule-12 property 2); `source` is
where the archive came from (a `world` reference); `d-work` the installing d-work. No date: a second install
of the same version changes nothing.

| craft | version | source | sha256 | d-work |
|-------|---------|--------|--------|--------|
| cabinet | 0.8.0 | dyad-system@7e152f90e73d | 9ddf31041fa216e4317836f4cc21d8f5068d6c4cfc10696c65facda650ca32c4 |  |
| dyad-operator | 1.3.2 | dyad-system@7e152f90e73d | 85224b4fd9fbbfed1c927dbfe3383c118c5865ae883b47b270d9cb73d926c244 |  |
| sysadmin | 0.3.3 | dyad-system@7e152f90e73d | e9df55129ffd9174e950a23f09c1515aa1c6819f318cfcfdb144217de56b6b53 |  |
| sysarch | 0.4.1 | dyad-system@7e152f90e73d | 5d93d056168d483829df36f54b1258618f0b090c2af5d06ba8ac0e834f7dc044 |  |
| syseng | 0.8.0 | dyad-system@7e152f90e73d | 267a6a64b4b81425065541bef1f3a4871295f9e529b9e0c07cb4d7d729de8a56 |  |
