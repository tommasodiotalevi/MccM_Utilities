## Fragments and girdpacks' collection for *Zphi/rho samples

### General fragments
pythia_fragment_run2_CUEP8M1 = """import FWCore.ParameterSet.Config as cms
from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.Pythia8CUEP8M1Settings_cfi import *
from Configuration.Generator.PSweightsPythia.PythiaPSweightsSettings_cfi import *
from Configuration.Generator.Pythia8PowhegEmissionVetoSettings_cfi import *

generator = cms.EDFilter("Pythia8HadronizerFilter",
                         maxEventsToPrint = cms.untracked.int32(1),
                         pythiaPylistVerbosity = cms.untracked.int32(1),
                         filterEfficiency = cms.untracked.double(1.0),
                         pythiaHepMCVerbosity = cms.untracked.bool(False),
                         comEnergy = cms.double(13000.),
                         PythiaParameters = cms.PSet(
        pythia8CommonSettingsBlock,
        pythia8CUEP8M1SettingsBlock,
        pythia8PSweightsSettingsBlock,
        pythia8PowhegEmissionVetoSettingsBlock,
        processParameters = cms.vstring(
             __CHANNEL_DECAY_FRAGMENT__
          ),
        parameterSets = cms.vstring('pythia8CommonSettings',
                                    'pythia8CUEP8M1Settings',
                                    'pythia8PSweightsSettings',
                                    'pythia8PowhegEmissionVetoSettings',
                                    'processParameters'
                                    )
        )
                         )


ProductionFilterSequence = cms.Sequence(generator)"""

pythia_fragment_run2_CP5 = """import FWCore.ParameterSet.Config as cms
from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.MCTunes2017.PythiaCP5Settings_cfi import *
from Configuration.Generator.PSweightsPythia.PythiaPSweightsSettings_cfi import *
from Configuration.Generator.Pythia8PowhegEmissionVetoSettings_cfi import *

generator = cms.EDFilter("Pythia8HadronizerFilter",
                         maxEventsToPrint = cms.untracked.int32(1),
                         pythiaPylistVerbosity = cms.untracked.int32(1),
                         filterEfficiency = cms.untracked.double(1.0),
                         pythiaHepMCVerbosity = cms.untracked.bool(False),
                         comEnergy = cms.double(13000.),
                         PythiaParameters = cms.PSet(
        pythia8CommonSettingsBlock,
        pythia8CP5SettingsBlock,
        pythia8PSweightsSettingsBlock,
        pythia8PowhegEmissionVetoSettingsBlock,
        processParameters = cms.vstring(
            __CHANNEL_DECAY_FRAGMENT__
          ),
        parameterSets = cms.vstring('pythia8CommonSettings',
                                    'pythia8CP5Settings',
                                    'pythia8PSweightsSettings',
                                    'pythia8PowhegEmissionVetoSettings',
                                    'processParameters'
                                    )
        )
                         )

ProductionFilterSequence = cms.Sequence(generator)
"""

def fragmentsDictCreator (decay_fr):
    dict = { '2016': pythia_fragment_run2_CUEP8M1.replace('__CHANNEL_DECAY_FRAGMENT__',decay_fr),
             '2017': pythia_fragment_run2_CP5.replace('__CHANNEL_DECAY_FRAGMENT__',decay_fr),
             '2018': pythia_fragment_run2_CP5.replace('__CHANNEL_DECAY_FRAGMENT__',decay_fr)
                    }
    return dict

lhe_fragmet = """import FWCore.ParameterSet.Config as cms

# link to card:
# __LINK__


externalLHEProducer = cms.EDProducer("ExternalLHEProducer",
    nEvents = cms.untracked.uint32(480),
    outputFile = cms.string('cmsgrid_final.lhe'),
    scriptName = cms.FileInPath('GeneratorInterface/LHEInterface/data/run_generic_tarball_cvmfs.sh'),
    numberOfParameters = cms.uint32(1),
    args = cms.vstring('__GRIDPACK__')
)

__PYTHIA_FRAGMENT__
"""

