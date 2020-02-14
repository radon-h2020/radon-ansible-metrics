# General metrics
from ansiblemetrics.general.loc   import LOC
from ansiblemetrics.general.bloc  import BLOC
from ansiblemetrics.general.cloc  import CLOC
from ansiblemetrics.general.dpt   import DPT
from ansiblemetrics.general.etp   import ETP 
from ansiblemetrics.general.ncd   import NCD
from ansiblemetrics.general.nco   import NCO
from ansiblemetrics.general.nfl   import NFL
from ansiblemetrics.general.ndk   import NDK
from ansiblemetrics.general.nicd  import NICD
from ansiblemetrics.general.nkeys import NKEYS
from ansiblemetrics.general.nlk   import NLK
from ansiblemetrics.general.nlo   import NLO
from ansiblemetrics.general.nmo   import NMO
from ansiblemetrics.general.nnnv  import NNNV
from ansiblemetrics.general.nnwv  import NNWV
from ansiblemetrics.general.nscm  import NSCM
from ansiblemetrics.general.ntkn  import NTKN
from ansiblemetrics.general.nun   import NUN

# Playbook scope
from ansiblemetrics.playbook.apls  import APLS
from ansiblemetrics.playbook.niu   import NIU
from ansiblemetrics.playbook.npl   import NPL
from ansiblemetrics.playbook.npnn  import NPNN
from ansiblemetrics.playbook.npun  import NPUN
from ansiblemetrics.playbook.npvr  import NPVR
from ansiblemetrics.playbook.nrgv  import NRGV
from ansiblemetrics.playbook.nrl   import NRL
from ansiblemetrics.playbook.nrvr  import NRVR
from ansiblemetrics.playbook.nvr   import NVR

# Tasks scope
from ansiblemetrics.tasks.atss  import ATSS
from ansiblemetrics.tasks.nbeh  import NBEH
from ansiblemetrics.tasks.nbl   import NBL
from ansiblemetrics.tasks.ncmd  import NCMD
from ansiblemetrics.tasks.ndm   import NDM
from ansiblemetrics.tasks.nemd  import NEMD
from ansiblemetrics.tasks.nfmd  import NFMD
from ansiblemetrics.tasks.nierr import NIERR
from ansiblemetrics.tasks.nimpp import NIMPP
from ansiblemetrics.tasks.nimpr import NIMPR
from ansiblemetrics.tasks.nimpt import NIMPT
from ansiblemetrics.tasks.ninc  import NINC
from ansiblemetrics.tasks.nincr import NINCR
from ansiblemetrics.tasks.ninct import NINCT
from ansiblemetrics.tasks.nincv import NINCV
from ansiblemetrics.tasks.nlp   import NLP
from ansiblemetrics.tasks.nmd   import NMD
from ansiblemetrics.tasks.nsh   import NSH
from ansiblemetrics.tasks.ntnn  import NTNN
from ansiblemetrics.tasks.nts   import NTS
from ansiblemetrics.tasks.ntun  import NTUN
from ansiblemetrics.tasks.ntvr  import NTVR

general_metrics ={
    'loc'   :   LOC, 
    'bloc'  :   BLOC, 
    'cloc'  :   CLOC,
    'dpt'   :   DPT, 
    'etp'   :   ETP, 
    'ncd'   :   NCD, 
    'nco'   :   NCO, 
    'ndk'   :   NDK, 
    'nfl'   :   NFL, 
    'nicd'  :   NICD, 
    'nkeys' :   NKEYS, 
    'nlk'   :   NLK, 
    'nlo'   :   NLO, 
    'nmo'   :   NMO, 
    'nnnv'  :   NNNV, 
    'nnwv'  :   NNWV,
    'nscm'  :   NSCM, 
    'ntkn'  :   NTKN, 
    'nun'   :   NUN
}

playbook_metrics = {
    'apls'  :   APLS, 
    'niu'   :   NIU, 
    'npl'   :   NPL, 
    'npnn'  :   NPNN, 
    'npun'  :   NPUN, 
    'npvr'  :   NPVR, 
    'nrgv'  :   NRGV, 
    'nrl'   :   NRL, 
    'nrvr'  :   NRVR,  
    'nvr'   :   NVR
}

tasks_metrics = {
    'atss'  :   ATSS, 
    'nbeh'  :   NBEH, 
    'nbl'   :   NBL, 
    'ncmd'  :   NCMD, 
    'ndm'   :   NDM, 
    'nemd'  :   NEMD, 
    'nfmd'  :   NFMD, 
    'nierr' :   NIERR,
    'nimpp' :   NIMPP, 
    'nimpr' :   NIMPR, 
    'nimpt' :   NIMPT, 
    'ninc'  :   NINC, 
    'nincr' :   NINCR, 
    'ninct' :   NINCT, 
    'nincv' :   NINCV,
    'nlp'   :   NLP, 
    'nmd'   :   NMD, 
    'nsh'   :   NSH, 
    'ntnn'  :   NTNN, 
    'nts'   :   NTS, 
    'ntun'  :   NTUN, 
    'ntvr'  :   NTVR
}