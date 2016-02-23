import FWCore.ParameterSet.Config as cms
process = cms.Process('TEST')

process.source = cms.Source(
    'PoolSource',
    fileNames = cms.untracked.vstring("file:hcalDigis_74X_dataRun2_Prompt_v1.root")
    )

process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(1))

process.load('Configuration.StandardSequences.Services_cff')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.StandardSequences.RawToDigi_Data_cff') 
process.load('Configuration.Geometry.GeometryExtended2015Reco_cff')
process.load('Configuration.Geometry.GeometryExtended2015_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_PostLS1_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
#process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')
process.load('SimCalorimetry.HcalTrigPrimProducers.hcaltpdigi_cff')

process.GlobalTag.globaltag = '74X_dataRun2_Prompt_v1'

process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 1

process.emulDigis = process.simHcalTriggerPrimitiveDigis.clone()
process.emulDigis.inputLabel =  cms.VInputTag('hcalDigis', 'hcalDigis')

process.Out = cms.OutputModule("PoolOutputModule",
        SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring("p")),
        fileName = cms.untracked.string ("HCAL.root")
)

process.seq = cms.Sequence( process.simHcalTriggerPrimitiveDigis)
process.p = cms.Path(process.seq)
process.e = cms.EndPath(process.Out)

