## Fragments and girdpacks' collection for H->aa->4gamma samples

### General fragments 
pythia_fragment_run2_CUEP8M1 = """import FWCore.ParameterSet.Config as cms
from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.Pythia8CUEP8M1Settings_cfi import *
from Configuration.Generator.PSweightsPythia.PythiaPSweightsSettings_cfi import *

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
        processParameters = cms.vstring(
             __CHANNEL_DECAY_FRAGMENT__
          ),
        parameterSets = cms.vstring('pythia8CommonSettings',
                                    'pythia8CUEP8M1Settings',
                                    'pythia8PSweightsSettings',
                                    'processParameters'
                                    )
        )
                         )


ProductionFilterSequence = cms.Sequence(generator)"""

pythia_fragment_run2_CP5 = """import FWCore.ParameterSet.Config as cms
from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.MCTunes2017.PythiaCP5Settings_cfi import *
from Configuration.Generator.PSweightsPythia.PythiaPSweightsSettings_cfi import *

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
        processParameters = cms.vstring(
            __CHANNEL_DECAY_FRAGMENT__
          ),
        parameterSets = cms.vstring('pythia8CommonSettings',
                                    'pythia8CP5Settings',
                                    'pythia8PSweightsSettings',
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

# Paths to proc cards on Github
proc_card_path = 'https://github.com/mbandrews/genproductions/blob/13ccb9321b7320770f5b8e7c211c93a2ebbd3591/bin/MadGraph5_aMCatNLO/cards/production/2017/13TeV/hToaaTo4gamma_ma_AMASS_GeV_MLM_4f_max1j/hToaaTo4gamma_ma_AMASS_GeV_MLM_4f_max1j_proc_card.dat'

# Add gridpack path once they are loaded on cvmfs

gp_haa_2016 = [] # gridpack path & proc_card_path for 2016
gp_haa_2017 = [] # gridpack path & proc_card_path for 2017
gp_haa_2018 = [] # gridpack path & proc_card_path for 2018

# Process parameters
h_aa = '''
'JetMatching:setMad = off',
'JetMatching:scheme = 1',
'JetMatching:merge = on',
'JetMatching:jetAlgorithm = 2',
'JetMatching:etaJetMax = 5.',
'JetMatching:coneRadius = 1.',
'JetMatching:slowJetPower = 1',
'JetMatching:qCut = 30.', 
'JetMatching:nQmatch = 4', 
'JetMatching:nJetMax = 1', 
'JetMatching:doShowerKt = off', 
'''

########################

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
