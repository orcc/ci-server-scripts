#!/usr/bin/ruby
require 'fileutils'
###############################################################################
# Constant
###############################################################################
#AVC_BIN2     = "Top_AVC_FREXT_decoder"
AVC_BIN2     = "New_Top_AVC_FREXT"
AVC_BIN     = "Top_mpeg4_part10_CBP_decoder"
AVC_BIN_DIR = "#{ENV['HOME']}/Work/workspace/projects/C/build-generated/#{AVC_BIN2}"
SOURCE_DIR  = "#{ENV['HOME']}/Images/01-Sequences/02-VideoSource/Rec._ITU-T_H.264.1_Base_Ext_Main_profiles_bitstreams"
SOURCE2_DIR  = "#{ENV['HOME']}/Images/01-Sequences/02-VideoSource/jvt_conformance_frext"
###############################################################################
# Global
###############################################################################
listPatternFiles = [
  "NL1_Sony_D.jsv" , "SVA_NL1_B.264" , "NL2_Sony_H.jsv" , "SVA_NL2_E.264"    , "LS_SVA_D.264"   ,
  "BA1_Sony_D.jsv" , "SVA_BA1_B.264" , "BA2_Sony_F.jsv" , "SVA_BA2_D.264"    , "BA_MW_D.264"    ,
  "BANM_MW_D.264"  , "BA1_FT_C.264"  , "NLMQ1_JVC_C.264", "NLMQ2_JVC_C.264"  , "BAMQ1_JVC_C.264",
  "BAMQ2_JVC_C.264", "SVA_Base_B.264", "SVA_FM1_E.264"  , "BASQP1_Sony_C.jsv",
#  "FM1_BT_B.h264" , "FM2_SVA_C.264" , "FM1_FT_E.264"   ,
  "CI_MW_D.264"    , "SVA_CL1_E.264" , "CI1_FT_B.264"   , "AUD_MW_E.264"     , "MIDR_MW_D.264"  ,
  "NRF_MW_E.264", "MPS_MW_A.264"
]

listFrextPatternFiles = [
  "FRExt1_Panasonic_D.avc" ,
#  "FRExt3_Panasonic_E.avc" ,
 "HPCV_BRCM_A.264" ,
 "freh1_b.264" ,
  "HPCVNL_BRCM_A.264"      ,
# "HCAFR2_HHI_A.264"  ,
# "HCAFR2_HHI_A.264"
]

listCabacPatternFiles = [
#  "CANL1_TOSHIBA_G.264", "CANL1_Sony_E.jsv", "CANL2_Sony_E.jsv" ,
#  "CANL3_Sony_C.jsv", # Slice B
#  "CANL1_SVA_B.264", "CANL2_SVA_B.264", "CANL3_SVA_B.264",
#  "CANL4_SVA_B.264",  # Slice B
#  "CABA1_Sony_D.jsv", "CABA2_Sony_E.jsv",
#  "CABA3_Sony_C.jsv", # Slice B
#  "CABA3_TOSHIBA_E.264", "CABA1_SVA_B.264", "CABA2_SVA_B.264", 
#  "CABA3_SVA_B.264",
## "camp_mot_frm0_full.26l",
#  "CABACI3_Sony_B.jsv",  # Slice B
#  "CAQP1_Sony_B.jsv",
#  "CABAST3_Sony_E.jsv", "CABASTBR3_Sony_B.jsv", # Slice B
  "CACQP3_Sony_D.jsv",
  "MR9_BT_B.h264",
  "HCMP1_HHI_A.264"
]

###############################################################################
# getopts
###############################################################################
def getopts (argv)
  for i in (0..argv.size) do
    case argv[i]
    when "-c" : compileBin()
    end
  end
end
###############################################################################
# cleanFile
###############################################################################
def cleanFile()
  liste_file = Dir.glob("*~")
  liste_file.each { |file| File.delete(file) }
end
###############################################################################
# getListZipFiles
###############################################################################
def getListZipFiles (source_dir )
  pwd   = Dir.pwd
  Dir.chdir(source_dir)
  list  = Dir.glob("*.zip")
  Dir.chdir(pwd)
  return list
end
###############################################################################
# compileBin
###############################################################################
def compileBin ( )
  pwd   = Dir.pwd
  Dir.chdir(AVC_BIN_DIR)
  cmd    = "make clean; make -j2"
  system(cmd)
#  ret    = IO.popen(cmd).readlines
  Dir.chdir(pwd)
