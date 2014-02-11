#!/usr/bin/python
'''
Copyright (c) 2009-2011, Artemis SudParis-IETR/INSA of Rennes
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

  * Redistributions of source code must retain the above copyright notice,
    this list of conditions and the following disclaimer.
  * Redistributions in binary form must reproduce the above copyright notice,
    this list of conditions and the following disclaimer in the documentation
    and/or other materials provided with the distribution.
  * Neither the name of the IETR/INSA of Rennes nor the names of its
    contributors may be used to endorse or promote products derived from this
    software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY
WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
SUCH DAMAGE.
'''

import argparse
import subprocess
import os
import sys

VERSION = "0.2"
DEFAULT_FILE_LIST = "mpeg"

def computeFileList():
    global fileList_all, fileList_reduce

    fileList_all = {

        # MPEG-4 Part2 Simple Profile
        "mpeg" : [
            "MPEG4/SIMPLE/I-VOP/hit000.m4v",
            "MPEG4/SIMPLE/I-VOP/jvc000.m4v",
            "MPEG4/SIMPLE/I-VOP/san000.m4v",
            "MPEG4/SIMPLE/I-VOP/san001.m4v",

            "MPEG4/SIMPLE/P-VOP/hit001.m4v",
            "MPEG4/SIMPLE/P-VOP/hit002.m4v",
            "MPEG4/SIMPLE/P-VOP/hit003.m4v",
            "MPEG4/SIMPLE/P-VOP/hit004.m4v",
            #"MPEG4/SIMPLE/P-VOP/hit005.m4v",
            #"MPEG4/SIMPLE/P-VOP/hit006.m4v",
            "MPEG4/SIMPLE/P-VOP/hit007.m4v",
            "MPEG4/SIMPLE/P-VOP/hit008.m4v",
            "MPEG4/SIMPLE/P-VOP/hit009.m4v",
            "MPEG4/SIMPLE/P-VOP/hit010.m4v",
            "MPEG4/SIMPLE/P-VOP/hit011.m4v",
            "MPEG4/SIMPLE/P-VOP/hit013.m4v",
            "MPEG4/SIMPLE/P-VOP/hit014.m4v",

            "MPEG4/SIMPLE/P-VOP/jvc001.m4v",
            "MPEG4/SIMPLE/P-VOP/jvc002.m4v",
            "MPEG4/SIMPLE/P-VOP/jvc003.m4v",
            "MPEG4/SIMPLE/P-VOP/jvc004.m4v",
            "MPEG4/SIMPLE/P-VOP/jvc005.m4v",
            "MPEG4/SIMPLE/P-VOP/jvc006.m4v",
            "MPEG4/SIMPLE/P-VOP/jvc007.m4v",
            "MPEG4/SIMPLE/P-VOP/jvc008.m4v",
            "MPEG4/SIMPLE/P-VOP/jvc009.m4v",
            "MPEG4/SIMPLE/P-VOP/jvc010.m4v",
            "MPEG4/SIMPLE/P-VOP/jvc011.m4v",
            "MPEG4/SIMPLE/P-VOP/jvc014.m4v",
            "MPEG4/SIMPLE/P-VOP/jvc015.m4v",
            "MPEG4/SIMPLE/P-VOP/jvc016.m4v",
            "MPEG4/SIMPLE/P-VOP/jvc017.m4v",
            "MPEG4/SIMPLE/P-VOP/jvc018.m4v",
            "MPEG4/SIMPLE/P-VOP/jvc019.m4v",
            "MPEG4/SIMPLE/P-VOP/jvc020.m4v",
            "MPEG4/SIMPLE/P-VOP/jvc021.m4v",

            "MPEG4/SIMPLE/P-VOP/san002.m4v",
            "MPEG4/SIMPLE/P-VOP/san003.m4v",
            "MPEG4/SIMPLE/P-VOP/san004.m4v",
            #"MPEG4/SIMPLE/P-VOP/san005.m4v",
            #"MPEG4/SIMPLE/P-VOP/san006.m4v",
            "MPEG4/SIMPLE/P-VOP/san007.m4v",
            #"MPEG4/SIMPLE/P-VOP/san009.m4v",
            "MPEG4/SIMPLE/P-VOP/san010.m4v",
            "MPEG4/SIMPLE/P-VOP/san011.m4v",
            "MPEG4/SIMPLE/P-VOP/san012.m4v",

            #"MPEG4/SIMPLE/Overall/hit016.m4v",
            #"MPEG4/SIMPLE/Overall/hit017.m4v",
            #"MPEG4/SIMPLE/Overall/hit018.m4v",
            #"MPEG4/SIMPLE/Overall/hit019.m4v",
            #"MPEG4/SIMPLE/Overall/hit020.m4v",
            #"MPEG4/SIMPLE/Overall/hit021.m4v",
            #"MPEG4/SIMPLE/Overall/hit022.m4v",
            #"MPEG4/SIMPLE/Overall/hit023.m4v",
            #"MPEG4/SIMPLE/Overall/hit024.m4v",

            #"MPEG4/CORE/I-VOP/mat001.m4v",
            #"MPEG4/CORE/I-VOP/mat004.m4v",
            #"MPEG4/CORE/I-VOP/mat005.m4v",
            #"MPEG4/CORE/I-VOP/mat006.m4v",
            #"MPEG4/CORE/I-VOP/mat007.m4v",
            #"MPEG4/CORE/I-VOP/mat008.m4v",
            #"MPEG4/CORE/I-VOP/mat009.m4v",
            #"MPEG4/CORE/I-VOP/mat010.m4v",
            #"MPEG4/CORE/I-VOP/mat013.m4v",
            #"MPEG4/CORE/I-VOP/mat014.m4v",
            #"MPEG4/CORE/I-VOP/mat015.m4v",
            #"MPEG4/CORE/I-VOP/mat016.m4v",

            #"MPEG4/SIMPLE/vcon-scs1.bits",
            #"MPEG4/SIMPLE/vcon-scs2.bits",
            #"MPEG4/SIMPLE/vcon-scs3.bits",
            #"MPEG4/SIMPLE/vcon-scs4.cmp",
            #"MPEG4/SIMPLE/vcon-scs5.cmp",
            #"MPEG4/SIMPLE/vcon-scs6.cmp",
            #"MPEG4/SIMPLE/vcon-scs7.cmp",
            #"MPEG4/SIMPLE/vcon-scs8.bits",
            #"MPEG4/SIMPLE/vcon-scs9.bits",
            #"MPEG4/SIMPLE/vcon-scs10.cmp",
            #"MPEG4/SIMPLE/vcon-scs11.cmp",

            #"MPEG4/foreman_cif_xvid_384kbps_I_P",
            #"MPEG4/foreman_cif_xvid_384kbps_I_P_B",
            #"MPEG4/foreman_cif_xvid_700kbps_I_P_B",

            "MPEG4/foreman_qcif_30.bit",

            "MPEG4/old_town_cross_420_720p_MPEG4_SP_6Mbps.bit",

            #"MPEG4/SIMPLE/P-VOP/jvc013",
            #"MPEG4/SIMPLE/P-VOP/hit012",
            #"MPEG4/SIMPLE/P-VOP/san008",
            #"MPEG4/SIMPLE/P-VOP/san014",
            #"MPEG4/SIMPLE/P-VOP/jvc012",
            #"MPEG4/SIMPLE/P-VOP/san013",
            #"MPEG4/SIMPLE/P-VOP/san015",
            #"MPEG4/SIMPLE/P-VOP/san016",
            #"MPEG4/SIMPLE/P-VOP/san017",
            #"MPEG4/SIMPLE/P-VOP/san018",
            #"MPEG4/SIMPLE/P-VOP/san019",
            #"MPEG4/SIMPLE/P-VOP/san020"
        ],

        # MPEG-4 Part10 / MPEG-4 AVC / H264
        "avc" : [
            "AVC/CAVLC/general/AVCNL-1/NL1_Sony_D.jsv",
            "AVC/CAVLC/general/AVCNL-2/SVA_NL1_B.264",
            "AVC/CAVLC/general/AVCNL-3/NL2_Sony_H.jsv",
            "AVC/CAVLC/general/AVCNL-4/SVA_NL2_E.264",
            "AVC/CAVLC/general/AVCBA-1/BA1_Sony_D.jsv",
            "AVC/CAVLC/general/AVCBA-2/SVA_BA1_B.264",
            "AVC/CAVLC/general/AVCBA-3/BA2_Sony_F.jsv",
            "AVC/CAVLC/general/AVCBA-4/SVA_BA2_D.264",
            "AVC/CAVLC/general/AVCBA-5/BA_MW_D.264",
            "AVC/CAVLC/general/AVCBA-6/BANM_MW_D.264",
            "AVC/CAVLC/general/AVCBA-7/BA1_FT_C.264",
            "AVC/CAVLC/general/AVCMQ-1/NLMQ1_JVC_C.264",
            "AVC/CAVLC/general/AVCMQ-2/NLMQ2_JVC_C.264",
            "AVC/CAVLC/general/AVCMQ-3/BAMQ1_JVC_C.264",
            "AVC/CAVLC/general/AVCMQ-4/BAMQ2_JVC_C.264",
            "AVC/CAVLC/general/AVCSL-1/SVA_Base_B.264",
            "AVC/CAVLC/general/AVCSL-2/SVA_FM1_E.264",
            "AVC/CAVLC/general/AVCSQ-1/BASQP1_Sony_C.jsv",
            "AVC/CAVLC/general/AVCCI-1/CI_MW_D.264",
            "AVC/CAVLC/general/AVCCI-2/SVA_CL1_E.264",
            "AVC/CAVLC/general/AVCCI-3/CI1_FT_B.264",
            #"AVC/CAVLC/general/AVCFC-1/CVFC1_Sony_C.jsv",
            "AVC/CAVLC/general/AVCAUD-1/AUD_MW_E.264",
            "AVC/CAVLC/general/AVCMIDR-1/MIDR_MW_D.264",
            "AVC/CAVLC/general/AVCNRF-1/NRF_MW_E.264",
            "AVC/CAVLC/general/AVCMPS-1/MPS_MW_A.264",
            "AVC/CAVLC/IPCM/AVCPCM-1/CVPCMNL1_SVA_C.264",
            "AVC/CAVLC/IPCM/AVCPCM-2/CVPCMNL2_SVA_C.264",
            "AVC/CAVLC/Long_Sequence/AVCLS-1/LS_SVA_D.264",
            "AVC/CAVLC/MMCO/AVCMR-1/MR1_BT_A.h264",
            "AVC/CAVLC/MMCO/AVCMR-2/MR2_TANDBERG_E.264",
            "AVC/CAVLC/MMCO/AVCMR-3/MR3_TANDBERG_B.264",
            "AVC/CAVLC/MMCO/AVCMR-4/MR4_TANDBERG_C.264",
            "AVC/CAVLC/MMCO/AVCMR-5/MR5_TANDBERG_C.264",
            "AVC/CAVLC/MMCO/AVCMR-6/MR1_MW_A.264",
            "AVC/CAVLC/MMCO/AVCMR-7/MR2_MW_A.264",
            "AVC/CAVLC/MMCO/AVCMR-11/HCBP1_HHI_A.264",
            "AVC/CAVLC/MMCO/AVCMR-12/HCBP2_HHI_A.264"
        ],

        # HEVC
        "hevc" : [
            #"HEVC/i_main/BasketballDrill_832x480_50_qp22.bin",
            #"HEVC/i_main/BasketballDrill_832x480_50_qp27.bin",
            #"HEVC/i_main/BasketballDrill_832x480_50_qp32.bin",
            "HEVC/i_main/BasketballDrill_832x480_50_qp37.bin",
            #"HEVC/i_main/BasketballDrillText_832x480_50_qp22.bin",
            #"HEVC/i_main/BasketballDrillText_832x480_50_qp27.bin",
            #"HEVC/i_main/BasketballDrillText_832x480_50_qp32.bin",
            "HEVC/i_main/BasketballDrillText_832x480_50_qp37.bin",
            #"HEVC/i_main/BasketballDrive_1920x1080_50_qp22.bin",
            #"HEVC/i_main/BasketballDrive_1920x1080_50_qp27.bin",
            #"HEVC/i_main/BasketballDrive_1920x1080_50_qp32.bin",
            "HEVC/i_main/BasketballDrive_1920x1080_50_qp37.bin",
            #"HEVC/i_main/BasketballPass_416x240_50_qp22.bin",
            #"HEVC/i_main/BasketballPass_416x240_50_qp27.bin",
            #"HEVC/i_main/BasketballPass_416x240_50_qp32.bin",
            "HEVC/i_main/BasketballPass_416x240_50_qp37.bin",
            #"HEVC/i_main/BlowingBubbles_416x240_50_qp22.bin",
            #"HEVC/i_main/BlowingBubbles_416x240_50_qp27.bin",
            #"HEVC/i_main/BlowingBubbles_416x240_50_qp32.bin",
            "HEVC/i_main/BlowingBubbles_416x240_50_qp37.bin",
            #"HEVC/i_main/BQMall_832x480_60_qp22.bin",
            #"HEVC/i_main/BQMall_832x480_60_qp27.bin",
            #"HEVC/i_main/BQMall_832x480_60_qp32.bin",
            "HEVC/i_main/BQMall_832x480_60_qp37.bin",
            #"HEVC/i_main/BQSquare_416x240_60_qp22.bin",
            #"HEVC/i_main/BQSquare_416x240_60_qp27.bin",
            #"HEVC/i_main/BQSquare_416x240_60_qp32.bin",
            "HEVC/i_main/BQSquare_416x240_60_qp37.bin",
            #"HEVC/i_main/BQTerrace_1920x1080_60_qp22.bin",
            #"HEVC/i_main/BQTerrace_1920x1080_60_qp27.bin",
            #"HEVC/i_main/BQTerrace_1920x1080_60_qp32.bin",
            "HEVC/i_main/BQTerrace_1920x1080_60_qp37.bin",
            #"HEVC/i_main/Cactus_1920x1080_50_qp22.bin",
            #"HEVC/i_main/Cactus_1920x1080_50_qp27.bin",
            #"HEVC/i_main/Cactus_1920x1080_50_qp32.bin",
            "HEVC/i_main/Cactus_1920x1080_50_qp37.bin",
            #"HEVC/i_main/ChinaSpeed_1024x768_30_qp22.bin",
            #"HEVC/i_main/ChinaSpeed_1024x768_30_qp27.bin",
            #"HEVC/i_main/ChinaSpeed_1024x768_30_qp32.bin",
            "HEVC/i_main/ChinaSpeed_1024x768_30_qp37.bin",
            #"HEVC/i_main/FourPeople_1280x720_60_qp22.bin",
            #"HEVC/i_main/FourPeople_1280x720_60_qp27.bin",
            #"HEVC/i_main/FourPeople_1280x720_60_qp32.bin",
            "HEVC/i_main/FourPeople_1280x720_60_qp37.bin",
            #"HEVC/i_main/Johnny_1280x720_60_qp22.bin",
            #"HEVC/i_main/Johnny_1280x720_60_qp27.bin",
            #"HEVC/i_main/Johnny_1280x720_60_qp32.bin",
            "HEVC/i_main/Johnny_1280x720_60_qp37.bin",
            #"HEVC/i_main/Kimono1_1920x1080_24_qp22.bin",
            #"HEVC/i_main/Kimono1_1920x1080_24_qp27.bin",
            #"HEVC/i_main/Kimono1_1920x1080_24_qp32.bin",
            "HEVC/i_main/Kimono1_1920x1080_24_qp37.bin",
            #"HEVC/i_main/KristenAndSara_1280x720_60_qp22.bin",
            #"HEVC/i_main/KristenAndSara_1280x720_60_qp27.bin",
            #"HEVC/i_main/KristenAndSara_1280x720_60_qp32.bin",
            "HEVC/i_main/KristenAndSara_1280x720_60_qp37.bin",
            #"HEVC/i_main/NebutaFestival_2560x1600_60_10bit_crop_qp22.bin",
            #"HEVC/i_main/NebutaFestival_2560x1600_60_10bit_crop_qp27.bin",
            #"HEVC/i_main/NebutaFestival_2560x1600_60_10bit_crop_qp32.bin",
            "HEVC/i_main/NebutaFestival_2560x1600_60_10bit_crop_qp37.bin",
            #"HEVC/i_main/ParkScene_1920x1080_24_qp22.bin",
            #"HEVC/i_main/ParkScene_1920x1080_24_qp27.bin",
            #"HEVC/i_main/ParkScene_1920x1080_24_qp32.bin",
            "HEVC/i_main/ParkScene_1920x1080_24_qp37.bin",
            #"HEVC/i_main/PartyScene_832x480_50_qp22.bin",
            #"HEVC/i_main/PartyScene_832x480_50_qp27.bin",
            #"HEVC/i_main/PartyScene_832x480_50_qp32.bin",
            "HEVC/i_main/PartyScene_832x480_50_qp37.bin",
            #"HEVC/i_main/PeopleOnStreet_2560x1600_30_crop_qp22.bin",
            #"HEVC/i_main/PeopleOnStreet_2560x1600_30_crop_qp27.bin",
            #"HEVC/i_main/PeopleOnStreet_2560x1600_30_crop_qp32.bin",
            "HEVC/i_main/PeopleOnStreet_2560x1600_30_crop_qp37.bin",
            #"HEVC/i_main/RaceHorses_416x240_30_qp22.bin",
            #"HEVC/i_main/RaceHorses_416x240_30_qp27.bin",
            #"HEVC/i_main/RaceHorses_416x240_30_qp32.bin",
            "HEVC/i_main/RaceHorses_416x240_30_qp37.bin",
            #"HEVC/i_main/RaceHorses_832x480_30_qp22.bin",
            #"HEVC/i_main/RaceHorses_832x480_30_qp27.bin",
            #"HEVC/i_main/RaceHorses_832x480_30_qp32.bin",
            "HEVC/i_main/RaceHorses_832x480_30_qp37.bin",
            #"HEVC/i_main/SlideEditing_1280x720_30_qp22.bin",
            #"HEVC/i_main/SlideEditing_1280x720_30_qp27.bin",
            #"HEVC/i_main/SlideEditing_1280x720_30_qp32.bin",
            "HEVC/i_main/SlideEditing_1280x720_30_qp37.bin",
            #"HEVC/i_main/SlideShow_1280x720_20_qp22.bin",
            #"HEVC/i_main/SlideShow_1280x720_20_qp27.bin",
            #"HEVC/i_main/SlideShow_1280x720_20_qp32.bin",
            "HEVC/i_main/SlideShow_1280x720_20_qp37.bin",
            #"HEVC/i_main/SteamLocomotiveTrain_2560x1600_60_10bit_crop_qp22.bin",
            #"HEVC/i_main/SteamLocomotiveTrain_2560x1600_60_10bit_crop_qp27.bin",
            #"HEVC/i_main/SteamLocomotiveTrain_2560x1600_60_10bit_crop_qp32.bin",
            "HEVC/i_main/SteamLocomotiveTrain_2560x1600_60_10bit_crop_qp37.bin",
            #"HEVC/i_main/Traffic_2560x1600_30_crop_qp22.bin",
            #"HEVC/i_main/Traffic_2560x1600_30_crop_qp27.bin",
            #"HEVC/i_main/Traffic_2560x1600_30_crop_qp32.bin",
            "HEVC/i_main/Traffic_2560x1600_30_crop_qp37.bin",
            #"HEVC/ld_main/BasketballDrill_832x480_50_qp22.bin",
            #"HEVC/ld_main/BasketballDrill_832x480_50_qp27.bin",
            #"HEVC/ld_main/BasketballDrill_832x480_50_qp32.bin",
            "HEVC/ld_main/BasketballDrill_832x480_50_qp37.bin",
            #"HEVC/ld_main/BasketballDrillText_832x480_50_qp22.bin",
            #"HEVC/ld_main/BasketballDrillText_832x480_50_qp27.bin",
            #"HEVC/ld_main/BasketballDrillText_832x480_50_qp32.bin",
            "HEVC/ld_main/BasketballDrillText_832x480_50_qp37.bin",
            #"HEVC/ld_main/BasketballDrive_1920x1080_50_qp22.bin",
            #"HEVC/ld_main/BasketballDrive_1920x1080_50_qp27.bin",
            #"HEVC/ld_main/BasketballDrive_1920x1080_50_qp32.bin",
            "HEVC/ld_main/BasketballDrive_1920x1080_50_qp37.bin",
            #"HEVC/ld_main/BasketballPass_416x240_50_qp22.bin",
            #"HEVC/ld_main/BasketballPass_416x240_50_qp27.bin",
            #"HEVC/ld_main/BasketballPass_416x240_50_qp32.bin",
            "HEVC/ld_main/BasketballPass_416x240_50_qp37.bin",
            #"HEVC/ld_main/BlowingBubbles_416x240_50_qp22.bin",
            #"HEVC/ld_main/BlowingBubbles_416x240_50_qp27.bin",
            #"HEVC/ld_main/BlowingBubbles_416x240_50_qp32.bin",
            "HEVC/ld_main/BlowingBubbles_416x240_50_qp37.bin",
            #"HEVC/ld_main/BQMall_832x480_60_qp22.bin",
            #"HEVC/ld_main/BQMall_832x480_60_qp27.bin",
            #"HEVC/ld_main/BQMall_832x480_60_qp32.bin",
            "HEVC/ld_main/BQMall_832x480_60_qp37.bin",
            #"HEVC/ld_main/BQSquare_416x240_60_qp22.bin",
            #"HEVC/ld_main/BQSquare_416x240_60_qp27.bin",
            #"HEVC/ld_main/BQSquare_416x240_60_qp32.bin",
            "HEVC/ld_main/BQSquare_416x240_60_qp37.bin",
            #"HEVC/ld_main/BQTerrace_1920x1080_60_qp22.bin",
            #"HEVC/ld_main/BQTerrace_1920x1080_60_qp27.bin",
            #"HEVC/ld_main/BQTerrace_1920x1080_60_qp32.bin",
            "HEVC/ld_main/BQTerrace_1920x1080_60_qp37.bin",
            #"HEVC/ld_main/Cactus_1920x1080_50_qp22.bin",
            #"HEVC/ld_main/Cactus_1920x1080_50_qp27.bin",
            #"HEVC/ld_main/Cactus_1920x1080_50_qp32.bin",
            "HEVC/ld_main/Cactus_1920x1080_50_qp37.bin",
            #"HEVC/ld_main/ChinaSpeed_1024x768_30_qp22.bin",
            #"HEVC/ld_main/ChinaSpeed_1024x768_30_qp27.bin",
            #"HEVC/ld_main/ChinaSpeed_1024x768_30_qp32.bin",
            "HEVC/ld_main/ChinaSpeed_1024x768_30_qp37.bin",
            #"HEVC/ld_main/FourPeople_1280x720_60_qp22.bin",
            #"HEVC/ld_main/FourPeople_1280x720_60_qp27.bin",
            #"HEVC/ld_main/FourPeople_1280x720_60_qp32.bin",
            "HEVC/ld_main/FourPeople_1280x720_60_qp37.bin",
            #"HEVC/ld_main/Johnny_1280x720_60_qp22.bin",
            #"HEVC/ld_main/Johnny_1280x720_60_qp27.bin",
            #"HEVC/ld_main/Johnny_1280x720_60_qp32.bin",
            "HEVC/ld_main/Johnny_1280x720_60_qp37.bin",
            #"HEVC/ld_main/Kimono1_1920x1080_24_qp22.bin",
            #"HEVC/ld_main/Kimono1_1920x1080_24_qp27.bin",
            #"HEVC/ld_main/Kimono1_1920x1080_24_qp32.bin",
            "HEVC/ld_main/Kimono1_1920x1080_24_qp37.bin",
            #"HEVC/ld_main/KristenAndSara_1280x720_60_qp22.bin",
            #"HEVC/ld_main/KristenAndSara_1280x720_60_qp27.bin",
            #"HEVC/ld_main/KristenAndSara_1280x720_60_qp32.bin",
            "HEVC/ld_main/KristenAndSara_1280x720_60_qp37.bin",
            #"HEVC/ld_main/NebutaFestival_2560x1600_60_10bit_crop_qp22.bin",
            #"HEVC/ld_main/NebutaFestival_2560x1600_60_10bit_crop_qp27.bin",
            #"HEVC/ld_main/NebutaFestival_2560x1600_60_10bit_crop_qp32.bin",
            "HEVC/ld_main/NebutaFestival_2560x1600_60_10bit_crop_qp37.bin",
            #"HEVC/ld_main/ParkScene_1920x1080_24_qp22.bin",
            #"HEVC/ld_main/ParkScene_1920x1080_24_qp27.bin",
            #"HEVC/ld_main/ParkScene_1920x1080_24_qp32.bin",
            "HEVC/ld_main/ParkScene_1920x1080_24_qp37.bin",
            #"HEVC/ld_main/PartyScene_832x480_50_qp22.bin",
            #"HEVC/ld_main/PartyScene_832x480_50_qp27.bin",
            #"HEVC/ld_main/PartyScene_832x480_50_qp32.bin",
            "HEVC/ld_main/PartyScene_832x480_50_qp37.bin",
            #"HEVC/ld_main/PeopleOnStreet_2560x1600_30_crop_qp22.bin",
            #"HEVC/ld_main/PeopleOnStreet_2560x1600_30_crop_qp27.bin",
            #"HEVC/ld_main/PeopleOnStreet_2560x1600_30_crop_qp32.bin",
            "HEVC/ld_main/PeopleOnStreet_2560x1600_30_crop_qp37.bin",
            #"HEVC/ld_main/RaceHorses_416x240_30_qp22.bin",
            #"HEVC/ld_main/RaceHorses_416x240_30_qp27.bin",
            #"HEVC/ld_main/RaceHorses_416x240_30_qp32.bin",
            "HEVC/ld_main/RaceHorses_416x240_30_qp37.bin",
            #"HEVC/ld_main/RaceHorses_832x480_30_qp22.bin",
            #"HEVC/ld_main/RaceHorses_832x480_30_qp27.bin",
            #"HEVC/ld_main/RaceHorses_832x480_30_qp32.bin",
            "HEVC/ld_main/RaceHorses_832x480_30_qp37.bin",
            #"HEVC/ld_main/SlideEditing_1280x720_30_qp22.bin",
            #"HEVC/ld_main/SlideEditing_1280x720_30_qp27.bin",
            #"HEVC/ld_main/SlideEditing_1280x720_30_qp32.bin",
            "HEVC/ld_main/SlideEditing_1280x720_30_qp37.bin",
            #"HEVC/ld_main/SlideShow_1280x720_20_qp22.bin",
            #"HEVC/ld_main/SlideShow_1280x720_20_qp27.bin",
            #"HEVC/ld_main/SlideShow_1280x720_20_qp32.bin",
            "HEVC/ld_main/SlideShow_1280x720_20_qp37.bin",
            #"HEVC/ld_main/SteamLocomotiveTrain_2560x1600_60_10bit_crop_qp22.bin",
            #"HEVC/ld_main/SteamLocomotiveTrain_2560x1600_60_10bit_crop_qp27.bin",
            #"HEVC/ld_main/SteamLocomotiveTrain_2560x1600_60_10bit_crop_qp32.bin",
            "HEVC/ld_main/SteamLocomotiveTrain_2560x1600_60_10bit_crop_qp37.bin",
            #"HEVC/ld_main/Traffic_2560x1600_30_crop_qp22.bin",
            #"HEVC/ld_main/Traffic_2560x1600_30_crop_qp27.bin",
            #"HEVC/ld_main/Traffic_2560x1600_30_crop_qp32.bin",
            "HEVC/ld_main/Traffic_2560x1600_30_crop_qp37.bin",
            #"HEVC/lp_main/BasketballDrill_832x480_50_qp22.bin",
            #"HEVC/lp_main/BasketballDrill_832x480_50_qp27.bin",
            #"HEVC/lp_main/BasketballDrill_832x480_50_qp32.bin",
            "HEVC/lp_main/BasketballDrill_832x480_50_qp37.bin",
            #"HEVC/lp_main/BasketballDrillText_832x480_50_qp22.bin",
            #"HEVC/lp_main/BasketballDrillText_832x480_50_qp27.bin",
            #"HEVC/lp_main/BasketballDrillText_832x480_50_qp32.bin",
            "HEVC/lp_main/BasketballDrillText_832x480_50_qp37.bin",
            #"HEVC/lp_main/BasketballDrive_1920x1080_50_qp22.bin",
            #"HEVC/lp_main/BasketballDrive_1920x1080_50_qp27.bin",
            #"HEVC/lp_main/BasketballDrive_1920x1080_50_qp32.bin",
            "HEVC/lp_main/BasketballDrive_1920x1080_50_qp37.bin",
            #"HEVC/lp_main/BasketballPass_416x240_50_qp22.bin",
            #"HEVC/lp_main/BasketballPass_416x240_50_qp27.bin",
            #"HEVC/lp_main/BasketballPass_416x240_50_qp32.bin",
            "HEVC/lp_main/BasketballPass_416x240_50_qp37.bin",
            #"HEVC/lp_main/BlowingBubbles_416x240_50_qp22.bin",
            #"HEVC/lp_main/BlowingBubbles_416x240_50_qp27.bin",
            #"HEVC/lp_main/BlowingBubbles_416x240_50_qp32.bin",
            "HEVC/lp_main/BlowingBubbles_416x240_50_qp37.bin",
            #"HEVC/lp_main/BQMall_832x480_60_qp22.bin",
            #"HEVC/lp_main/BQMall_832x480_60_qp27.bin",
            #"HEVC/lp_main/BQMall_832x480_60_qp32.bin",
            "HEVC/lp_main/BQMall_832x480_60_qp37.bin",
            #"HEVC/lp_main/BQSquare_416x240_60_qp22.bin",
            #"HEVC/lp_main/BQSquare_416x240_60_qp27.bin",
            #"HEVC/lp_main/BQSquare_416x240_60_qp32.bin",
            "HEVC/lp_main/BQSquare_416x240_60_qp37.bin",
            #"HEVC/lp_main/BQTerrace_1920x1080_60_qp22.bin",
            #"HEVC/lp_main/BQTerrace_1920x1080_60_qp27.bin",
            #"HEVC/lp_main/BQTerrace_1920x1080_60_qp32.bin",
            "HEVC/lp_main/BQTerrace_1920x1080_60_qp37.bin",
            #"HEVC/lp_main/Cactus_1920x1080_50_qp22.bin",
            #"HEVC/lp_main/Cactus_1920x1080_50_qp27.bin",
            #"HEVC/lp_main/Cactus_1920x1080_50_qp32.bin",
            "HEVC/lp_main/Cactus_1920x1080_50_qp37.bin",
            #"HEVC/lp_main/ChinaSpeed_1024x768_30_qp22.bin",
            #"HEVC/lp_main/ChinaSpeed_1024x768_30_qp27.bin",
            #"HEVC/lp_main/ChinaSpeed_1024x768_30_qp32.bin",
            "HEVC/lp_main/ChinaSpeed_1024x768_30_qp37.bin",
            #"HEVC/lp_main/FourPeople_1280x720_60_qp22.bin",
            #"HEVC/lp_main/FourPeople_1280x720_60_qp27.bin",
            #"HEVC/lp_main/FourPeople_1280x720_60_qp32.bin",
            "HEVC/lp_main/FourPeople_1280x720_60_qp37.bin",
            #"HEVC/lp_main/Johnny_1280x720_60_qp22.bin",
            #"HEVC/lp_main/Johnny_1280x720_60_qp27.bin",
            #"HEVC/lp_main/Johnny_1280x720_60_qp32.bin",
            "HEVC/lp_main/Johnny_1280x720_60_qp37.bin",
            #"HEVC/lp_main/Kimono1_1920x1080_24_qp22.bin",
            #"HEVC/lp_main/Kimono1_1920x1080_24_qp27.bin",
            #"HEVC/lp_main/Kimono1_1920x1080_24_qp32.bin",
            "HEVC/lp_main/Kimono1_1920x1080_24_qp37.bin",
            #"HEVC/lp_main/KristenAndSara_1280x720_60_qp22.bin",
            #"HEVC/lp_main/KristenAndSara_1280x720_60_qp27.bin",
            #"HEVC/lp_main/KristenAndSara_1280x720_60_qp32.bin",
            "HEVC/lp_main/KristenAndSara_1280x720_60_qp37.bin",
            #"HEVC/lp_main/NebutaFestival_2560x1600_60_10bit_crop_qp22.bin",
            #"HEVC/lp_main/NebutaFestival_2560x1600_60_10bit_crop_qp27.bin",
            #"HEVC/lp_main/NebutaFestival_2560x1600_60_10bit_crop_qp32.bin",
            "HEVC/lp_main/NebutaFestival_2560x1600_60_10bit_crop_qp37.bin",
            #"HEVC/lp_main/ParkScene_1920x1080_24_qp22.bin",
            #"HEVC/lp_main/ParkScene_1920x1080_24_qp27.bin",
            #"HEVC/lp_main/ParkScene_1920x1080_24_qp32.bin",
            "HEVC/lp_main/ParkScene_1920x1080_24_qp37.bin",
            #"HEVC/lp_main/PartyScene_832x480_50_qp22.bin",
            #"HEVC/lp_main/PartyScene_832x480_50_qp27.bin",
            #"HEVC/lp_main/PartyScene_832x480_50_qp32.bin",
            "HEVC/lp_main/PartyScene_832x480_50_qp37.bin",
            #"HEVC/lp_main/PeopleOnStreet_2560x1600_30_crop_qp22.bin",
            #"HEVC/lp_main/PeopleOnStreet_2560x1600_30_crop_qp27.bin",
            #"HEVC/lp_main/PeopleOnStreet_2560x1600_30_crop_qp32.bin",
            "HEVC/lp_main/PeopleOnStreet_2560x1600_30_crop_qp37.bin",
            #"HEVC/lp_main/RaceHorses_416x240_30_qp22.bin",
            #"HEVC/lp_main/RaceHorses_416x240_30_qp27.bin",
            #"HEVC/lp_main/RaceHorses_416x240_30_qp32.bin",
            "HEVC/lp_main/RaceHorses_416x240_30_qp37.bin",
            #"HEVC/lp_main/RaceHorses_832x480_30_qp22.bin",
            #"HEVC/lp_main/RaceHorses_832x480_30_qp27.bin",
            #"HEVC/lp_main/RaceHorses_832x480_30_qp32.bin",
            "HEVC/lp_main/RaceHorses_832x480_30_qp37.bin",
            #"HEVC/lp_main/SlideEditing_1280x720_30_qp22.bin",
            #"HEVC/lp_main/SlideEditing_1280x720_30_qp27.bin",
            #"HEVC/lp_main/SlideEditing_1280x720_30_qp32.bin",
            "HEVC/lp_main/SlideEditing_1280x720_30_qp37.bin",
            #"HEVC/lp_main/SlideShow_1280x720_20_qp22.bin",
            #"HEVC/lp_main/SlideShow_1280x720_20_qp27.bin",
            #"HEVC/lp_main/SlideShow_1280x720_20_qp32.bin",
            "HEVC/lp_main/SlideShow_1280x720_20_qp37.bin",
            #"HEVC/lp_main/SteamLocomotiveTrain_2560x1600_60_10bit_crop_qp22.bin",
            #"HEVC/lp_main/SteamLocomotiveTrain_2560x1600_60_10bit_crop_qp27.bin",
            #"HEVC/lp_main/SteamLocomotiveTrain_2560x1600_60_10bit_crop_qp32.bin",
            "HEVC/lp_main/SteamLocomotiveTrain_2560x1600_60_10bit_crop_qp37.bin",
            #"HEVC/lp_main/Traffic_2560x1600_30_crop_qp22.bin",
            #"HEVC/lp_main/Traffic_2560x1600_30_crop_qp27.bin",
            #"HEVC/lp_main/Traffic_2560x1600_30_crop_qp32.bin",
            "HEVC/lp_main/Traffic_2560x1600_30_crop_qp37.bin"
        ],

        # HEVC Intra
        "hevcIntra" : [
            #"HEVC/i_main/BasketballDrill_832x480_50_qp22.bin",
            #"HEVC/i_main/BasketballDrill_832x480_50_qp27.bin",
            #"HEVC/i_main/BasketballDrill_832x480_50_qp32.bin",
            "HEVC/i_main/BasketballDrill_832x480_50_qp37.bin",
            #"HEVC/i_main/BasketballDrillText_832x480_50_qp22.bin",
            #"HEVC/i_main/BasketballDrillText_832x480_50_qp27.bin",
            #"HEVC/i_main/BasketballDrillText_832x480_50_qp32.bin",
            "HEVC/i_main/BasketballDrillText_832x480_50_qp37.bin",
            #"HEVC/i_main/BasketballDrive_1920x1080_50_qp22.bin",
            #"HEVC/i_main/BasketballDrive_1920x1080_50_qp27.bin",
            #"HEVC/i_main/BasketballDrive_1920x1080_50_qp32.bin",
            "HEVC/i_main/BasketballDrive_1920x1080_50_qp37.bin",
            #"HEVC/i_main/BasketballPass_416x240_50_qp22.bin",
            #"HEVC/i_main/BasketballPass_416x240_50_qp27.bin",
            #"HEVC/i_main/BasketballPass_416x240_50_qp32.bin",
            "HEVC/i_main/BasketballPass_416x240_50_qp37.bin",
            #"HEVC/i_main/BlowingBubbles_416x240_50_qp22.bin",
            #"HEVC/i_main/BlowingBubbles_416x240_50_qp27.bin",
            #"HEVC/i_main/BlowingBubbles_416x240_50_qp32.bin",
            "HEVC/i_main/BlowingBubbles_416x240_50_qp37.bin",
            #"HEVC/i_main/BQMall_832x480_60_qp22.bin",
            #"HEVC/i_main/BQMall_832x480_60_qp27.bin",
            #"HEVC/i_main/BQMall_832x480_60_qp32.bin",
            "HEVC/i_main/BQMall_832x480_60_qp37.bin",
            #"HEVC/i_main/BQSquare_416x240_60_qp22.bin",
            #"HEVC/i_main/BQSquare_416x240_60_qp27.bin",
            #"HEVC/i_main/BQSquare_416x240_60_qp32.bin",
            "HEVC/i_main/BQSquare_416x240_60_qp37.bin",
            #"HEVC/i_main/BQTerrace_1920x1080_60_qp22.bin",
            #"HEVC/i_main/BQTerrace_1920x1080_60_qp27.bin",
            #"HEVC/i_main/BQTerrace_1920x1080_60_qp32.bin",
            "HEVC/i_main/BQTerrace_1920x1080_60_qp37.bin",
            #"HEVC/i_main/Cactus_1920x1080_50_qp22.bin",
            #"HEVC/i_main/Cactus_1920x1080_50_qp27.bin",
            #"HEVC/i_main/Cactus_1920x1080_50_qp32.bin",
            "HEVC/i_main/Cactus_1920x1080_50_qp37.bin",
            #"HEVC/i_main/ChinaSpeed_1024x768_30_qp22.bin",
            #"HEVC/i_main/ChinaSpeed_1024x768_30_qp27.bin",
            #"HEVC/i_main/ChinaSpeed_1024x768_30_qp32.bin",
            "HEVC/i_main/ChinaSpeed_1024x768_30_qp37.bin",
            #"HEVC/i_main/FourPeople_1280x720_60_qp22.bin",
            #"HEVC/i_main/FourPeople_1280x720_60_qp27.bin",
            #"HEVC/i_main/FourPeople_1280x720_60_qp32.bin",
            "HEVC/i_main/FourPeople_1280x720_60_qp37.bin",
            #"HEVC/i_main/Johnny_1280x720_60_qp22.bin",
            #"HEVC/i_main/Johnny_1280x720_60_qp27.bin",
            #"HEVC/i_main/Johnny_1280x720_60_qp32.bin",
            "HEVC/i_main/Johnny_1280x720_60_qp37.bin",
            #"HEVC/i_main/Kimono1_1920x1080_24_qp22.bin",
            #"HEVC/i_main/Kimono1_1920x1080_24_qp27.bin",
            #"HEVC/i_main/Kimono1_1920x1080_24_qp32.bin",
            "HEVC/i_main/Kimono1_1920x1080_24_qp37.bin",
            #"HEVC/i_main/KristenAndSara_1280x720_60_qp22.bin",
            #"HEVC/i_main/KristenAndSara_1280x720_60_qp27.bin",
            #"HEVC/i_main/KristenAndSara_1280x720_60_qp32.bin",
            "HEVC/i_main/KristenAndSara_1280x720_60_qp37.bin",
            #"HEVC/i_main/NebutaFestival_2560x1600_60_10bit_crop_qp22.bin",
            #"HEVC/i_main/NebutaFestival_2560x1600_60_10bit_crop_qp27.bin",
            #"HEVC/i_main/NebutaFestival_2560x1600_60_10bit_crop_qp32.bin",
            "HEVC/i_main/NebutaFestival_2560x1600_60_10bit_crop_qp37.bin",
            #"HEVC/i_main/ParkScene_1920x1080_24_qp22.bin",
            #"HEVC/i_main/ParkScene_1920x1080_24_qp27.bin",
            #"HEVC/i_main/ParkScene_1920x1080_24_qp32.bin",
            "HEVC/i_main/ParkScene_1920x1080_24_qp37.bin",
            #"HEVC/i_main/PartyScene_832x480_50_qp22.bin",
            #"HEVC/i_main/PartyScene_832x480_50_qp27.bin",
            #"HEVC/i_main/PartyScene_832x480_50_qp32.bin",
            "HEVC/i_main/PartyScene_832x480_50_qp37.bin",
            #"HEVC/i_main/PeopleOnStreet_2560x1600_30_crop_qp22.bin",
            #"HEVC/i_main/PeopleOnStreet_2560x1600_30_crop_qp27.bin",
            #"HEVC/i_main/PeopleOnStreet_2560x1600_30_crop_qp32.bin",
            "HEVC/i_main/PeopleOnStreet_2560x1600_30_crop_qp37.bin",
            #"HEVC/i_main/RaceHorses_416x240_30_qp22.bin",
            #"HEVC/i_main/RaceHorses_416x240_30_qp27.bin",
            #"HEVC/i_main/RaceHorses_416x240_30_qp32.bin",
            "HEVC/i_main/RaceHorses_416x240_30_qp37.bin",
            #"HEVC/i_main/RaceHorses_832x480_30_qp22.bin",
            #"HEVC/i_main/RaceHorses_832x480_30_qp27.bin",
            #"HEVC/i_main/RaceHorses_832x480_30_qp32.bin",
            "HEVC/i_main/RaceHorses_832x480_30_qp37.bin",
            #"HEVC/i_main/SlideEditing_1280x720_30_qp22.bin",
            #"HEVC/i_main/SlideEditing_1280x720_30_qp27.bin",
            #"HEVC/i_main/SlideEditing_1280x720_30_qp32.bin",
            "HEVC/i_main/SlideEditing_1280x720_30_qp37.bin",
            #"HEVC/i_main/SlideShow_1280x720_20_qp22.bin",
            #"HEVC/i_main/SlideShow_1280x720_20_qp27.bin",
            #"HEVC/i_main/SlideShow_1280x720_20_qp32.bin",
            "HEVC/i_main/SlideShow_1280x720_20_qp37.bin",
            #"HEVC/i_main/SteamLocomotiveTrain_2560x1600_60_10bit_crop_qp22.bin",
            #"HEVC/i_main/SteamLocomotiveTrain_2560x1600_60_10bit_crop_qp27.bin",
            #"HEVC/i_main/SteamLocomotiveTrain_2560x1600_60_10bit_crop_qp32.bin",
            "HEVC/i_main/SteamLocomotiveTrain_2560x1600_60_10bit_crop_qp37.bin",
            #"HEVC/i_main/Traffic_2560x1600_30_crop_qp22.bin",
            #"HEVC/i_main/Traffic_2560x1600_30_crop_qp27.bin",
            #"HEVC/i_main/Traffic_2560x1600_30_crop_qp32.bin",
            "HEVC/i_main/Traffic_2560x1600_30_crop_qp37.bin"
        ],

        # HEVC conf
        "hevcConf" : [
            #"HEVC/jctvc/avconv/AMP_A_Samsung_4.bit",
            #"HEVC/jctvc/avconv/AMP_B_Samsung_4.bit",
            "HEVC/jctvc/avconv/AMP_D_Hisilicon_3.bit",
            "HEVC/jctvc/avconv/AMP_E_Hisilicon_3.bit",
            "HEVC/jctvc/avconv/AMP_F_Hisilicon_3.bit",
            "HEVC/jctvc/avconv/AMVP_A_MTK_4.bit",
            "HEVC/jctvc/avconv/AMVP_B_MTK_4.bit",
            #"HEVC/jctvc/avconv/AMVP_C_Samsung_4.bit",
            "HEVC/jctvc/avconv/CAINIT_A_SHARP_4.bit",
            "HEVC/jctvc/avconv/CAINIT_B_SHARP_4.bit",
            "HEVC/jctvc/avconv/CAINIT_C_SHARP_3.bit",
            "HEVC/jctvc/avconv/CAINIT_D_SHARP_3.bit",
            "HEVC/jctvc/avconv/CAINIT_E_SHARP_3.bit",
            "HEVC/jctvc/avconv/CAINIT_F_SHARP_3.bit",
            #"HEVC/jctvc/avconv/CAINIT_G_SHARP_3.bit",
            #"HEVC/jctvc/avconv/CAINIT_H_SHARP_3.bit",
            #"HEVC/jctvc/avconv/CIP_A_Panasonic_3.bit",
            "HEVC/jctvc/avconv/cip_B_NEC_2.bit",
            #"HEVC/jctvc/avconv/CIP_C_Panasonic_2.bit",
            #"HEVC/jctvc/avconv/DBLK_A_MAIN10_VIXS_2.bit",
            #"HEVC/jctvc/avconv/DBLK_A_SONY_3.bit",
            #"HEVC/jctvc/avconv/DBLK_B_SONY_3.bit",
            #"HEVC/jctvc/avconv/DBLK_C_SONY_3.bit",
            #"HEVC/jctvc/avconv/DBLK_D_VIXS_2.bit",
            #"HEVC/jctvc/avconv/DBLK_E_VIXS_2.bit",
            #"HEVC/jctvc/avconv/DBLK_F_VIXS_2.bit",
            #"HEVC/jctvc/avconv/DBLK_G_VIXS_2.bit",
            #"HEVC/jctvc/avconv/DELTAQP_A_BRCM_4.bit",
            #"HEVC/jctvc/avconv/DELTAQP_B_SONY_3.bit",
            #"HEVC/jctvc/avconv/DELTAQP_C_SONY_3.bit",
            #"HEVC/jctvc/avconv/DSLICE_A_HHI_5.bin",
            #"HEVC/jctvc/avconv/DSLICE_B_HHI_5.bin",
            #"HEVC/jctvc/avconv/DSLICE_C_HHI_5.bin",
            #"HEVC/jctvc/avconv/ENTP_A_LG_2.bin",
            "HEVC/jctvc/avconv/ENTP_B_LG_2.bin",
            "HEVC/jctvc/avconv/ENTP_C_LG_3.bin",
            #"HEVC/jctvc/avconv/EXT_A_ericsson_3.bit",
            #"HEVC/jctvc/avconv/HRD_A_Fujitsu_2.bin",
            #"HEVC/jctvc/avconv/ipcm_A_NEC_3.bit",
            #"HEVC/jctvc/avconv/ipcm_B_NEC_3.bit",
            #"HEVC/jctvc/avconv/ipcm_C_NEC_3.bit",
            #"HEVC/jctvc/avconv/ipcm_D_NEC_3.bit",
            #"HEVC/jctvc/avconv/ipcm_E_NEC_2.bit",
            "HEVC/jctvc/avconv/IPRED_A_docomo_2.bit",
            #"HEVC/jctvc/avconv/IPRED_B_Nokia_3.bit",
            "HEVC/jctvc/avconv/IPRED_C_Mitsubishi_2.bit",
            #"HEVC/jctvc/avconv/LS_A_Orange_2.bit",
            #"HEVC/jctvc/avconv/LS_B_ORANGE_3.bit",
            #"HEVC/jctvc/avconv/MAXBINS_A_TI_4.bit",
            #"HEVC/jctvc/avconv/MAXBINS_B_TI_4.bit",
            #"HEVC/jctvc/avconv/MAXBINS_C_TI_4.bit",
            "HEVC/jctvc/avconv/MERGE_A_TI_3.bit",
            "HEVC/jctvc/avconv/MERGE_B_TI_3.bit",
            "HEVC/jctvc/avconv/MERGE_C_TI_3.bit",
            "HEVC/jctvc/avconv/MERGE_D_TI_3.bit",
            "HEVC/jctvc/avconv/MERGE_E_TI_3.bit",
            "HEVC/jctvc/avconv/MERGE_F_MTK_4.bit",
            "HEVC/jctvc/avconv/MERGE_G_HHI_4.bit",
            "HEVC/jctvc/avconv/MVCLIP_A_qualcomm_3.bit",
            #"HEVC/jctvc/avconv/MVDL1ZERO_A_docomo_3.bit",
            "HEVC/jctvc/avconv/MVEDGE_A_qualcomm_3.bit",
            #"HEVC/jctvc/avconv/NUT_A_ericsson_4.bit",
            #"HEVC/jctvc/avconv/PICSIZE_A_Bossen_1.bin",
            #"HEVC/jctvc/avconv/PICSIZE_B_Bossen_1.bin",
            #"HEVC/jctvc/avconv/PICSIZE_C_Bossen_1.bin",
            #"HEVC/jctvc/avconv/PICSIZE_D_Bossen_1.bin",
            "HEVC/jctvc/avconv/PMERGE_A_TI_3.bit",
            "HEVC/jctvc/avconv/PMERGE_B_TI_3.bit",
            "HEVC/jctvc/avconv/PMERGE_C_TI_3.bit",
            "HEVC/jctvc/avconv/PMERGE_D_TI_3.bit",
            "HEVC/jctvc/avconv/PMERGE_E_TI_3.bit",
            "HEVC/jctvc/avconv/POC_A_Bossen_3.bin",
            #"HEVC/jctvc/avconv/PPS_A_qualcomm_7.bit",
            "HEVC/jctvc/avconv/PS_A_VIDYO_3.bit",
            "HEVC/jctvc/avconv/PS_B_VIDYO_3.bit",
            #"HEVC/jctvc/avconv/RAP_A_docomo_4.bit",
            #"HEVC/jctvc/avconv/RAP_B_Bossen_1.bin",
            "HEVC/jctvc/avconv/RPLM_A_qualcomm_4.bit",
            #"HEVC/jctvc/avconv/RPLM_B_qualcomm_4.bit",
            "HEVC/jctvc/avconv/RPS_A_docomo_4.bit",
            #"HEVC/jctvc/avconv/RPS_B_qualcomm_5.bit",
            #"HEVC/jctvc/avconv/RPS_C_ericsson_4.bit",
            #"HEVC/jctvc/avconv/RPS_D_ericsson_5.bit",
            #"HEVC/jctvc/avconv/RPS_E_qualcomm_5.bit",
            #"HEVC/jctvc/avconv/RPS_F_docomo_1.bit",
            "HEVC/jctvc/avconv/RQT_A_HHI_4.bit",
            "HEVC/jctvc/avconv/RQT_B_HHI_4.bit",
            "HEVC/jctvc/avconv/RQT_C_HHI_4.bit",
            "HEVC/jctvc/avconv/RQT_D_HHI_4.bit",
            "HEVC/jctvc/avconv/RQT_E_HHI_4.bit",
            "HEVC/jctvc/avconv/RQT_F_HHI_4.bit",
            "HEVC/jctvc/avconv/RQT_G_HHI_4.bit",
            "HEVC/jctvc/avconv/SAO_A_MediaTek_4.bit",
            #"HEVC/jctvc/avconv/SAO_B_MediaTek_5.bit",
            "HEVC/jctvc/avconv/SAO_C_Samsung_4.bin",
            "HEVC/jctvc/avconv/SAO_D_Samsung_4.bin",
            "HEVC/jctvc/avconv/SAO_E_Canon_4.bit",
            "HEVC/jctvc/avconv/SAO_F_Canon_3.bit",
            "HEVC/jctvc/avconv/SAO_G_Canon_3.bit",
            #"HEVC/jctvc/avconv/SDH_A_Orange_3.bit",
            #"HEVC/jctvc/avconv/SLICES_A_Rovi_3.bin",
            "HEVC/jctvc/avconv/SLIST_A_Sony_4.bin",
            "HEVC/jctvc/avconv/SLIST_B_Sony_8.bin",
            "HEVC/jctvc/avconv/SLIST_C_Sony_3.bin",
            "HEVC/jctvc/avconv/SLIST_D_Sony_9.bin",
            "HEVC/jctvc/avconv/STRUCT_A_Samsung_5.bin",
            #"HEVC/jctvc/avconv/STRUCT_B_Samsung_4.bit",
            "HEVC/jctvc/avconv/TILES_A_Cisco_2.bin",
            #"HEVC/jctvc/avconv/TILES_B_Cisco_1.bin",
            "HEVC/jctvc/avconv/TMVP_A_MS_3.bit",
            #"HEVC/jctvc/avconv/TSCL_A_VIDYO_5.bit",
            "HEVC/jctvc/avconv/TSCL_B_VIDYO_4.bit",
            "HEVC/jctvc/avconv/TSKIP_A_MS_3.bit",
            #"HEVC/jctvc/avconv/TUSIZE_A_Samsung_1.bin",
            #"HEVC/jctvc/avconv/WP_A_MAIN10_Toshiba_3.bit",
            "HEVC/jctvc/avconv/WP_A_Toshiba_3.bit",
            "HEVC/jctvc/avconv/WP_B_Toshiba_3.bit",
            #"HEVC/jctvc/avconv/WP_MAIN10_B_Toshiba_3.bit",
            #"HEVC/jctvc/avconv/WPP_A_ericsson_MAIN10_2.bit",
            #"HEVC/jctvc/avconv/WPP_A_ericsson_MAIN_2.bit",
            #"HEVC/jctvc/avconv/WPP_B_ericsson_MAIN10_2.bit",
            #"HEVC/jctvc/avconv/WPP_B_ericsson_MAIN_2.bit",
            #"HEVC/jctvc/avconv/WPP_C_ericsson_MAIN10_2.bit",
            #"HEVC/jctvc/avconv/WPP_C_ericsson_MAIN_2.bit",
            #"HEVC/jctvc/avconv/WPP_D_ericsson_MAIN10_2.bit",
            #"HEVC/jctvc/avconv/WPP_D_ericsson_MAIN_2.bit",
            #"HEVC/jctvc/avconv/WPP_E_ericsson_MAIN10_2.bit",
            #"HEVC/jctvc/avconv/WPP_E_ericsson_MAIN_2.bit",
            #"HEVC/jctvc/avconv/WPP_F_ericsson_MAIN10_2.bit",
            #"HEVC/jctvc/avconv/WPP_F_ericsson_MAIN_2.bit",
        ]

    }

    fileList_reduce = {
        "mpeg" : [
            "MPEG4/SIMPLE/P-VOP/hit001.m4v",
            "MPEG4/foreman_qcif_30.bit"
        ],

        "avc" : [
            "AVC/CAVLC/general/AVCNL-1/NL1_Sony_D.jsv",
            "AVC/CAVLC/MMCO/AVCMR-11/HCBP1_HHI_A.264"
        ],

        "hevc" : [
            "HEVC/lp_main/BasketballPass_416x240_50_qp22.bin",
            "HEVC/ld_main/Traffic_2560x1600_30_crop_qp22.bin"
        ],

        "hevcIntra" : [
            "HEVC/i_main/BasketballPass_416x240_50_qp22.bin",
            "HEVC/i_main/Traffic_2560x1600_30_crop_qp22.bin"
        ],

        "hevcConf" : [
        ]
    }


