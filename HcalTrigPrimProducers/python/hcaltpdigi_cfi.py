import FWCore.ParameterSet.Config as cms

simHcalTriggerPrimitiveDigis = cms.EDProducer("HcalTrigPrimDigiProducer",
    peakFilter = cms.bool(True),
    weights = cms.vdouble(1.0, 1.0), ##hardware algo        
    latency = cms.int32(1),
    FG_threshold = cms.uint32(12), ## threshold for setting fine grain bit
    ZS_threshold = cms.uint32(1),  ## threshold for setting fine grain bit
    numberOfSamples = cms.int32(4),
    numberOfPresamples = cms.int32(2),
    numberOfSamplesHF = cms.int32(4),
    numberOfPresamplesHF = cms.int32(2),
    muonBitThreshold_high = cms.uint32(1023), # For HO muon bit
    muonBitThreshold_low = cms.uint32(40),    # For HO muon bit
    firstSample         = cms.uint32(3),
    sampleToAdd         = cms.uint32(4),
    MinSignalThreshold = cms.uint32(0), # For HF PMT veto
    PMTNoiseThreshold = cms.uint32(0),  # For HF PMT veto
#
    #vdouble weights = { -1, -1, 1, 1} //low lumi algo
    # Input digi label (_must_ be without zero-suppression!)
    inputLabel = cms.VInputTag(cms.InputTag('simHcalUnsuppressedDigis'),
                               cms.InputTag('simHcalUnsuppressedDigis')),

    InputTagFEDRaw = cms.InputTag("rawDataCollector"),
    RunZS = cms.bool(False),
    FrontEndFormatError = cms.bool(False), # Front End Format Error, for real data only
    PeakFinderAlgorithm = cms.int32(2)

)
