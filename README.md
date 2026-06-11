README

This code is based on Python MNE code by Welke and Kalenkovich, and checks each of our 8 videos for an SSVEP.

First run CleanData, then AnalyzeData.

The code uses original video IDs. A key from original ID to video ID used in the paper is present in the code, and below:

Original ID=Video ID referred to in paper
#H1=A1
#H2=A2
#H3=A3
#H4=A4
#C1=B1
#D1=B2
#E2=B3
#F1=B4

FlickerAnalysis.py is the source code for detecting true flicker rates after induced latency from openvibe. FlickerAnalysis.py is not necessary for main data analysis pipeline.=
