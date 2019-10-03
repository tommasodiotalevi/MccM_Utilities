### POWHEG fragment for HH
import string

class HHchannel:
    def __init__(self, name, generator):
        self.name = name
        self.generator = generator.upper()
        self.__fragment2016 = ''
        self.__fragment2017 = ''
        self.__fragment2018 = ''

    def setFragment(self, fragmentsDict):
        for key, item in fragmentsDict.items():
            if key == '2016':
                self.__fragment2016 = item
            if key == '2017':
                self.__fragment2017 = item
            if key == '2018':
                self.__fragment2018 = item

    def getFragment(self, year):
        try:
            if not self.__fragment2016 or not self.__fragment2017 or not self.__fragment2018:
                raise ValueError('Please initialize fragments')

            if year == '2016':
                self.__fragment2016 = item
            if year == '2017':
                self.__fragment2017 = item
            if year == '2018':
                self.__fragment2018 = item
        except ValueError as e:
            print(e)


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

## 4B

decay_HHTo4B = """'POWHEG:nFinal = 2',   ## Number of final state particles
                                   ## (BEFORE THE DECAYS) in the LHE
                                   ## other than emitted extra parton
             '25:onMode = off',
             '25:onIfMatch = 5 -5',
             'ResonanceDecayFilter:filter = on'"""

HHTo4B_dict = fragmentsDictCreator(decay_HHTo4B)

## 4T

decay_HHTo4T = """'POWHEG:nFinal = 2',   ## Number of final state particles
            '23:mMin = 0.05',
            '24:mMin = 0.05',
            '25:m0 = 125.0',
            '25:onMode = off',
            '25:onIfMatch = 15 -15',
            'ResonanceDecayFilter:filter = on',
            'ResonanceDecayFilter:exclusive = on', #off: require at least the specified number of daughters, on: require exactly the specified number of daughters
            'ResonanceDecayFilter:mothers = 25', #list of mothers not specified -> count all particles in hard process+resonance decays (better to avoid specifying mothers when including leptons from the lhe in counting, since intermediate resonances are not gauranteed to appear in general
            'ResonanceDecayFilter:daughters = 15,15,15,15',"""

HHTo4T_dict = fragmentsDictCreator(decay_HHTo4T)

## 4V

decay_HHTo4V = """'POWHEG:nFinal = 2',   ## Number of final state particles
            '23:mMin = 0.05',
            '24:mMin = 0.05',
            '25:m0 = 125.0',
            '25:onMode = off',
            '25:onIfMatch = 24 -24',
            '25:onIfMatch = 23 23',
            'ResonanceDecayFilter:filter = on',
            'ResonanceDecayFilter:exclusive = on', #off: require at least the specified number of daughters, on: require exactly the specified number of daughters
            'ResonanceDecayFilter:mothers = 25', #list of mothers not specified -> count all particles in hard process+resonance decays (better to avoid specifying mothers when including leptons from the lhe in counting, since intermediate resonances are not gauranteed to appear in general
            'ResonanceDecayFilter:wzAsEquivalent = on',
            'ResonanceDecayFilter:daughters = 23,23,23,23',"""

HHTo4V_dict = fragmentsDictCreator(decay_HHTo4V)

## 2B2G

decay_HHTo2B2G = """
                     'POWHEG:nFinal = 2',   ## Number of final state particles
                                            ## (BEFORE THE DECAYS) in the LHE
                                            ## other than emitted extra parton
                     '25:m0 = 125.0',
                     '25:onMode = off',
                     '25:onIfMatch = 5 -5',
                     '25:onIfMatch = 22 22',
                     'ResonanceDecayFilter:filter = on',
                     'ResonanceDecayFilter:exclusive = on', #off: require at least the specified number of daughters, on: require exactly the specified number of daughters
                     'ResonanceDecayFilter:mothers = 25', #list of mothers not specified -> count all particles in hard process+resonance decays (better to avoid specifying mothers when including leptons from the lhe in counting, since intermediate resonances are not gauranteed to appear in general
                     'ResonanceDecayFilter:daughters = 5,5,22,22'
                     """

HHTo2B2G_dict = fragmentsDictCreator(decay_HHTo2B2G)

# 2B2Tau
decay_HHTo2B2Tau = """'POWHEG:nFinal = 2',   ## Number of final state particles
                                   ## (BEFORE THE DECAYS) in the LHE
                                   ## other than emitted extra parton
                                 '25:m0 = 125.0',
                                 '25:onMode = off',
                                 '25:onIfMatch = 5 -5',
                                 '25:onIfMatch = 15 -15',
                                 'ResonanceDecayFilter:filter = on',
                                 'ResonanceDecayFilter:exclusive = on', #off: require at least the specified number of daughters, on: require exactly the specified number of daughters
                                 'ResonanceDecayFilter:mothers = 25', #list of mothers not specified -> count all particles in hard process+resonance decays (better to avoid specifying mothers when including leptons from the lhe in counting, since intermediate resonances are not gauranteed to appear in general
                                 'ResonanceDecayFilter:daughters = 5,5,15,15'"""