def main():
    clArguments = parser.parse_args()

    #print clArguments
    #sys.exit(0)

    errorsCount = 0
    warningsCount = 0

    execPath = []

    # Build the command line for Jade execution
    if clArguments.useJade :
        if clArguments.topXdf == None or not os.path.isfile(clArguments.topXdf):
            sys.exit("Please use -xdf argument to set the path of a top network")
        elif clArguments.vtl == None or not os.path.isdir(clArguments.vtl):
            sys.exit("Please use -vtl argument to set the path of a VTL folder")
        else:
            if clArguments.executable != None:
                execPath.append(clArguments.executable)
            else:
                execPath.append("Jade")
            execPath.extend(["-xdf", clArguments.topXdf, "-L", clArguments.vtl])

        if clArguments.loopNumber != None:
            print "Warning : By default, Jade read only one time the input file. The -l value you passed will be ignored."

        if not clArguments.enableDisplay:
            execPath.append("-nodisplay")

    # Build the command line for standalone decoder
    elif clArguments.useClassic:
        if clArguments.executable == None:
            sys.exit("Please use -e argument to set the path of a decoder")
        elif not os.path.isfile(clArguments.executable) or not os.access(clArguments.executable, os.X_OK):
            sys.exit(clArguments.executable + " must be an executable file !")
        else:
            execPath.append(clArguments.executable)

        # Set the max loops number
        if clArguments.loopNumber != None:
            execPath.extend(["-l", str(clArguments.loopNumber)])

        # Disable display
        if not clArguments.enableDisplay:
            execPath.append("-n")

    # Check validity of "sequences" directory
    if not os.path.isdir(clArguments.sequences):
        sys.exit("The sequence path must be a valid directory, containing sequences")

    if clArguments.quickTest:
        fileList = fileList_reduce
    else:
        fileList = fileList_all

    if not fileList.has_key(clArguments.filesKey) :
       clArguments.filesKey = DEFAULT_FILE_LIST

    for file in fileList[clArguments.filesKey]:
        file = file.replace("/", os.sep)
        inputFile = file
        outputFile = '.'.join(file.split('.')[:-1]) + ".yuv"

        inputPath = clArguments.sequences + os.sep + inputFile
        outputPath = clArguments.sequences + os.sep + outputFile

        if not os.path.exists(inputPath):
            print "Warning : input file", inputPath, "does not exists"
            warningsCount += 1
            continue
        elif not os.access(inputPath, os.R_OK):
            print "Warning : input file", inputPath, "is not readable"
            warningsCount += 1
            continue

        if not clArguments.skipYuv:
            if not os.path.exists(outputPath):
                print "Warning : output file", outputPath, "does not exists"
                warningsCount += 1
                continue
            elif not os.access(outputPath, os.R_OK):
                print "Warning : output file", outputPath, "is not readable"
                warningsCount += 1
                continue

        finalCommandLine = list(execPath)

        finalCommandLine.extend(["-i", inputPath])

        traceMsg = "Try to decode " + inputFile

        if not clArguments.skipYuv:
            finalCommandLine.extend(["-o", outputPath])
            traceMsg += " and check consistency with " + outputFile + ":"

        if clArguments.verbose:
            print " ".join(finalCommandLine)

        print traceMsg
        commandResult = subprocess.call(finalCommandLine)

        if commandResult != 0:
            sys.stderr.write("Error, command returned code " + str(commandResult))
            errorsCount += 1

    if errorsCount != 0:
        ws, es = "", ""
        if errorsCount > 1 : es = "s"
        if warningsCount > 1 : ws = "s"
        sys.exit("The test suite finished with " + str(errorsCount) + " error"+es+" and " + str(warningsCount) + " warning"+ws+".")
    elif warningsCount != 0:
        s = ""
        if warningsCount > 1 : s = "s"
        print "The test suite finished with no error but", warningsCount, "warning"+s+"."
        sys.exit()
    else :
        print "The test suite finished with no error !"
        sys.exit()


