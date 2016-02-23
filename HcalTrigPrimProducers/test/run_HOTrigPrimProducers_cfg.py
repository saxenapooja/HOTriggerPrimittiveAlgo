import FWCore.ParameterSet.Config as cms
process = cms.Process('test')

process.source = cms.Source(
    'PoolSource',
#   fileNames = cms.untracked.vstring("file:SingleMuPlus_Summer15_FlatPt-5to40_PRE_LS172_V15_inputToHOTriggerPrimittive.root")
#    fileNames = cms.untracked.vstring("file:hcalDigis_74X_dataRun2_Prompt_v1.root") # as this is not avaialble anymore, so switched to 2015D
#    fileNames = cms.untracked.vstring("file:hcalDigis_74X_2015D_1000Evnt.root")
    fileNames = cms.untracked.vstring("file:hcalDigis_74X_2015D.root")
    )


process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(6882))

process.load('Configuration.StandardSequences.Services_cff')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.Geometry.GeometryExtended2015Reco_cff')
process.load('Configuration.Geometry.GeometryExtended2015_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_PostLS1_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load('SimCalorimetry.HcalTrigPrimProducers.hotpdigi_cff')

process.GlobalTag.globaltag = '74X_dataRun2_Prompt_v1'


process.emulDigis = process.simHOTriggerPrimitiveDigis.clone()
process.emulDigis.inputLabel = cms.VInputTag('hcalDigis')

process.Out = cms.OutputModule("PoolOutputModule",
                               SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring("p")),
                               fileName = cms.untracked.string ("HO_EmulDigis_2015D_test.root")
)

process.p = cms.Path(process.emulDigis)
process.e = cms.EndPath(process.Out)