HHTo2B2Tau_dict = fragmentsDictCreator(decay_HHTo2B2Tau)

## 2B4L (ZZ)

decay_HHTo2B4L = """'POWHEG:nFinal = 2',   ## Number of final state particles
                                   ## (BEFORE THE DECAYS) in the LHE
                                   ## other than emitted extra parton
                        '23:mMin = 0.05',
                        '23:onMode = off',
                        '23:onIfAny = 11 13 15', # only leptonic Z decays
                        '25:m0 = 125.0',
                        '25:onMode = off',
                        '25:onIfMatch = 5 -5',
                        '25:onIfMatch = 23 23',
                        'ResonanceDecayFilter:filter = on',
                        'ResonanceDecayFilter:exclusive = on', #off: require at least the specified number of daughters, on: require exactly the specified number of daughters
                        'ResonanceDecayFilter:eMuAsEquivalent = off', #on: treat electrons and muons as equivalent
                        'ResonanceDecayFilter:eMuTauAsEquivalent = on', #on: treat electrons, muons , and taus as equivalent
                        'ResonanceDecayFilter:allNuAsEquivalent = off', #on: treat all three neutrino flavours as equivalent
                        'ResonanceDecayFilter:mothers = 25,23', #list of mothers not specified -> count all particles in hard process+resonance decays (better to avoid specifying mothers when including leptons from the lhe in counting, since intermediate resonances are not gauranteed to appear in general
                        'ResonanceDecayFilter:daughters = 5,5,11,11,11,11',
"""

HHTo2B4L_dict = fragmentsDictCreator(decay_HHTo2B4L)

## 2T2V

decay_HHTo2Tau2V = """'POWHEG:nFinal = 2',   ## Number of final state particles
            '23:mMin = 0.05',
            '24:mMin = 0.05',
            '25:m0 = 125.0',
            '25:onMode = off',
            '25:onIfMatch = 15 -15',
            '25:onIfMatch = 23 23',
            '25:onIfMatch = 24 -24',
            'ResonanceDecayFilter:filter = on',
            'ResonanceDecayFilter:exclusive = on', #off: require at least the specified number of daughters, on: require exactly the specified number of daughters
            'ResonanceDecayFilter:mothers = 25', #list of mothers not specified -> count all particles in hard process+resonance decays (better to avoid specifying mothers when including leptons from the lhe in counting, since intermediate resonances are not gauranteed to appear in general
            'ResonanceDecayFilter:wzAsEquivalent = on',
            'ResonanceDecayFilter:daughters = 15,15,23,23',"""

HHTo2Tau2V_dict = fragmentsDictCreator(decay_HHTo2Tau2V)

# ZZTo2L2J
decay_HHTo2B2L2J = """'POWHEG:nFinal = 2',   ## Number of final state particles
                                   ## (BEFORE THE DECAYS) in the LHE
                                   ## other than emitted extra parton
            '15:onMode = off',
            '15:onIfAny = 11 13', # only leptonic tau decays
            '23:mMin = 0.05',
            '23:onMode = off',
            '23:onIfAny = 1 2 3 4 5 11 13 15', # Z->jets decay and a leptonic charged Z decay, including taus
            '24:mMin = 0.05',
            '24:onMode = off',
            '25:m0 = 125.0',
            '25:onMode = off',
            '25:onIfMatch = 5 -5',
            '25:onIfMatch = 23 23',
            'ResonanceDecayFilter:filter = on',
            'ResonanceDecayFilter:exclusive = on', #off: require at least the specified number of daughters, on: require exactly the specified number of daughters
            'ResonanceDecayFilter:eMuAsEquivalent = off', #on: treat electrons and muons as equivalent
            'ResonanceDecayFilter:eMuTauAsEquivalent = on', #on: treat electrons, muons , and taus as equivalent
            'ResonanceDecayFilter:allNuAsEquivalent  = off', #on: treat all three neutrino flavours as equivalent
            'ResonanceDecayFilter:udscAsEquivalent   = off', #on: treat udsc quarks as equivalent
            'ResonanceDecayFilter:udscbAsEquivalent  = on',  #on: treat udscb quarks as equivalent
            'ResonanceDecayFilter:mothers = 25,23', #list of mothers not specified -> count all particles in hard process+resonance decays (better to avoid specifying mothers when including leptons from the lhe in counting, since intermediate resonances are not gauranteed to appear in general
            'ResonanceDecayFilter:daughters = 5,5,23,23,1,1,11,11',"""

