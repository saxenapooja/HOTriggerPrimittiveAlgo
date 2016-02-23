import FWCore.ParameterSet.Config as cms
process = cms.Process('TEST')

process.source = cms.Source("PoolSource",
	fileNames = cms.untracked.vstring(
            "/store/data/Run2015B/SingleMuon/RAW/v1/000/251/721/00000/061A67FD-412A-E511-AE36-02163E0133B5.root"
        ),
)

process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(100))

process.load('Configuration.StandardSequences.Services_cff')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.StandardSequences.RawToDigi_Data_cff')
process.load('SimCalorimetry.HcalTrigPrimProducers.hcaltpdigi_cff')
process.load("Configuration.Geometry.GeometryIdeal_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")

from Configuration.AlCa.autoCond import autoCond
process.GlobalTag.globaltag = autoCond['run2_mc']

#process.GlobalTag.globaltag = '74X_dataRun2_Prompt_v1'

process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 1

process.Out = cms.OutputModule("PoolOutputModule",
	SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring("p")),
	fileName = cms.untracked.string ("hcalDigis.root")
)

process.p = cms.Path(process.hcalDigis)
process.e = cms.EndPath(process.Out)


