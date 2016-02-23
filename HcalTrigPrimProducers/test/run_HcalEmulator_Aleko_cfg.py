import FWCore.ParameterSet.Config as cms
process = cms.Process('ntuple')

process.source = cms.Source("PoolSource",
	fileNames = cms.untracked.vstring(
	    "file:hcalDigis_74X_dataRun2_Prompt_v1.root",
        ),
)

process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(1))

process.load('Configuration.StandardSequences.Services_cff')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.StandardSequences.RawToDigi_Data_cff')
process.load('SimCalorimetry.HcalTrigPrimProducers.hcaltpdigi_cff')
process.load("Configuration.Geometry.GeometryIdeal_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.GlobalTag.globaltag = '74X_dataRun2_Prompt_v1'

process.MessageLogger.cerr.FwkReport.reportEvery = 10

process.emulDigis = process.simHcalTriggerPrimitiveDigis.clone()
process.emulDigis.inputLabel = cms.VInputTag('hcalDigis', 'hcalDigis')

process.Out = cms.OutputModule("PoolOutputModule",
	SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring("p")),
	fileName = cms.untracked.string ("emulDigis.root")
)


process.p = cms.Path(process.emulDigis)
process.e = cms.EndPath(process.Out)
