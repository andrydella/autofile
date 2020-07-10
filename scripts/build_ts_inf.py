"""
  Generate 
"""

import automol
import autofile
from automol.zmatrix._unimol_ts import min_hyd_mig_dist
from automol.zmatrix._unimol_ts import hydrogen_migration
from automol.zmatrix._unimol_ts import min_unimolecular_elimination_dist
from automol.zmatrix._unimol_ts import concerted_unimolecular_elimination
from automol.zmatrix._unimol_ts import beta_scission
from automol.zmatrix._bimol_ts import insertion
from automol.zmatrix._bimol_ts import substitution
from automol.zmatrix._bimol_ts import addition
from automol.zmatrix._bimol_ts import hydrogen_abstraction

FAILS = [
[
     ['InChI=1S/C12H26/c1-3-5-7-9-11-12-10-8-6-4-2/h3-12H2,1-2H3', 'InChI=1S/H'],
     ['InChI=1S/C12H25/c1-3-5-7-9-11-12-10-8-6-4-2/h7H,3-6,8-12H2,1-2H3', 'InChI=1S/H2/h1H'],
     'abst',
     '/lcrc/project/PACC/AutoMech/data/save/RXN/C12H25.H2/DFAXIAFEKRBNIW/0_0/2_1/UHFFFAOYSA-N/C12H26.H/ZGAMHLWDMNACOE/0_0/1_2/UHFFFAOYSA-N/2/u-ulpJU/TS/CONFS/cbhxR_Bp4YbEY/'
],
[
     ['InChI=1S/C12H26/c1-3-5-7-9-11-12-10-8-6-4-2/h3-12H2,1-2H3', 'InChI=1S/H'],
     ['InChI=1S/C12H25/c1-3-5-7-9-11-12-10-8-6-4-2/h9H,3-8,10-12H2,1-2H3', 'InChI=1S/H2/h1H'],
     'abst',
     '/lcrc/project/PACC/AutoMech/data/save/RXN/C12H25.H2/FWGAWEOTTFYPIM/0_0/2_1/UHFFFAOYSA-N/C12H26.H/ZGAMHLWDMNACOE/0_0/1_2/UHFFFAOYSA-N/2/u-ulpJU/TS/CONFS/c7owVu4hCz_Ep/'
],
[
     ['InChI=1S/C12H25/c1-3-5-7-9-11-12-10-8-6-4-2/h11H,3-10,12H2,1-2H3', 'InChI=1S/H2/h1H'],
     ['InChI=1S/C12H26/c1-3-5-7-9-11-12-10-8-6-4-2/h3-12H2,1-2H3', 'InChI=1S/H'],
     'abst',
     '/lcrc/project/PACC/AutoMech/data/save/RXN/C12H25.H2/NEZIQCLFGSOSAH/0_0/2_1/UHFFFAOYSA-N/C12H26.H/ZGAMHLWDMNACOE/0_0/1_2/UHFFFAOYSA-N/2/u-ulpJU/TS/CONFS/cJBgSyjmU-40a/'
],
[
     ['InChI=1S/C12H26/c1-3-5-7-9-11-12-10-8-6-4-2/h3-12H2,1-2H3', 'InChI=1S/H'],
     ['InChI=1S/C12H25/c1-3-5-7-9-11-12-10-8-6-4-2/h5H,3-4,6-12H2,1-2H3', 'InChI=1S/H2/h1H'],
     'abst',
     '/lcrc/project/PACC/AutoMech/data/save/RXN/C12H25.H2/NSAMIFBPMFLPEM/0_0/2_1/UHFFFAOYSA-N/C12H26.H/ZGAMHLWDMNACOE/0_0/1_2/UHFFFAOYSA-N/2/u-ulpJU/TS/CONFS/cnQ2HALtswwC3/'
],
[
     ['InChI=1S/C12H26/c1-3-5-7-9-11-12-10-8-6-4-2/h3-12H2,1-2H3', 'InChI=1S/H'],
     ['InChI=1S/C12H25/c1-3-5-7-9-11-12-10-8-6-4-2/h1,3-12H2,2H3', 'InChI=1S/H2/h1H'],
     'abst',
     '/lcrc/project/PACC/AutoMech/data/save/RXN/C12H25.H2/TYZYUZRJZLYPEP/0_0/2_1/UHFFFAOYSA-N/C12H26.H/ZGAMHLWDMNACOE/0_0/1_2/UHFFFAOYSA-N/2/u-ulpJU/TS/CONFS/ccON58LktrVnR/'
],
[
     ['InChI=1S/C12H26/c1-3-5-7-9-11-12-10-8-6-4-2/h3-12H2,1-2H3', 'InChI=1S/HO/h1H'],
     ['InChI=1S/C12H25/c1-3-5-7-9-11-12-10-8-6-4-2/h9H,3-8,10-12H2,1-2H3', 'InChI=1S/H2O/h1H2'],
     'abst',
     '/lcrc/project/PACC/AutoMech/data/save/RXN/C12H25.H2O/JZABJFVQNVCYCP/0_0/2_1/UHFFFAOYSA-N/C12H26.HO/APYCEKLDDDRQRK/0_0/1_2/UHFFFAOYSA-N/2/u-ulpJU/TS/CONFS/cpsJxRvcMYbWx/'
],
[
     ['InChI=1S/C12H26/c1-3-5-7-9-11-12-10-8-6-4-2/h3-12H2,1-2H3', 'InChI=1S/HO/h1H'],
     ['InChI=1S/C12H25/c1-3-5-7-9-11-12-10-8-6-4-2/h3H,4-12H2,1-2H3', 'InChI=1S/H2O/h1H2'],
     'abst',
     '/lcrc/project/PACC/AutoMech/data/save/RXN/C12H25.H2O/KBMXFRTXJGGTRG/0_0/2_1/UHFFFAOYSA-N/C12H26.HO/APYCEKLDDDRQRK/0_0/1_2/UHFFFAOYSA-N/2/u-ulpJU/TS/CONFS/cyGqMyUukXJ6l/'
],
[
     ['InChI=1S/C12H26/c1-3-5-7-9-11-12-10-8-6-4-2/h3-12H2,1-2H3', 'InChI=1S/HO/h1H'],
     ['InChI=1S/C12H25/c1-3-5-7-9-11-12-10-8-6-4-2/h1,3-12H2,2H3', 'InChI=1S/H2O/h1H2'],
     'abst',
     '/lcrc/project/PACC/AutoMech/data/save/RXN/C12H25.H2O/NDSPOJVKMHAPTB/0_0/2_1/UHFFFAOYSA-N/C12H26.HO/APYCEKLDDDRQRK/0_0/1_2/UHFFFAOYSA-N/2/u-ulpJU/TS/CONFS/c8zSWDOCl0hm_/'
],
[
     ['InChI=1S/C12H26/c1-3-5-7-9-11-12-10-8-6-4-2/h3-12H2,1-2H3', 'InChI=1S/HO/h1H'],
     ['InChI=1S/C12H25/c1-3-5-7-9-11-12-10-8-6-4-2/h11H,3-10,12H2,1-2H3', 'InChI=1S/H2O/h1H2'],
     'abst',
     '/lcrc/project/PACC/AutoMech/data/save/RXN/C12H25.H2O/SFTZGZQDEREJJO/0_0/2_1/UHFFFAOYSA-N/C12H26.HO/APYCEKLDDDRQRK/0_0/1_2/UHFFFAOYSA-N/2/u-ulpJU/TS/CONFS/c9FBlL6kkqK3V/'
],
[
     ['InChI=1S/C12H26/c1-3-5-7-9-11-12-10-8-6-4-2/h3-12H2,1-2H3', 'InChI=1S/HO/h1H'],
     ['InChI=1S/C12H25/c1-3-5-7-9-11-12-10-8-6-4-2/h7H,3-6,8-12H2,1-2H3', 'InChI=1S/H2O/h1H2'],
     'abst',
     '/lcrc/project/PACC/AutoMech/data/save/RXN/C12H25.H2O/UORSQPCPDMZTCN/0_0/2_1/UHFFFAOYSA-N/C12H26.HO/APYCEKLDDDRQRK/0_0/1_2/UHFFFAOYSA-N/2/u-ulpJU/TS/CONFS/cGEXoZq29H0gB/'
],
[
     ['InChI=1S/C12H26/c1-3-5-7-9-11-12-10-8-6-4-2/h3-12H2,1-2H3', 'InChI=1S/HO/h1H'],
     ['InChI=1S/C12H25/c1-3-5-7-9-11-12-10-8-6-4-2/h5H,3-4,6-12H2,1-2H3', 'InChI=1S/H2O/h1H2'],
     'abst',
     '/lcrc/project/PACC/AutoMech/data/save/RXN/C12H25.H2O/VDSUOIBCWUGMNU/0_0/2_1/UHFFFAOYSA-N/C12H26.HO/APYCEKLDDDRQRK/0_0/1_2/UHFFFAOYSA-N/2/u-ulpJU/TS/CONFS/cy6vEe74Z9CBy/'
],
[
     ['InChI=1S/H2O2/c1-2/h1-2H', 'InChI=1S/C12H25/c1-3-5-7-9-11-12-10-8-6-4-2/h5H,3-4,6-12H2,1-2H3'],
     ['InChI=1S/C12H26/c1-3-5-7-9-11-12-10-8-6-4-2/h3-12H2,1-2H3', 'InChI=1S/HO2/c1-2/h1H'],
     'abst',
     '/lcrc/project/PACC/AutoMech/data/save/RXN/C12H25.H2O2/GWVXNSKTIQAPQO/0_0/2_1/UHFFFAOYSA-N/C12H26.HO2/QDJWAPYTOVEPPJ/0_0/1_2/UHFFFAOYSA-N/2/u-ulpJU/TS/CONFS/cneJ2NQ-cTnuE/'
],
[
     ['InChI=1S/H2O2/c1-2/h1-2H', 'InChI=1S/C12H25/c1-3-5-7-9-11-12-10-8-6-4-2/h11H,3-10,12H2,1-2H3'],
     ['InChI=1S/C12H26/c1-3-5-7-9-11-12-10-8-6-4-2/h3-12H2,1-2H3', 'InChI=1S/HO2/c1-2/h1H'],
     'abst',
     '/lcrc/project/PACC/AutoMech/data/save/RXN/C12H25.H2O2/JZBIBIGCWXLSQH/0_0/2_1/UHFFFAOYSA-N/C12H26.HO2/QDJWAPYTOVEPPJ/0_0/1_2/UHFFFAOYSA-N/2/u-ulpJU/TS/CONFS/cwb20yYV-Pp8-/'
],
[
     ['InChI=1S/H2O2/c1-2/h1-2H', 'InChI=1S/C12H25/c1-3-5-7-9-11-12-10-8-6-4-2/h9H,3-8,10-12H2,1-2H3'],
     ['InChI=1S/C12H26/c1-3-5-7-9-11-12-10-8-6-4-2/h3-12H2,1-2H3', 'InChI=1S/HO2/c1-2/h1H'],
     'abst',
     '/lcrc/project/PACC/AutoMech/data/save/RXN/C12H25.H2O2/ZHXAUVOLZVRYDK/0_0/2_1/UHFFFAOYSA-N/C12H26.HO2/QDJWAPYTOVEPPJ/0_0/1_2/UHFFFAOYSA-N/2/u-ulpJU/TS/CONFS/cykSF6U6KlJN-/'
],
[
     ['InChI=1S/C12H26/c1-3-5-7-9-11-12-10-8-6-4-2/h3-12H2,1-2H3', 'InChI=1S/O'],
     ['InChI=1S/C12H25/c1-3-5-7-9-11-12-10-8-6-4-2/h3H,4-12H2,1-2H3', 'InChI=1S/HO/h1H'],
     'abst',
     '/lcrc/project/PACC/AutoMech/data/save/RXN/C12H25.HO/HULDITQIPBSMHF/0_0/2_2/UHFFFAOYSA-N/C12H26.O/CVYNBVMJLPTTFD/0_0/1_3/UHFFFAOYSA-N/3/u-ulpJU/TS/CONFS/cWm9G87C98gsN/'
],
[
     ['InChI=1S/C12H26/c1-3-5-7-9-11-12-10-8-6-4-2/h3-12H2,1-2H3', 'InChI=1S/O'],
     ['InChI=1S/C12H25/c1-3-5-7-9-11-12-10-8-6-4-2/h11H,3-10,12H2,1-2H3', 'InChI=1S/HO/h1H'],
     'abst',
     '/lcrc/project/PACC/AutoMech/data/save/RXN/C12H25.HO/JTYKGCDIQGRUCU/0_0/2_2/UHFFFAOYSA-N/C12H26.O/CVYNBVMJLPTTFD/0_0/1_3/UHFFFAOYSA-N/3/u-ulpJU/TS/CONFS/c6lE4lmT4oVvd/'
],
[
     ['InChI=1S/HO/h1H', 'InChI=1S/C12H25/c1-3-5-7-9-11-12-10-8-6-4-2/h7H,3-6,8-12H2,1-2H3'],
     ['InChI=1S/C12H26/c1-3-5-7-9-11-12-10-8-6-4-2/h3-12H2,1-2H3', 'InChI=1S/O'],
     'abst',
     '/lcrc/project/PACC/AutoMech/data/save/RXN/C12H25.HO/LFDWMPGZVNMVJB/0_0/2_2/UHFFFAOYSA-N/C12H26.O/CVYNBVMJLPTTFD/0_0/1_3/UHFFFAOYSA-N/3/u-ulpJU/TS/CONFS/crPweX1kRPPpF/'
],
[
     ['InChI=1S/HO/h1H', 'InChI=1S/C12H25/c1-3-5-7-9-11-12-10-8-6-4-2/h5H,3-4,6-12H2,1-2H3'],
     ['InChI=1S/C12H26/c1-3-5-7-9-11-12-10-8-6-4-2/h3-12H2,1-2H3', 'InChI=1S/O'],
     'abst',
     '/lcrc/project/PACC/AutoMech/data/save/RXN/C12H25.HO/UXURQUKKAAERTP/0_0/2_2/UHFFFAOYSA-N/C12H26.O/CVYNBVMJLPTTFD/0_0/1_3/UHFFFAOYSA-N/3/u-ulpJU/TS/CONFS/cIXM5TpS_aua9/'
],
[
     ['InChI=1S/C2H4O/c1-2-3/h2H,1H3', 'InChI=1S/H'],
     ['InChI=1S/C2H3O/c1-2-3/h1H3', 'InChI=1S/H2/h1H'],
     'abst',
     '/lcrc/project/PACC/AutoMech/data/save/RXN/C2H3O.H2/OAUXQTHVBDKAQI/0_0/2_1/UHFFFAOYSA-N/C2H4O.H/ZYUQWGNPABHJHI/0_0/1_2/UHFFFAOYSA-N/2/hJUn9NU/TS/CONFS/cmloZpqMh-CAh/'
],
[
     ['InChI=1S/C2H4O/c1-2-3/h2H,1H3', 'InChI=1S/HO/h1H'],
     ['InChI=1S/C2H3O/c1-2-3/h1H3', 'InChI=1S/H2O/h1H2'],
     'abst',
     '/lcrc/project/PACC/AutoMech/data/save/RXN/C2H3O.H2O/WVZIMQZWEVDUHA/0_0/2_1/UHFFFAOYSA-N/C2H4O.HO/DQIRUQPUUCQTAO/0_0/1_2/UHFFFAOYSA-N/2/hJUn9NU/TS/CONFS/cts7hnn_qfrrx/'
],
[
     ['InChI=1S/H2/h1H', 'InChI=1S/C2H5/c1-2/h1H2,2H3'],
     ['InChI=1S/C2H6/c1-2/h1-2H3', 'InChI=1S/H'],
     'abst',
     '/lcrc/project/PACC/AutoMech/data/save/RXN/C2H5.H2/AZYGZKNHAUXYNZ/0_0/2_1/UHFFFAOYSA-N/C2H6.H/LTIIYKNOQWYAPP/0_0/1_2/UHFFFAOYSA-N/2/hJUn9NU/TS/CONFS/cxb3qn_HbKrg7/'
],
[
     ['InChI=1S/C2H6/c1-2/h1-2H3', 'InChI=1S/HO/h1H'],
     ['InChI=1S/C2H5/c1-2/h1H2,2H3', 'InChI=1S/H2O/h1H2'],
     'abst',
     '/lcrc/project/PACC/AutoMech/data/save/RXN/C2H5.H2O/KVAJJDGMKKGZOJ/0_0/2_1/UHFFFAOYSA-N/C2H6.HO/WSNWQMSECHDLSY/0_0/1_2/UHFFFAOYSA-N/2/hJUn9NU/TS/CONFS/czPhPUGF1MAsA/'
],
[
     ['InChI=1S/C2H6O/c1-2-3/h3H,2H2,1H3', 'InChI=1S/CH3/h1H3'],
     ['InChI=1S/C2H5O/c1-2-3/h2H2,1H3', 'InChI=1S/CH4/h1H4'],
     'abst',
     '/lcrc/project/PACC/AutoMech/data/save/RXN/C2H5O.CH4/ZHWZVQKUASXLCA/0_0/2_1/UHFFFAOYSA-N/C2H6O.CH3/GJNGZCTXZDYVIR/0_0/1_2/UHFFFAOYSA-N/2/hJUn9NU/TS/CONFS/csfsMfoBSe079/'
],
[
     ['InChI=1S/ClH/h1H', 'InChI=1S/C2H5O/c1-2-3/h2-3H,1H3'],
     ['InChI=1S/C2H6O/c1-2-3/h3H,2H2,1H3', 'InChI=1S/Cl'],
     'abst',
     '/lcrc/project/PACC/AutoMech/data/save/RXN/C2H5O.ClH/GKIQHUSCZUKWGC/0_0/2_1/UHFFFAOYSA-N/C2H6O.Cl/LUJULUIUNNBXKV/0_0/1_2/UHFFFAOYSA-N/2/u-ulpJU/TS/CONFS/cPGaDEERlSywG/'
],
[
     ['InChI=1S/ClH/h1H', 'InChI=1S/C2H5O/c1-2-3/h2H2,1H3'],
     ['InChI=1S/C2H6O/c1-2-3/h3H,2H2,1H3', 'InChI=1S/Cl'],
     'abst',
     '/lcrc/project/PACC/AutoMech/data/save/RXN/C2H5O.ClH/LPSMGZAWXHCPPZ/0_0/2_1/UHFFFAOYSA-N/C2H6O.Cl/LUJULUIUNNBXKV/0_0/1_2/UHFFFAOYSA-N/2/u-ulpJU/TS/CONFS/c1hzpvitTHlZv/'
],
[
     ['InChI=1S/C2H6O/c1-2-3/h3H,2H2,1H3', 'InChI=1S/H'],
     ['InChI=1S/C2H5O/c1-2-3/h2-3H,1H3', 'InChI=1S/H2/h1H'],
     'abst',
     '/lcrc/project/PACC/AutoMech/data/save/RXN/C2H5O.H2/JPJMOSAZPDYUIC/0_0/2_1/UHFFFAOYSA-N/C2H6O.H/JNCRXHBFBKUOMK/0_0/1_2/UHFFFAOYSA-N/2/hJUn9NU/TS/CONFS/cqEVQ1nDznuqy/'
],
[
     ['InChI=1S/C2H6O/c1-2-3/h3H,2H2,1H3', 'InChI=1S/H'],
     ['InChI=1S/C2H5O/c1-2-3/h2H2,1H3', 'InChI=1S/H2/h1H'],
     'abst',
     '/lcrc/project/PACC/AutoMech/data/save/RXN/C2H5O.H2/QWKTYMGWPVTQHK/0_0/2_1/UHFFFAOYSA-N/C2H6O.H/JNCRXHBFBKUOMK/0_0/1_2/UHFFFAOYSA-N/2/hJUn9NU/TS/CONFS/cva1KU2rfRb3s/'
],
[
     ['InChI=1S/C3H6O/c1-3(2)4/h4H,1H2,2H3', 'InChI=1S/CH3/h1H3'],
     ['InChI=1S/C3H5O/c1-3(2)4/h1H2,2H3', 'InChI=1S/CH4/h1H4'],
     'abst',
     '/lcrc/project/PACC/AutoMech/data/save/RXN/C3H5O.CH4/YHOMETWLUQHRHZ/0_0/2_1/UHFFFAOYSA-N/C3H6O.CH3/FXCFHNXVLLFOLK/0_0/1_2/UHFFFAOYSA-N/2/hJUn9NU/TS/CONFS/c2Z2z2hSKf8ci/'
],
[
     ['InChI=1S/C3H6O/c1-3(2)4/h4H,1H2,2H3', 'InChI=1S/H'],
     ['InChI=1S/C3H5O/c1-3(2)4/h1H2,2H3', 'InChI=1S/H2/h1H'],
     'abst',
     '/lcrc/project/PACC/AutoMech/data/save/RXN/C3H5O.H2/DWUGGFDVIAJDAM/0_0/2_1/UHFFFAOYSA-N/C3H6O.H/MFXDNUSUBSEYRB/0_0/1_2/UHFFFAOYSA-N/2/hJUn9NU/TS/CONFS/c-w1Ep8SRIR3M/'
],
[
     ['InChI=1S/C3H6O/c1-3(2)4/h4H,1H2,2H3', 'InChI=1S/H'],
     ['InChI=1S/C3H5O/c1-3(2)4/h4H,1-2H2', 'InChI=1S/H2/h1H'],
     'abst',
     '/lcrc/project/PACC/AutoMech/data/save/RXN/C3H5O.H2/MEWJMIMRRWYBPT/0_0/2_1/UHFFFAOYSA-N/C3H6O.H/MFXDNUSUBSEYRB/0_0/1_2/UHFFFAOYSA-N/2/hJUn9NU/TS/CONFS/cKNDlgEvd5TXK/'
],
[
     ['InChI=1S/H2O/h1H2', 'InChI=1S/C3H5O/c1-3(2)4/h1,4H,2H3'],
     ['InChI=1S/C3H6O/c1-3(2)4/h4H,1H2,2H3', 'InChI=1S/HO/h1H'],
     'abst',
     '/lcrc/project/PACC/AutoMech/data/save/RXN/C3H5O.H2O/NLJSTXRGTXQOFL/0_0/2_1/UHFFFAOYSA-N/C3H6O.HO/FMKOEFMNSGAVLA/0_0/1_2/UHFFFAOYSA-N/2/hJUn9NU/TS/CONFS/cV4QQZ8S9w_as/'
],
[
     ['InChI=1S/H2/h1H', 'InChI=1S/C3H7/c1-3-2/h1,3H2,2H3'],
     ['InChI=1S/C3H8/c1-3-2/h3H2,1-2H3', 'InChI=1S/H'],
     'abst',
     '/lcrc/project/PACC/AutoMech/data/save/RXN/C3H7.H2/OOFHSPZRBDWYTD/0_0/2_1/UHFFFAOYSA-N/C3H8.H/HUJGSBJJMJGGRX/0_0/1_2/UHFFFAOYSA-N/2/hJUn9NU/TS/CONFS/cSwlD_PjykSdc/'
],
[
     ['InChI=1S/C3H8/c1-3-2/h3H2,1-2H3', 'InChI=1S/H'],
     ['InChI=1S/C3H7/c1-3-2/h3H,1-2H3', 'InChI=1S/H2/h1H'],
     'abst',
     '/lcrc/project/PACC/AutoMech/data/save/RXN/C3H7.H2/XIAUYTNEJOZPQS/0_0/2_1/UHFFFAOYSA-N/C3H8.H/HUJGSBJJMJGGRX/0_0/1_2/UHFFFAOYSA-N/2/hJUn9NU/TS/CONFS/coC9G8PlRxW6J/'
],
[
     ['InChI=1S/C3H8/c1-3-2/h3H2,1-2H3', 'InChI=1S/HO/h1H'],
     ['InChI=1S/C3H7/c1-3-2/h1,3H2,2H3', 'InChI=1S/H2O/h1H2'],
     'abst',
     '/lcrc/project/PACC/AutoMech/data/save/RXN/C3H7.H2O/AUZBWHOFGLJBPE/0_0/2_1/UHFFFAOYSA-N/C3H8.HO/NZBFINHRVZBCME/0_0/1_2/UHFFFAOYSA-N/2/hJUn9NU/TS/CONFS/cpCnNQ1qASRsO/'
],
[
     ['InChI=1S/C3H8/c1-3-2/h3H2,1-2H3', 'InChI=1S/HO/h1H'],
     ['InChI=1S/C3H7/c1-3-2/h3H,1-2H3', 'InChI=1S/H2O/h1H2'],
     'abst',
     '/lcrc/project/PACC/AutoMech/data/save/RXN/C3H7.H2O/WKDCVMIBWBWKPP/0_0/2_1/UHFFFAOYSA-N/C3H8.HO/NZBFINHRVZBCME/0_0/1_2/UHFFFAOYSA-N/2/hJUn9NU/TS/CONFS/cYbttyXAnIOjA/'
],
[
     ['InChI=1S/C3H8O/c1-3(2)4/h3-4H,1-2H3', 'InChI=1S/CH3/h1H3'],
     ['InChI=1S/C3H7O/c1-3(2)4/h3H,1-2H3', 'InChI=1S/CH4/h1H4'],
     'abst',
     '/lcrc/project/PACC/AutoMech/data/save/RXN/C3H7O.CH4/MPBIXXTXMHXQEI/0_0/2_1/UHFFFAOYSA-N/C3H8O.CH3/RDNIFOJLXJXHEW/0_0/1_2/UHFFFAOYSA-N/2/hJUn9NU/TS/CONFS/cygmO_u4k15px/'
],
[
     ['InChI=1S/C3H8O/c1-2-3-4/h4H,2-3H2,1H3', 'InChI=1S/CH3/h1H3'],
     ['InChI=1S/C3H7O/c1-2-3-4/h2-3H2,1H3', 'InChI=1S/CH4/h1H4'],
     'abst',
     '/lcrc/project/PACC/AutoMech/data/save/RXN/C3H7O.CH4/XDRNMKKTXXIKEZ/0_0/2_1/UHFFFAOYSA-N/C3H8O.CH3/JIEVOEDQAJUVDK/0_0/1_2/UHFFFAOYSA-N/2/hJUn9NU/TS/CONFS/cfwFwF0nFD8bk/'
],
[
     ['InChI=1S/H2/h1H', 'InChI=1S/C3H7O/c1-2-3-4/h4H,1-3H2'],
     ['InChI=1S/C3H8O/c1-2-3-4/h4H,2-3H2,1H3', 'InChI=1S/H'],
     'abst',
     '/lcrc/project/PACC/AutoMech/data/save/RXN/C3H7O.H2/AOTCHQGQEPLISY/0_0/2_1/UHFFFAOYSA-N/C3H8O.H/HGCIFESEWSOQSD/0_0/1_2/UHFFFAOYSA-N/2/hJUn9NU/TS/CONFS/clQxaM3GCE0qV/'
],
[
     ['InChI=1S/C3H7O/c1-2-3-4/h2-3H2,1H3', 'InChI=1S/H2/h1H'],
     ['InChI=1S/C3H8O/c1-2-3-4/h4H,2-3H2,1H3', 'InChI=1S/H'],
     'abst',
     '/lcrc/project/PACC/AutoMech/data/save/RXN/C3H7O.H2/FTZHMWWNVCKRSY/0_0/2_1/UHFFFAOYSA-N/C3H8O.H/HGCIFESEWSOQSD/0_0/1_2/UHFFFAOYSA-N/2/hJUn9NU/TS/CONFS/cm4GpfSKXIwt4/'
],
[
     ['InChI=1S/C3H8O/c1-2-3-4/h4H,2-3H2,1H3', 'InChI=1S/H'],
     ['InChI=1S/C3H7O/c1-2-3-4/h2,4H,3H2,1H3', 'InChI=1S/H2/h1H'],
     'abst',
     '/lcrc/project/PACC/AutoMech/data/save/RXN/C3H7O.H2/ISSYEHFTGXCFCE/0_0/2_1/UHFFFAOYSA-N/C3H8O.H/HGCIFESEWSOQSD/0_0/1_2/UHFFFAOYSA-N/2/hJUn9NU/TS/CONFS/clXiGUr9YubXt/'
],
[
     ['InChI=1S/C3H8O/c1-3(2)4/h3-4H,1-2H3', 'InChI=1S/H'],
     ['InChI=1S/C3H7O/c1-3(2)4/h3H,1-2H3', 'InChI=1S/H2/h1H'],
     'abst',
     '/lcrc/project/PACC/AutoMech/data/save/RXN/C3H7O.H2/PDURACYGGQILOP/0_0/2_1/UHFFFAOYSA-N/C3H8O.H/YPBCKSJTCGVTKO/0_0/1_2/UHFFFAOYSA-N/2/hJUn9NU/TS/CONFS/czILzjQm6BVKr/'
],
[
     ['InChI=1S/C3H8O/c1-3(2)4/h3-4H,1-2H3', 'InChI=1S/H'],
     ['InChI=1S/C3H7O/c1-3(2)4/h4H,1-2H3', 'InChI=1S/H2/h1H'],
     'abst',
     '/lcrc/project/PACC/AutoMech/data/save/RXN/C3H7O.H2/QHPGDJDPGJJFLD/0_0/2_1/UHFFFAOYSA-N/C3H8O.H/YPBCKSJTCGVTKO/0_0/1_2/UHFFFAOYSA-N/2/hJUn9NU/TS/CONFS/cFEe52msKhYRV/'
],
[
     ['InChI=1S/C3H8O/c1-2-3-4/h4H,2-3H2,1H3', 'InChI=1S/H'],
     ['InChI=1S/C3H7O/c1-2-3-4/h3-4H,2H2,1H3', 'InChI=1S/H2/h1H'],
     'abst',
     '/lcrc/project/PACC/AutoMech/data/save/RXN/C3H7O.H2/VIGZAZGHTSFBDO/0_0/2_1/UHFFFAOYSA-N/C3H8O.H/HGCIFESEWSOQSD/0_0/1_2/UHFFFAOYSA-N/2/hJUn9NU/TS/CONFS/c7oK0-8BFps9o/'
],
[
     ['InChI=1S/H2/h1H', 'InChI=1S/C4H9/c1-3-4-2/h3H,4H2,1-2H3'],
     ['InChI=1S/C4H10/c1-3-4-2/h3-4H2,1-2H3', 'InChI=1S/H'],
     'abst',
     '/lcrc/project/PACC/AutoMech/data/save/RXN/C4H10.H/GPBIFMRNVFKQEQ/0_0/1_2/UHFFFAOYSA-N/C4H9.H2/BTUUFTYPQGONPB/0_0/2_1/UHFFFAOYSA-N/2/hJUn9NU/TS/CONFS/cL-eaL3PRA8nY/'
],
[
     ['InChI=1S/H2/h1H', 'InChI=1S/C4H9/c1-3-4-2/h1,3-4H2,2H3'],
     ['InChI=1S/C4H10/c1-3-4-2/h3-4H2,1-2H3', 'InChI=1S/H'],
     'abst',
     '/lcrc/project/PACC/AutoMech/data/save/RXN/C4H10.H/GPBIFMRNVFKQEQ/0_0/1_2/UHFFFAOYSA-N/C4H9.H2/MHWVAZWXCGSNKB/0_0/2_1/UHFFFAOYSA-N/2/hJUn9NU/TS/CONFS/c1vLVNB8KJxvV/'
],
[
     ['InChI=1S/C4H10/c1-3-4-2/h3-4H2,1-2H3', 'InChI=1S/HO/h1H'],
     ['InChI=1S/C4H9/c1-3-4-2/h1,3-4H2,2H3', 'InChI=1S/H2O/h1H2'],
     'abst',
     '/lcrc/project/PACC/AutoMech/data/save/RXN/C4H10.HO/JVTQLSMLVOIGCX/0_0/1_2/UHFFFAOYSA-N/C4H9.H2O/CGNQFKWPCPYLTK/0_0/2_1/UHFFFAOYSA-N/2/hJUn9NU/TS/CONFS/cnQX-9THIaKfo/'
],
[
     ['InChI=1S/C4H10/c1-3-4-2/h3-4H2,1-2H3', 'InChI=1S/HO/h1H'],
     ['InChI=1S/C4H9/c1-3-4-2/h3H,4H2,1-2H3', 'InChI=1S/H2O/h1H2'],
     'abst',
     '/lcrc/project/PACC/AutoMech/data/save/RXN/C4H10.HO/JVTQLSMLVOIGCX/0_0/1_2/UHFFFAOYSA-N/C4H9.H2O/JIGBWOWHVUCPHB/0_0/2_1/UHFFFAOYSA-N/2/hJUn9NU/TS/CONFS/cVd0-JnBxip22/'
],
[
     ['InChI=1S/C4H10O/c1-2-3-4-5/h5H,2-4H2,1H3', 'InChI=1S/CH3/h1H3'],
     ['InChI=1S/C4H9O/c1-2-3-4-5/h2-4H2,1H3', 'InChI=1S/CH4/h1H4'],
     'abst',
     '/lcrc/project/PACC/AutoMech/data/save/RXN/C4H10O.CH3/NWAKIYMIQQTZBJ/0_0/1_2/UHFFFAOYSA-N/C4H9O.CH4/LZIYBMKHHCBNPK/0_0/2_1/UHFFFAOYSA-N/2/hJUn9NU/TS/CONFS/cd--n3mbure_o/'
],
[
     ['InChI=1S/C4H10O/c1-2-3-4-5/h5H,2-4H2,1H3', 'InChI=1S/H'],
     ['InChI=1S/C4H9O/c1-2-3-4-5/h3,5H,2,4H2,1H3', 'InChI=1S/H2/h1H'],
     'abst',
     '/lcrc/project/PACC/AutoMech/data/save/RXN/C4H10O.H/YOJUBXONRQCQSO/0_0/1_2/UHFFFAOYSA-N/C4H9O.H2/GQUXBLTUZYTZNL/0_0/2_1/UHFFFAOYSA-N/2/hJUn9NU/TS/CONFS/cHd6ESv5hmL5V/'
],
[
     ['InChI=1S/C4H10O/c1-2-3-4-5/h5H,2-4H2,1H3', 'InChI=1S/H'],
     ['InChI=1S/C4H9O/c1-2-3-4-5/h2,5H,3-4H2,1H3', 'InChI=1S/H2/h1H'],
     'abst',
     '/lcrc/project/PACC/AutoMech/data/save/RXN/C4H10O.H/YOJUBXONRQCQSO/0_0/1_2/UHFFFAOYSA-N/C4H9O.H2/IJQRKXOLRRVINO/0_0/2_1/UHFFFAOYSA-N/2/hJUn9NU/TS/CONFS/cXYySyl4TAjgy/'
],
[
     ['InChI=1S/C4H10O/c1-2-3-4-5/h5H,2-4H2,1H3', 'InChI=1S/H'],
     ['InChI=1S/C4H9O/c1-2-3-4-5/h4-5H,2-3H2,1H3', 'InChI=1S/H2/h1H'],
     'abst',
     '/lcrc/project/PACC/AutoMech/data/save/RXN/C4H10O.H/YOJUBXONRQCQSO/0_0/1_2/UHFFFAOYSA-N/C4H9O.H2/JJZPYWOVKBCCAL/0_0/2_1/UHFFFAOYSA-N/2/hJUn9NU/TS/CONFS/cnOhJeVNipp4e/'
],
[
     ['InChI=1S/C4H10O/c1-2-3-4-5/h5H,2-4H2,1H3', 'InChI=1S/H'],
     ['InChI=1S/C4H9O/c1-2-3-4-5/h2-4H2,1H3', 'InChI=1S/H2/h1H'],
     'abst',
     '/lcrc/project/PACC/AutoMech/data/save/RXN/C4H10O.H/YOJUBXONRQCQSO/0_0/1_2/UHFFFAOYSA-N/C4H9O.H2/TWXROUUJEKHJKJ/0_0/2_1/UHFFFAOYSA-N/2/hJUn9NU/TS/CONFS/c6pVw2tpjsLtx/'
],
[
     ['InChI=1S/C4H10O/c1-3-5-4-2/h3-4H2,1-2H3', 'InChI=1S/HO/h1H'],
     ['InChI=1S/C4H9O/c1-3-5-4-2/h3H,4H2,1-2H3', 'InChI=1S/H2O/h1H2'],
     'abst',
     '/lcrc/project/PACC/AutoMech/data/save/RXN/C4H10O.HO/YOJMYECXEAPARS/0_0/1_2/UHFFFAOYSA-N/C4H9O.H2O/FSPXZUPNMRUSEL/0_0/2_1/UHFFFAOYSA-N/2/u-ulpJU/TS/CONFS/c0OG2JIZJNA2n/'
],
[
     ['InChI=1S/CH4/h1H4', 'InChI=1S/C7H15/c1-3-5-7-6-4-2/h3H,4-7H2,1-2H3'],
     ['InChI=1S/C7H16/c1-3-5-7-6-4-2/h3-7H2,1-2H3', 'InChI=1S/CH3/h1H3'],
     'abst',
     '/lcrc/project/PACC/AutoMech/data/save/RXN/C7H15.CH4/HIAVESNTBNVRCC/0_0/2_1/UHFFFAOYSA-N/C7H16.CH3/HKWOHCPNSOEAQR/0_0/1_2/UHFFFAOYSA-N/2/u-ulpJU/TS/CONFS/c-3Rx6aX87hDu/'
],
[
     ['InChI=1S/CH4/h1H4', 'InChI=1S/C7H15/c1-3-5-7-6-4-2/h1,3-7H2,2H3'],
     ['InChI=1S/C7H16/c1-3-5-7-6-4-2/h3-7H2,1-2H3', 'InChI=1S/CH3/h1H3'],
     'abst',
     '/lcrc/project/PACC/AutoMech/data/save/RXN/C7H15.CH4/JQUOPRYSDBKOOQ/0_0/2_1/UHFFFAOYSA-N/C7H16.CH3/HKWOHCPNSOEAQR/0_0/1_2/UHFFFAOYSA-N/2/u-ulpJU/TS/CONFS/c-KY1lVpp14Oi/'
],
[
     ['InChI=1S/CH4/h1H4', 'InChI=1S/C7H15/c1-3-5-7-6-4-2/h5H,3-4,6-7H2,1-2H3'],
     ['InChI=1S/C7H16/c1-3-5-7-6-4-2/h3-7H2,1-2H3', 'InChI=1S/CH3/h1H3'],
     'abst',
     '/lcrc/project/PACC/AutoMech/data/save/RXN/C7H15.CH4/OZUKSPKIIIQOGM/0_0/2_1/UHFFFAOYSA-N/C7H16.CH3/HKWOHCPNSOEAQR/0_0/1_2/UHFFFAOYSA-N/2/u-ulpJU/TS/CONFS/c-UOlodHfXv_Z/'
],
[
     ['InChI=1S/CH4/h1H4', 'InChI=1S/C7H15/c1-3-5-7-6-4-2/h7H,3-6H2,1-2H3'],
     ['InChI=1S/C7H16/c1-3-5-7-6-4-2/h3-7H2,1-2H3', 'InChI=1S/CH3/h1H3'],
     'abst',
     '/lcrc/project/PACC/AutoMech/data/save/RXN/C7H15.CH4/UNJHACNIEKUYAH/0_0/2_1/UHFFFAOYSA-N/C7H16.CH3/HKWOHCPNSOEAQR/0_0/1_2/UHFFFAOYSA-N/2/u-ulpJU/TS/CONFS/c-6gxJUpwMqUh/'
],
[
     ['InChI=1S/H2/h1H', 'InChI=1S/C7H15/c1-3-5-7-6-4-2/h7H,3-6H2,1-2H3'],
     ['InChI=1S/C7H16/c1-3-5-7-6-4-2/h3-7H2,1-2H3', 'InChI=1S/H'],
     'abst',
     '/lcrc/project/PACC/AutoMech/data/save/RXN/C7H15.H2/LPMBZDXHEUCLRL/0_0/2_1/UHFFFAOYSA-N/C7H16.H/HHTKZUGPCYVNGX/0_0/1_2/UHFFFAOYSA-N/2/u-ulpJU/TS/CONFS/c-wNkEeAn-6zn/'
],
[
     ['InChI=1S/H2/h1H', 'IChI=1S/C7H15/c1-3-5-7-6-4-2/h3H,4-7H2,1-2H3'],
     ['InChI=1S/C7H16/c1-3-5-7-6-4-2/h3-7H2,1-2H3', 'InChI=1S/H'],
     'abst',
     '/lcrc/project/PACC/AutoMech/data/save/RXN/C7H15.H2/UHHWOZZUBZWGJL/0_0/2_1/UHFFFAOYSA-N/C7H16.H/HHTKZUGPCYVNGX/0_0/1_2/UHFFFAOYSA-N/2/u-ulpJU/TS/CONFS/c1o90Gxvk-YCc/'
],
[
     ['InChI=1S/H2/h1H', 'InChI=1S/C7H15/c1-3-5-7-6-4-2/h5H,3-4,6-7H2,1-2H3'],
     ['InChI=1S/C7H16/c1-3-5-7-6-4-2/h3-7H2,1-2H3', 'InChI=1S/H'],
     'abst',
     '/lcrc/project/PACC/AutoMech/data/save/RXN/C7H15.H2/XOJKZJHASNBVHY/0_0/2_1/UHFFFAOYSA-N/C7H16.H/HHTKZUGPCYVNGX/0_0/1_2/UHFFFAOYSA-N/2/u-ulpJU/TS/CONFS/c1iKly_t6kZtD/'
],
[
     ['InChI=1S/CH4/h1H4', 'InChI=1S/C8H17/c1-7(2)6-8(3,4)5/h7H,3,6H2,1-2,4-5H3'],
     ['InChI=1S/C8H18/c1-7(2)6-8(3,4)5/h7H,6H2,1-5H3', 'InChI=1S/CH3/h1H3'],
     'abst',
     '/lcrc/project/PACC/AutoMech/data/save/RXN/C8H17.CH4/QZNQQBUNQORGJN/0_0/2_1/UHFFFAOYSA-N/C8H18.CH3/TWXYLPVWIPREIC/0_0/1_2/UHFFFAOYSA-N/2/u-ulpJU/TS/CONFS/c29G4dnyVT9wL/'
],
[
     ['InChI=1S/CH4/h1H4', 'InChI=1S/C8H17/c1-7(2)6-8(3,4)5/h6H2,1-5H3'],
     ['InChI=1S/C8H18/c1-7(2)6-8(3,4)5/h7H,6H2,1-5H3', 'InChI=1S/CH3/h1H3'],
     'abst',
     '/lcrc/project/PACC/AutoMech/data/save/RXN/C8H17.CH4/SIFZOXQDAUPVHG/0_0/2_1/UHFFFAOYSA-N/C8H18.CH3/TWXYLPVWIPREIC/0_0/1_2/UHFFFAOYSA-N/2/u-ulpJU/TS/CONFS/c1JWr_mEzEFs_/'
],
[
     ['InChI=1S/CH4/h1H4', 'InChI=1S/C8H17/c1-7(2)6-8(3,4)5/h6-7H,1-5H3'],
     ['InChI=1S/C8H18/c1-7(2)6-8(3,4)5/h7H,6H2,1-5H3', 'InChI=1S/CH3/h1H3'],
     'abst',
     '/lcrc/project/PACC/AutoMech/data/save/RXN/C8H17.CH4/WNNYRAVZHXWDSS/0_0/2_1/UHFFFAOYSA-N/C8H18.CH3/TWXYLPVWIPREIC/0_0/1_2/UHFFFAOYSA-N/2/u-ulpJU/TS/CONFS/c6HuWmaHoMGu4/'
],
[
     ['InChI=1S/CH4/h1H4', 'InChI=1S/C8H17/c1-7(2)6-8(3,4)5/h7H,1,6H2,2-5H3/t7-/m1/s1'],
     ['InChI=1S/C8H18/c1-7(2)6-8(3,4)5/h7H,6H2,1-5H3', 'InChI=1S/CH3/h1H3'],
     'abst',
     '/lcrc/project/PACC/AutoMech/data/save/RXN/C8H17.CH4/YAAYQXRHULWITN/0_0/2_1/OGFXRTJISA-N/C8H18.CH3/TWXYLPVWIPREIC/0_0/1_2/UHFFFAOYSA-N/2/u-ulpJU/TS/CONFS/c4d9gE_xNpeGN/'
],
[
     ['InChI=1S/C8H18/c1-7(2)6-8(3,4)5/h7H,6H2,1-5H3', 'InChI=1S/H'],
     ['InChI=1S/C8H17/c1-7(2)6-8(3,4)5/h7H,3,6H2,1-2,4-5H3', 'InChI=1S/H2/h1H'],
     'abst',
     '/lcrc/project/PACC/AutoMech/data/save/RXN/C8H17.H2/OMEXJWYBPCMNBQ/0_0/2_1/UHFFFAOYSA-N/C8H18.H/JYYNQQFSTLPVPP/0_0/1_2/UHFFFAOYSA-N/2/u-ulpJU/TS/CONFS/cpWgecBPv7CGN/'
],
[
     ['InChI=1S/C8H17/c1-7(2)6-8(3,4)5/h6H2,1-5H3', 'InChI=1S/H2/h1H'],
     ['InChI=1S/C8H18/c1-7(2)6-8(3,4)5/h7H,6H2,1-5H3', 'InChI=1S/H'],
     'abst',
     '/lcrc/project/PACC/AutoMech/data/save/RXN/C8H17.H2/PHNIFEFKGAYXQK/0_0/2_1/UHFFFAOYSA-N/C8H18.H/JYYNQQFSTLPVPP/0_0/1_2/UHFFFAOYSA-N/2/u-ulpJU/TS/CONFS/cjZNIX4YJxSby/'
],
[
     ['InChI=1S/H2/h1H', 'InChI=1S/C8H17/c1-7(2)6-8(3,4)5/h6-7H,1-5H3'],
     ['InChI=1S/C8H18/c1-7(2)6-8(3,4)5/h7H,6H2,1-5H3', 'InChI=1S/H'],
     'abst',
     '/lcrc/project/PACC/AutoMech/data/save/RXN/C8H17.H2/WIONASNPDYTHBI/0_0/2_1/UHFFFAOYSA-N/C8H18.H/JYYNQQFSTLPVPP/0_0/1_2/UHFFFAOYSA-N/2/u-ulpJU/TS/CONFS/c1KXGv1gwy6fJ/'
],
[
     ['InChI=1S/H2O/h1H2', 'InChI=1S/C8H17/c1-7(2)6-8(3,4)5/h7H,3,6H2,1-2,4-5H3'],
     ['InChI=1S/C8H18/c1-7(2)6-8(3,4)5/h7H,6H2,1-5H3', 'InChI=1S/HO/h1H'],
     'abst',
     '/lcrc/project/PACC/AutoMech/data/save/RXN/C8H17.H2O/DXIGUQDJRVJCKE/0_0/2_1/UHFFFAOYSA-N/C8H18.HO/QLQMBQYCQFOESO/0_0/1_2/UHFFFAOYSA-N/2/u-ulpJU/TS/CONFS/c0QWqh7cX9zWE/'
],
[
     ['InChI=1S/H2O2/c1-2/h1-2H', 'InChI=1S/C8H17/c1-7(2)6-8(3,4)5/h6-7H,1-5H3'],
     ['InChI=1S/C8H18/c1-7(2)6-8(3,4)5/h7H,6H2,1-5H3', 'InChI=1S/HO2/c1-2/h1H'],
     'abst',
     '/lcrc/project/PACC/AutoMech/data/save/RXN/C8H17.H2O2/KGXKACQVPLZYQZ/0_0/2_1/UHFFFAOYSA-N/C8H18.HO2/BIMUMYVQDGCPQF/0_0/1_2/UHFFFAOYSA-N/2/u-ulpJU/TS/CONFS/cfg0JNsd5KFIu/'
],
[
     ['InChI=1S/CH2O/c1-2/h1H2', 'InChI=1S/H'],
     ['InChI=1S/CHO/c1-2/h1H', 'InChI=1S/H2/h1H'],
     'abst',
     '/lcrc/project/PACC/AutoMech/data/save/RXN/CH2O.H/KXHBQQZVFZEZFF/0_0/1_2/UHFFFAOYSA-N/CHO.H2/LNJYZYRLCOOVAC/0_0/2_1/UHFFFAOYSA-N/2/hJUn9NU/TS/CONFS/cquzlzc6ftjYH/'
],
[
     ['InChI=1S/CH4O/c1-2/h2H,1H3', 'InChI=1S/CH3/h1H3'],
     ['InChI=1S/CH3O/c1-2/h1H3', 'InChI=1S/CH4/h1H4'],
     'abst',
     '/lcrc/project/PACC/AutoMech/data/save/RXN/CH3O.CH4/AGXRHOCDCQWMFD/0_0/2_1/UHFFFAOYSA-N/CH4O.CH3/ZCLSVULFHKBZIQ/0_0/1_2/UHFFFAOYSA-N/2/hJUn9NU/TS/CONFS/ckTygaI-yXF0P/'
],
[
     ['InChI=1S/ClH/h1H', 'InChI=1S/CH3O/c1-2/h1H3'],
     ['InChI=1S/CH4O/c1-2/h2H,1H3', 'InChI=1S/Cl'],
     'abst',
     '/lcrc/project/PACC/AutoMech/data/save/RXN/CH3O.ClH/NJRMHSANCWDHIH/0_0/2_1/UHFFFAOYSA-N/CH4O.Cl/GBZGZYCOLUISIG/0_0/1_2/UHFFFAOYSA-N/2/u-ulpJU/TS/CONFS/cCYJpq9v4DTIb/'
],
[
     ['InChI=1S/CH4O/c1-2/h2H,1H3', 'InChI=1S/H'],
     ['InChI=1S/CH3O/c1-2/h1H3', 'InChI=1S/H2/h1H'],
     'abst',
     '/lcrc/project/PACC/AutoMech/data/save/RXN/CH3O.H2/CLBSTEJXMSLHPG/0_0/2_1/UHFFFAOYSA-N/CH4O.H/OIDGHIWDBOZRPL/0_0/1_2/UHFFFAOYSA-N/2/hJUn9NU/TS/CONFS/cTg_L1WJRotmk/'
],
[
     ['InChI=1S/CH4O/c1-2/h2H,1H3', 'InChI=1S/H'],
     ['InChI=1S/CH3O/c1-2/h2H,1H2', 'InChI=1S/H2/h1H'],
     'abst',
     '/lcrc/project/PACC/AutoMech/data/save/RXN/CH3O.H2/LYMPBMURRRVRFL/0_0/2_1/UHFFFAOYSA-N/CH4O.H/OIDGHIWDBOZRPL/0_0/1_2/UHFFFAOYSA-N/2/hJUn9NU/TS/CONFS/cX4pwpm7QK09e/'
],
[
     ['InChI=1S/CHO/c1-2/h1H'],
     ['InChI=1S/CO/c1-2', 'InChI=1S/H'],
     'addn',
     '/lcrc/project/PACC/AutoMech/data/save/RXN/CHO/CFHIDWOYWUOIHU/0/2/UHFFFAOYSA-N/CO.H/VOKSOUSYRMTVCE/0_0/1_2/UHFFFAOYSA-N/2/hJUn9NU/TS/CONFS/cOi5ParvKFKTQ/'
]
]

CLA = {
    'mig': hydrogen_migration,
    'bsci': beta_scission,
    'ins': insertion,
    'sub': substitution,
    'add': addition,
    'abst': hydrogen_abstraction
}


fails = []
for i, fail in enumerate(FAILS):
    print(fail[0])
    print(fail[1])
    zma_fs = autofile.fs.manager(fail[3], 'ZMATRIX')
    rct_geos = list(map(automol.inchi.geometry, fail[0]))
    prd_geos = list(map(automol.inchi.geometry, fail[1]))
    rct_zmas = list(map(automol.geom.zmatrix, rct_geos))
    prd_zmas = list(map(automol.geom.zmatrix, prd_geos))
    ts_zma, dist_name, frm_key, brk_key, tors_names, rcts_gra = CLA[fail[2]](rct_zmas, prd_zmas)
    tra = (frozenset({frm_key}),
           frozenset({brk_key}))
    # zma_fs[-1].file.transformation.write(tra, [0])
    # zma_fs[-1].file.reactant_graph.write(rcts_gra, [0])
