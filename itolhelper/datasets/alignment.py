from typing import List

from ..io import SeqRecord, read_seq_records

TEMPLATE = """DATASET_ALIGNMENT
#visualize multiple sequence alignments directly on the tree. Alignment must be in FASTA format.
#lines starting with a hash are comments and ignored during parsing
#=================================================================#
#                    MANDATORY SETTINGS                           #
#=================================================================#
#select the separator which is used to delimit the data below (TAB,SPACE or COMMA).This separator must be used throughout this file.
#SEPARATOR TAB
#SEPARATOR SPACE
SEPARATOR COMMA
#label is used in the legend table (can be changed later)
DATASET_LABEL,@label@
#dataset color (can be changed later)
COLOR,#ff0000
#=================================================================#
#                    OPTIONAL SETTINGS                            #
#=================================================================#
#define one or more custom alignment coloring schemes. They will appear in the color scheme selection box
#first field defines the scheme name, followed by a list of letters and their color assignments. Letters which do not
#have a color defined will be displayed with a white background
CUSTOM_COLOR_SCHEME,MY_SCHEME_1,A=#d2d0c9,M=#d2d0c9,I=#d2d0c9,L=#d2d0c9,V=#d2d0c9,P=#746f69,G=#746f69,C=#746f69,F=#d0ad16,Y=#d0ad16,W=#d0ad16,S=#34acfb,T=#34acfb,N=#34acfb,Q=#34acfb,R=#34fb54,K=#34fb54,H=#34fb54,D=#fb4034,E=#fb4034
CUSTOM_COLOR_SCHEME,MY_SCHEME_2,A=#30a040,R=#2015a5,N=#10ffa0,D=#6048c0,C=#608a80,Q=#601f00,E=#5048c0,G=#702048,H=#a5a4a4,I=#1a30f0,L=#11a0f0,K=#003505,M=#00a0f0,F=#10a0f0,P=#0ff300,S=#93f300,T=#33ff00,W=#0a30f0,Y=#25a4a4,V=#90a3f0
#=================================================================#
#     all other optional settings can be set or changed later     #
#           in the web interface (under 'Datasets' tab)           #
#=================================================================#
#left margin, used to increase/decrease the spacing to the next dataset. Can be negative, causing datasets to overlap. Used only for text labels which are displayed on the outside
MARGIN,0
#font size factor; default font size will be slightly less than the available space between leaves, but you can set a multiplication factor here to increase/decrease it (values from 0 to 1 will decrease it, values above 1 will increase it)
SIZE_FACTOR,1
#color scheme to use; possible values are 'none','clustal','zappo','taylor','hphob','helix','strand','turn' and 'buried'
#if CUSTOM_COLOR_SCHEME is defined, its label can also be used here
COLOR_SCHEME,clustal
#start and stop residue of the alignment to display; note that the complete length should be below ~4000 residues
START_POSITION,1
END_POSITION,100
#display repeating identical residues in each column as dots, instead of letters. Only the first letter in each repeat block will be displayed.
DOTTED_DISPLAY,0
#when DOTTED_DISPLAY=1, backgrounds of each dot will be colored if COLORED_DOTS is set to 1
COLORED_DOTS,1
#display the consensus sequence blow the alignment
DISPLAY_CONSENSUS,1
#display the residue conservation graph below the alignment
DISPLAY_CONSERVATION,1
#=================================================================#
#       Put the actual alignment below the "DATA" keyword         #
#=================================================================#
#alignment must be in FASTA format
#lines starting with a ">" sign should contain the sequence IDs (matching the tree IDs)
#all lines until the next sequence ID line will be taken as the actual aligned sequence string
#all space characters will be removed automatically
#empty lines are ignored
DATA
#Example alignment
#>SRC_AVIS2
#EEWYFGKI-- ---TRRESER LLLNP----- -----ENPRG TFLVRESET-
#---------- ---------- ---------- ------TKGA YCLSVSDFDN
#---------- ---------- ---------- ---------- ----------
#--AKGLNVKH YKIRKLDS-- ---------- -----GGFYI TS--------
#----RTQFSS --LQQLVAYY SKHADG
#
#>FGR_HUMAN
#EEWYFGKI-- ---GRKDAER QLLSP----- -----GNPQG AFLIRESET-
#---------- ---------- ---------- ------TKGA YSLSIRDWDQ
#---------- ---------- ---------- ---------- ----------
#--TRGDHVKH YKIRKLDM-- ---------- -----GGYYI TT--------
#----RVQFNS --VQELVQHY MEVNDG
#
#>Q94879
#EPWYFRKI-- ---KRIEAEK KLLLP----- -----ENEHG AFLIRDSES-
#---------- ---------- ---------- ------RHND YSLSVRDG--
#---------- ---------- ---------- ---------- ----------
#-----DTVKH YRIRQLDE-- ---------- -----GGFFI AR--------
#----RTTFRT --LQELVEHY SKDSDG
"""


def create_data(id: str, seq: str) -> str:
    return f">{id}\n{seq}"


def generate_alignment(seqrecords: List[SeqRecord], label: str = "alignment") -> str:
    template = [TEMPLATE.replace("@label@", label)]
    for record in seqrecords:
        template.append(create_data(record.id, record.seq))

    return "\n".join(template)