def setupCommandLine():
    # Help on arparse usage module : http://docs.python.org/library/argparse.html#module-argparse
    global parser

    parser = argparse.ArgumentParser(description='Execute parser to test video decoding', version=VERSION)

    options = parser.add_argument_group(title="Parameters")

    mode = options.add_mutually_exclusive_group(required=True)
    mode.add_argument("-jade", action="store_true", default=False, dest="useJade")
    mode.add_argument("-classic", action="store_true", default=False, dest="useClassic")

    jade = parser.add_argument_group("Parameters for -jade mode", "Test a decoder in LLVM with Jade toolchain")
    jade.add_argument("-xdf", action="store", dest="topXdf",
                            help="Path to the Top_*.xdf network of the decoder")
    jade.add_argument("-vtl", action="store", dest="vtl",
                            help="Path to the VTL directory of the decoder")

    classic = parser.add_argument_group("Parameters for -classic mode", "Test a classic C decoder")
    classic.add_argument("-l", "--loops", type=int, action="store", dest="loopNumber",
                        help="Number of times input is read for every file")

    options.add_argument("-e", "--executable", action="store", dest="executable",
                        help="In -classic mode, path to a decoder. In -jade mode, path to Jade executable.")
    options.add_argument("-s", "--sequences", action="store", dest="sequences", required=True,
                        help="Path to directory containing sequences (ie : containing MPEG4/AVC/etc. folder).")
    options.add_argument("-n", "--nodisplay", action="store_false", dest="enableDisplay", default=True,
                        help="Pass this argument to disable display when testing decoders.")
    options.add_argument("-f", "--filestypes", choices=["mpeg","avc","hevc","hevcIntra", "hevcConf"], default=DEFAULT_FILE_LIST, dest="filesKey",
                        help="Set the type of videos to test (default='"+DEFAULT_FILE_LIST+"')")
    options.add_argument("-q", "--quick", action="store_true", dest="quickTest", default=False,
                        help="Test the decoder on a small subset of sequences.")
    options.add_argument("--skip-yuv", action="store_true", dest="skipYuv", default=False,
                        help="Skip the consistency checking using the YUV file.")
    options.add_argument("--verbose", action="store_true", dest="verbose", default=False,
                        help="Verbose mode.")


if __name__ == "__main__":
    setupCommandLine()
    computeFileList()
    main()