HHTo2B2L2J_dict = fragmentsDictCreator(decay_HHTo2B2L2J)

# ZZ/WW To2L2Nu
decay_HHTo2B2L2Nu = """'POWHEG:nFinal = 2',   ## Number of final state particles
                                   ## (BEFORE THE DECAYS) in the LHE
                                   ## other than emitted extra parton
                        '23:mMin = 0.05',
                        '23:onMode = off',
                        '23:onIfAny = 11 12 13 14 15 16', # only leptonic Z decays
                        '24:mMin = 0.05',
                        '24:onMode = off',
                        '24:onIfAny = 11 13 15', # only leptonic W decays
                        '25:m0 = 125.0',
                        '25:onMode = off',
                        '25:onIfMatch = 5 -5',
                        '25:onIfMatch = 23 23',
                        '25:onIfMatch = 24 -24',
                        'ResonanceDecayFilter:filter = on',
                        'ResonanceDecayFilter:exclusive = on', #off: require at least the specified number of daughters, on: require exactly the specified number of daughters
                        'ResonanceDecayFilter:eMuAsEquivalent = off', #on: treat electrons and muons as equivalent
                        'ResonanceDecayFilter:eMuTauAsEquivalent = on', #on: treat electrons, muons , and taus as equivalent
                        'ResonanceDecayFilter:allNuAsEquivalent = on', #on: treat all three neutrino flavours as equivalent
                        'ResonanceDecayFilter:mothers = 25,23,24', #list of mothers not specified -> count all particles in hard process+resonance decays (better to avoid specifying mothers when including leptons from the lhe in counting, since intermediate resonances are not gauranteed to appear in general
                        'ResonanceDecayFilter:daughters = 5,5,11,11,12,12',"""

HHTo2B2L2Nu_dict = fragmentsDictCreator(decay_HHTo2B2L2Nu)

decay_HHTo2B2ZTo2B2L2Nu = """'POWHEG:nFinal = 2',   ## Number of final state particles
                                   ## (BEFORE THE DECAYS) in the LHE
                                   ## other than emitted extra parton
            '15:onMode = on',
            '23:mMin = 0.05',
            '23:onMode = off',
            '23:onIfAny = 11 12 13 14 15 16', # only leptonic Z decays
            '25:m0 = 125.0',
            '25:onMode = off',
            '25:onIfMatch = 5 -5',
            '25:onIfMatch = 23 23',
            'ResonanceDecayFilter:filter = on',
            'ResonanceDecayFilter:exclusive = on', #off: require at least the specified number of daughters, on: require exactly the specified number of daughters
            'ResonanceDecayFilter:eMuAsEquivalent = off', #on: treat electrons and muons as equivalent
            'ResonanceDecayFilter:eMuTauAsEquivalent = on', #on: treat electrons, muons , and taus as equivalent
            'ResonanceDecayFilter:allNuAsEquivalent = on', #on: treat all three neutrino flavours as equivalent
            'ResonanceDecayFilter:mothers = 25,23', #list of mothers not specified -> count all particles in hard process+resonance decays (better to avoid specifying mothers when including leptons from the lhe in counting, since intermediate resonances are not gauranteed to appear in general
            'ResonanceDecayFilter:daughters = 5,5,11,11,12,12',"""

HHTo2B2ZTo2B2L2Nu_dict = fragmentsDictCreator(decay_HHTo2B2ZTo2B2L2Nu)

decay_HHTo2BLNu2J = """'POWHEG:nFinal = 2',   # Number of final state particles (BEFORE THE DECAYS) in the LHE other than emitted extra parton
            '24:mMin = 0.05',
            '24:onMode = on',
            '25:m0 = 125.0',
            '25:onMode = off',
            '25:onIfMatch = 5 -5',
            '25:onIfMatch = 24 -24',
            'ResonanceDecayFilter:filter = on',
            'ResonanceDecayFilter:exclusive = on', #on: require exactly the specified number of daughters
            'ResonanceDecayFilter:eMuTauAsEquivalent = on', #on: treat electrons, muons , and taus as equivalent
            'ResonanceDecayFilter:allNuAsEquivalent = on', #on: treat all three neutrino flavours as equivalent
            'ResonanceDecayFilter:udscAsEquivalent = on', #on: treat udsc quarks as equivalent
            'ResonanceDecayFilter:mothers = 24,25',
            'ResonanceDecayFilter:daughters = 5,5,1,1,11,12',"""

HHTo2BLNu2J_dict = fragmentsDictCreator(decay_HHTo2BLNu2J)