gp_vbf_2016 = ["/cvmfs/cms.cern.ch/phys_generator/gridpacks/slc6_amd64_gcc481/13TeV/powheg/V2/VBF_H_NNPDF30_13TeV_M125/v1/VBFH_NNPDF30_M-125_13TeV_tarball.tar.gz",
               "https://github.com/cms-sw/genproductions/blob/master/bin/Powheg/production/V2/13TeV/Higgs/VBF_H_NNPDF30_13TeV/VBF_H_NNPDF30_13TeV_M-125.input"]
gp_vbf_2017 = ["/cvmfs/cms.cern.ch/phys_generator/gridpacks/2017/13TeV/powheg/V2/VBF_H_NNPDF31_13TeV_M125/v1/VBF_H_NNPDF31_13TeV_M125_slc6_amd64_gcc630_CMSSW_9_3_0.tgz",
              "https://github.com/cms-sw/genproductions/blob/master/bin/Powheg/production/2017/13TeV/VBF_H_NNPDF31_13TeV/VBF_H_NNPDF31_13TeV_template.input"]
gp_WmH_2016 = ["/cvmfs/cms.cern.ch/phys_generator/gridpacks/slc6_amd64_gcc481/13TeV/powheg/V2/HWminusJ_HanythingJ_NNPDF30_13TeV_M125/v2_folding/HWminusJ_HanythingJ_NNPDF30_13TeV_M125_tarball.tar.gz",
              "https://github.com/cms-sw/genproductions/blob/329fda9f8d07c2d4d4e75c9a00279dcd6e78cda7/bin/Powheg/production/VH_from_Hbb/HWminusJ_HanythingJ_NNPDF30_13TeV_M125.input"]
gp_WmH_2017 = ["/cvmfs/cms.cern.ch/phys_generator/gridpacks/2017/13TeV/powheg/V2/HWminusJ_HanythingJ_NNPDF31_13TeV_M125/HWJ_slc6_amd64_gcc630_CMSSW_9_3_0_HWminusJ_HanythingJ_NNPDF31_13TeV_M125_Vinclusive.tgz",
              "https://github.com/cms-sw/genproductions/tree/ed4fe8f16facb54accec64bfc72246690a166ae3/bin/Powheg/production/2017/13TeV/Higgs/WminusHJ_HanythingJ_NNPDF31_13TeV/HWminusJ_HanythingJ_NNPDF31_13TeV_Vinclusive_template.input"]
gp_WpH_2016 = ["/cvmfs/cms.cern.ch/phys_generator/gridpacks/slc6_amd64_gcc481/13TeV/powheg/V2/HWplusJ_HanythingJ_NNPDF30_13TeV_M125/v2_folding/HWplusJ_HanythingJ_NNPDF30_13TeV_M125_tarball.tar.gz",
               "https://github.com/cms-sw/genproductions/blob/329fda9f8d07c2d4d4e75c9a00279dcd6e78cda7/bin/Powheg/production/VH_from_Hbb/HWplusJ_HanythingJ_NNPDF30_13TeV_M125.input"]
gp_WpH_2017 = ["/cvmfs/cms.cern.ch/phys_generator/gridpacks/2017/13TeV/powheg/V2/HWplusJ_HanythingJ_NNPDF31_13TeV_M125/HWJ_slc6_amd64_gcc630_CMSSW_9_3_0_HWplusJ_HanythingJ_NNPDF31_13TeV_M125_Vinclusive.tgz",
               "https://github.com/cms-sw/genproductions/blob/ed4fe8f16facb54accec64bfc72246690a166ae3/bin/Powheg/production/2017/13TeV/Higgs/WplusHJ_HanythingJ_NNPDF31_13TeV/HWplusJ_HanythingJ_NNPDF31_13TeV_Vinclusive_template.input"]
gp_ZH_2016 = ["/cvmfs/cms.cern.ch/phys_generator/gridpacks/slc6_amd64_gcc481/13TeV/powheg/V2/HZJ_HanythingJ_NNPDF30_13TeV_M125/v2_folding/HZJ_HanythingJ_NNPDF30_13TeV_M125_tarball.tar.gz",
              "https://github.com/cms-sw/genproductions/blob/329fda9f8d07c2d4d4e75c9a00279dcd6e78cda7/bin/Powheg/production/VH_from_Hbb/HZJ_HanythingJ_NNPDF30_13TeV_M125.input"]