end
###############################################################################
# extractZipFiles
###############################################################################
def extractZipFiles ( source_dir, zipName )
  cleanZipFiles(zipName) if File.exists?(zipName)
  cmd    = "unzip -d #{zipName} #{source_dir}/#{zipName}.zip"
  ret    = IO.popen(cmd).readlines
end
###############################################################################
# getH264File
###############################################################################
def getH264File ( dir )
  pwd   = Dir.pwd
  Dir.chdir(dir)
  list  = Dir.glob("*.h264")
  list  = Dir.glob("*.26l") if list.size() == 0
  list  = Dir.glob("*.264") if list.size() == 0
  list  = Dir.glob("*.jsv") if list.size() == 0
  list  = Dir.glob("*.avc") if list.size() == 0
  Dir.chdir(pwd)
  return list
end
###############################################################################
# getYUVFile
###############################################################################
def getYUVFile ( dir )
  pwd   = Dir.pwd
  Dir.chdir(dir)
  list  = Dir.glob("*.yuv")
  list  = Dir.glob("*.YUV")  if list.size() == 0
  list  = Dir.glob("*.qcif") if list.size() == 0
  Dir.chdir(pwd)
  return list
end
###############################################################################
# cleanZipFiles
###############################################################################
def cleanZipFiles ( zipName )
  cmd = "rm -r #{zipName}"
  system(cmd)
end
###############################################################################
# runPattern
###############################################################################
def runPattern ( patternName )
  yuv     = getYUVFile(patternName)
  h264    = getH264File(patternName)
  cmd     = "#{AVC_BIN_DIR}/#{AVC_BIN} -i #{patternName}/#{h264}"
  cmd    += " -o #{patternName}/#{yuv} -l 2"
  puts cmd
  retCmd  = IO.popen(cmd).readlines
  regex2 = Regexp.new("no error")
  filters = ["image", "error"]
  filters.each do |filter|
    regex = Regexp.new(filter)
    retCmd.each do |line|
      ret = regex.match(line)
      if ret != nil then
	if filter == "error" then
	  ret = regex2.match(line)
	  if ret == nil then
	    puts line
	    exit
	  end
	else
	  puts line
	end
      end
    end
  end
end
###############################################################################
# runAll
###############################################################################
def runAll ( source_dir, zipName )
  extractZipFiles(source_dir, zipName)
  runPattern(zipName)
  cleanZipFiles(zipName)
end

###############################################################################
# main
###############################################################################
cleanFile()
getopts(ARGV)
cptPattern = 1
listZipFiles = getListZipFiles(SOURCE_DIR)
listPatternFiles.each do |pattern|
  patternExt   = File.extname(pattern)
  patternName  = File.basename(pattern, patternExt)
  listZipFiles.each do |zip|
    zipExt   = File.extname(zip)
    zipName  = File.basename(zip, zipExt)
    if zipName == patternName then
      puts "============================================================="
      puts "== #{cptPattern}/#{listPatternFiles.size()} == #{zipName}"
      puts "============================================================="
      runAll(SOURCE_DIR, zipName)
      cptPattern += 1
    end
  end
end

# FREXT
cptPattern = 1
listZipFiles = getListZipFiles(SOURCE2_DIR)
listFrextPatternFiles.each do |pattern|
  patternExt   = File.extname(pattern)
  patternName  = File.basename(pattern, patternExt)
  listZipFiles.each do |zip|
    zipExt   = File.extname(zip)
    zipName  = File.basename(zip, zipExt)
    if zipName == patternName then
      puts "============================================================="
      puts "== #{cptPattern}/#{listFrextPatternFiles.size()} == #{zipName}"
      puts "============================================================="
      runAll(SOURCE2_DIR, zipName)
      cptPattern += 1
    end
  end
end

# CABAC 
cptPattern = 1
listZipFiles = getListZipFiles(SOURCE_DIR)
listCabacPatternFiles.each do |pattern|
  patternExt   = File.extname(pattern)
  patternName  = File.basename(pattern, patternExt)
  listZipFiles.each do |zip|
    zipExt   = File.extname(zip)
    zipName  = File.basename(zip, zipExt)
    if zipName == patternName then
      puts "============================================================="
      puts "== #{cptPattern}/#{listCabacPatternFiles.size()} == #{zipName}"
      puts "============================================================="
#      runAll(SOURCE_DIR, zipName)
      cptPattern += 1
    end
  end
end