HHTo2Tau2ZTo4L = """'POWHEG:nFinal = 2',
            '23:mMin = 0.05',
            '23:onMode = off',
            '23:onIfAny = 11 13 15', # only leptonic Z decays
            '25:m0 = 125.0',
            '25:onMode = off',
            '25:onIfMatch = 15 -15',
            '25:onIfMatch = 23 23',
            'ResonanceDecayFilter:filter = on',
            'ResonanceDecayFilter:exclusive = on', #off: require at least the specified number of daughters, on: require exactly the specified number of daughters
            'ResonanceDecayFilter:eMuAsEquivalent = off', #on: treat electrons and muons as equivalent
            'ResonanceDecayFilter:eMuTauAsEquivalent = on', #on: treat electrons, muons , and taus as equivalent
            'ResonanceDecayFilter:allNuAsEquivalent = off', #on: treat all three neutrino flavours as equivalent
            'ResonanceDecayFilter:mothers = 25,23', #list of mothers not specified -> count all particles in hard process+resonance decays (better to avoid specifying mothers when including leptons from the lhe in counting, since intermediate resonances are not gauranteed to appear in general
            'ResonanceDecayFilter:daughters = 15,15,11,11,11,11',"""

HHTo2Tau2ZTo4L_dict = fragmentsDictCreator(HHTo2Tau2ZTo4L)

HHTo2G2ZTo4L = """'POWHEG:nFinal = 2',
       '23:mMin = 0.05',
       '23:onMode = off',
       '23:onIfAny = 11 13 15', # only leptonic Z decays
       '25:m0 = 125.0',
       '25:onMode = off',
       '25:onIfMatch = 22 22',
       '25:onIfMatch = 23 23',
       'ResonanceDecayFilter:filter = on',
       'ResonanceDecayFilter:exclusive = on', #off: require at least the specified number of daughters, on: require exactly the specified number of daughters
       'ResonanceDecayFilter:eMuAsEquivalent = off', #on: treat electrons and muons as equivalent
       'ResonanceDecayFilter:eMuTauAsEquivalent = on', #on: treat electrons, muons , and taus as equivalent
       'ResonanceDecayFilter:allNuAsEquivalent = off', #on: treat all three neutrino flavours as equivalent
       'ResonanceDecayFilter:mothers = 25,23', #list of mothers not specified -> count all particles in hard process+resonance decays (better to avoid specifying mothers when including leptons from the lhe in counting, since intermediate resonances are not gauranteed to appear in general
       'ResonanceDecayFilter:daughters = 22,22,11,11,11,11',"""

HHTo2G2ZTo4L_dict = fragmentsDictCreator(HHTo2G2ZTo4L)

HHTo2W2ZTo4L = """'POWHEG:nFinal = 2',
            '23:mMin = 0.05',
            '23:onMode = off',
            '23:onIfAny = 11 13 15', # only leptonic Z decays
            '25:m0 = 125.0',
            '25:onMode = off',
            '25:onIfMatch = 24 24',
            '25:onIfMatch = 23 23',
            'ResonanceDecayFilter:filter = on',
            'ResonanceDecayFilter:exclusive = off', #off: require at least the specified number of daughters, on: require exactly the specified number of daughters
            'ResonanceDecayFilter:eMuAsEquivalent = off', #on: treat electrons and muons as equivalent
            'ResonanceDecayFilter:eMuTauAsEquivalent = on', #on: treat electrons, muons , and taus as equivalent
            'ResonanceDecayFilter:allNuAsEquivalent = off', #on: treat all three neutrino flavours as equivalent
            'ResonanceDecayFilter:mothers = 23,24', # list of mothers not specified -> count all particles in hard process+resonance decays (better to avoid specifying mothers when including leptons from the lhe in counting, since intermediate resonances are not gauranteed to appear in general
            'ResonanceDecayFilter:daughters = 11,11,11,11,11',"""

HHTo2W2ZTo4L_dict = fragmentsDictCreator(HHTo2W2ZTo4L)

HHchannel_dict = {
 '4B' : HHTo4B_dict,
 '4Tau' : HHTo4T_dict,
 '4V'   : HHTo4V_dict,
 '2B2G' : HHTo2B2G_dict,
 '2B2Tau' : HHTo2B2Tau_dict,
 '2B2ZTo4L' : HHTo2B4L_dict,
 '2V2Tau'  : HHTo2Tau2V_dict,
 '2B2ZTo2L2J' : HHTo2B2L2J_dict,
 '2B2VTo2L2Nu' : HHTo2B2L2Nu_dict,
 '2B2Z2L2Nu_ZZfilter' : HHTo2B2ZTo2B2L2Nu_dict,
 '2B2VLNu2J' : HHTo2BLNu2J_dict,
 '2Tau2ZTo4L' :  HHTo2Tau2ZTo4L_dict,
 '2G2ZTo4L'   :  HHTo2G2ZTo4L_dict,
 '2W2ZTo4L'   : HHTo2W2ZTo4L_dict
}