gp_ZH_2017 = ["/cvmfs/cms.cern.ch/phys_generator/gridpacks/2017/13TeV/powheg/V2/HZJ_HanythingJ_NNPDF31_13TeV_M125/v1/HZJ_HanythingJ_NNPDF31_13TeV_M125.tgz",
              "https://github.com/cms-sw/genproductions/blob/ed4fe8f16facb54accec64bfc72246690a166ae3/bin/Powheg/production/2017/13TeV/Higgs/HZJ_HanythingJ_NNPDF31_13TeV/HZJ_HanythingJ_NNPDF31_13TeV_M125_Vinc.input"]

vbfh_zll_phi = '''
'POWHEG:nFinal = 3',
'25:onMode = off',
'25:addChannel = 1  1.00   103   23   333',
'25:m0 = 125.0',
'23:onMode = off',
'23:onIfMatch = 11 -11',
'23:onIfMatch = 13 -13',
'23:onIfMatch = 15 -15'
'''

vbfh_zll_rho = '''
'POWHEG:nFinal = 3',
'25:onMode = off',
'25:addChannel = 1  1.00   103   23   113',
'25:m0 = 125.0',
'23:onMode = off',
'23:onIfMatch = 11 -11',
'23:onIfMatch = 13 -13',
'23:onIfMatch = 15 -15'
'''

wh_zll_phi = '''
'POWHEG:nFinal = 3',
'25:onMode = off',
'25:addChannel = 1  1.00   103   23   333',
'25:m0 = 125.0',
'23:onMode = off',
'23:onIfMatch = 11 -11',
'23:onIfMatch = 13 -13',
'23:onIfMatch = 15 -15'
'''
wh_zll_rho = '''
'POWHEG:nFinal = 3',
'25:onMode = off',
'25:addChannel = 1  1.00   103   23   113',
'25:m0 = 125.0',
'23:onMode = off',
'23:onIfMatch = 11 -11',
'23:onIfMatch = 13 -13',
'23:onIfMatch = 15 -15'
'''

zh_zll_phi = '''
'POWHEG:nFinal = 3',
'25:onMode = off',
'25:addChannel = 1  1.00   103   23   333',
'25:m0 = 125.0'
'''

zh_zll_rho = '''
'POWHEG:nFinal = 3',
'25:onMode = off',
'25:addChannel = 1  1.00   103   23   113',
'25:m0 = 125.0'
'''

resonances = ['rho','phi']
production_modes_events = {'VBFH' : 250000, 'WmH': 100000, 'WpH': 100000, 'ZH': 300000}

dataset_names = {'2016' : '{}ToZ{}_TuneCUETP8M1_PSweights_13TeV-powheg_pythia8',
                 '2017' : '{}ToZ{}_TuneCP5_PSweights_13TeV-powheg_pythia8',
                 '2018' : '{}ToZ{}_TuneCP5_PSweights_13TeV-powheg_pythia8'}


pythia_fragmets_dict = {'VBFH_rho' : fragmentsDictCreator(vbfh_zll_rho),
                        'WmH_rho'  : fragmentsDictCreator(wh_zll_rho),
                        'WpH_rho'  : fragmentsDictCreator(wh_zll_rho),
                        'ZH_rho'   : fragmentsDictCreator(zh_zll_rho),
                        'VBFH_phi' : fragmentsDictCreator(vbfh_zll_phi),
                         'WmH_phi' : fragmentsDictCreator(wh_zll_phi),
                         'WpH_phi' : fragmentsDictCreator(wh_zll_phi),
                         'ZH_phi'  : fragmentsDictCreator(zh_zll_phi)
                        }

gridpacks_dict = {'VBFH' : {'2016': gp_vbf_2016, '2017': gp_vbf_2017, '2018': gp_vbf_2017},
                    'WmH' : {'2016': gp_WmH_2016, '2017': gp_WmH_2017, '2018': gp_WmH_2017},
                    'WpH' : {'2016': gp_WpH_2016, '2017': gp_WpH_2017, '2018': gp_WpH_2017},
                     'ZH' : {'2016': gp_ZH_2016,  '2017': gp_ZH_2017,  '2018': gp_ZH_2016}
                    }
