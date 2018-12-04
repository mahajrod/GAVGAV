#!/usr/bin/env python
from collections import OrderedDict

from GAVGAV.Routines import FileRoutines, GFFRoutines


class Gene:
    """
    id:          str
    name                str
    alias_list          list of str
    biotype            str // maybe use list of str?
    strand              str
    transcript_id_list    list of str
    coords                  list of 6 1D numpy arrays
        0   tss_coords              numpy 1D array, length = total number of TSS in all transcripts
        1   5ss_coords              numpy 1D array, length = total number of 5' splice sites in all transcripts
        2   3ss_coords              numpy 1D array, length = total number of 3' s[lice sites in all transcripts
        3   tes_coords              numpy 1D array, length = total number of TES in all transcripts
        4   trss_coords             numpy 1D array, length = total number of Translation SS in all transcripts
        5   tres_coords             numpy 1D array, length = total number of Translation ES in all transcripts
    transcripts             list of 6 2D numpy arrays
        0   tss                 numpy 2D array, size = number of transcripts X total number of TSS in all transcripts
        1   5ss                 numpy 2D array, size = number of transcripts X total number of 5' splice sites in all transcripts
        2   3ss                 numpy 2D array, size = number of transcripts X total number of 3' s[lice sites in all transcripts
        3   tes                 numpy 2D array, size = number of transcripts X total number of TES in all transcripts
        4   trss                numpy 2D array, size = number of transcripts X total number of Translation SS in all transcripts
        5   tres                numpy 2D array, size = number of transcripts X total number of Translation ES in all transcripts



    """

    __slots__ = ["id",                  # str
                 "name",                # str
                 "alias_list",          # list of str
                 "biotype",             # str // maybe use list of str?
                 "strand",              # str
                 "transcript_id_list",  # list of str
                 "coords"               # list of 6 numpy arrays
                 "tss_coords",           # numpy 1D array, length = total number of TSS in all transcripts
                 "5ss_coords",           # numpy 1D array, length = total number of 5' splice sites in all transcripts
                 "3ss_coords",            # numpy 1D array, length = total number of 3' s[lice sites in all transcripts
                 "tes_coords",            # numpy 1D array, length = total number of TES in all transcripts
                 "trss_coords",           # numpy 1D array, length = total number of Translation SS in all transcripts
                 "tres_coords",           # numpy 1D array, length = total number of Translation ES in all transcripts

                 ]

    def __init__(self):
        pass


class GeneCollection(OrderedDict):

    def __init__(self, input_file=None, filetype="gff"):

        self.TSS_INDEX = 0
        self.FIVESS_INDEX = 1
        self.THREE_INDEX = 2
        self.TES_INDEX = 3
        self.TRSS_INDEX = 4
        self.TESS_INDEX = 5

        OrderedDict.__init__(self)

        if input_file:
            if filetype == "gff":
                self.read_gff(input_file)

    def read_gff(self, gff_file):
        for line_list in FileRoutines.file_line_as_list_generator(gff_file):
            pass


