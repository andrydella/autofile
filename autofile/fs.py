"""
autofile.fs
===========

Each function in this module returns a tuple of autofile.model.DataSeries
objects for interacting with successive layers in a file system.
"""
from autofile.schema import data_files
from autofile.schema import data_series
from autofile.schema import info_objects


class _FilePrefix():
    """ file prefixes """
    RUN = 'run'
    BUILD = 'build'
    CONF = 'conf'
    TAU = 'tau'
    SP = 'sp'
    HS = 'hs'
    SCAN = 'scan'
    GEOM = 'geom'
    GRAD = 'grad'
    HESS = 'hess'
    MIN = 'min'
    VPT2 = 'vpt2'
    LJ = 'lj'
    IRC = 'irc'


class _FileAttributeName():
    """ DataFile attribute names """
    INFO = 'info'
    INPUT = 'input'
    OUTPUT = 'output'
    VMATRIX = 'vmatrix'
    GEOM_INFO = 'geometry_info'
    GRAD_INFO = 'gradient_info'
    HESS_INFO = 'hessian_info'
    VPT2_INFO = 'vpt2_info'
    IRC_INFO = 'irc_info'
    GEOM_INPUT = 'geometry_input'
    GRAD_INPUT = 'gradient_input'
    HESS_INPUT = 'hessian_input'
    VPT2_INPUT = 'vpt2_input'
    IRC_INPUT = 'irc_input'
    ENERGY = 'energy'
    GEOM = 'geometry'
    ZMAT = 'zmatrix'
    GRAD = 'gradient'
    HESS = 'hessian'
    HFREQ = 'harmonic_frequencies'
    TRAJ = 'trajectory'
    ANHFREQ = 'anharmonic_frequencies'
    ANHZPVE = 'anharmonic_zpve'
    XMAT = 'anharmonicity_matrix'
    VIBROT_MAX = 'vibro_rot_alpha_matrix'
    CENTIF_DIST = 'quartic_centrifugal_dist_consts'
    LJ_EPS = 'lennard_jones_epsilon'
    LJ_SIG = 'lennard_jones_sigma'


def species(prefix):
    """ construct the species filesystem (2 layers)

    specifiers:
        0 - []
                (no files)
        1 - [ich, chg, mul]
                (no files)

    :param prefix: sets the path where this filesystem will sit
    :type prefix: str
    """
    trunk_ds = data_series.species_trunk(prefix)
    leaf_ds = data_series.species_leaf(prefix, root_ds=trunk_ds)
    return (trunk_ds, leaf_ds)


def theory(prefix):
    """ construct the theory filesystem (1 layer)

    specifiers:
        0 - [method, basis, orb_type]
                files:
                - energy
                - geometry
                - hessian
                - zmatrix

    :param prefix: sets the path where this filesystem will sit
    :type prefix: str
    """
    leaf_ds = data_series.theory_leaf(prefix)

    geom_dfile = data_files.geometry(_FilePrefix.GEOM)
    ene_dfile = data_files.energy(_FilePrefix.GEOM)
    zmat_dfile = data_files.zmatrix(_FilePrefix.GEOM)
    hess_dfile = data_files.hessian(_FilePrefix.HESS)
    leaf_ds.add_data_files({
        _FileAttributeName.ENERGY: ene_dfile,
        _FileAttributeName.GEOM: geom_dfile,
        _FileAttributeName.HESS: hess_dfile,
        _FileAttributeName.ZMAT: zmat_dfile})

    return (leaf_ds,)


def conformer(prefix):
    """ construct the conformer filesystem (2 layers)

    specifiers:
        0 - []
                files:
                - vmatrix
                - info
                - energy
                - trajectory
        1 - [cid]
                files:
                - geometry_info
                - gradient_info
                - hessian_info
                - geometry_input
                - gradient_input
                - hessian_input
                - energy
                - geometry
                - zmatrix
                - gradient
                - hessian
                - harmonic_frequencies
                - vpt2_info
                - vpt2_input
                - anharmonic_frequencies
                - anharmonic_zpve
                - anharmonicity_matrix
                - vibro_rot_alpha_matrix
                - quartic_centrifugal_dist_consts

    :param prefix: sets the path where this filesystem will sit
    :type prefix: str
    """
    trunk_ds = data_series.conformer_trunk(prefix)
    leaf_ds = data_series.conformer_leaf(prefix, root_ds=trunk_ds)

    min_ene_dfile = data_files.energy(_FilePrefix.MIN)
    vma_dfile = data_files.vmatrix(_FilePrefix.CONF)
    inf_dfile = data_files.information(_FilePrefix.CONF,
                                       function=info_objects.conformer_trunk)
    traj_dfile = data_files.trajectory(_FilePrefix.CONF)
    trunk_ds.add_data_files({
        _FileAttributeName.VMATRIX: vma_dfile,
        _FileAttributeName.INFO: inf_dfile,
        _FileAttributeName.ENERGY: min_ene_dfile,
        _FileAttributeName.TRAJ: traj_dfile})

    geom_inf_dfile = data_files.information(_FilePrefix.GEOM,
                                            function=info_objects.run)
    grad_inf_dfile = data_files.information(_FilePrefix.GRAD,
                                            function=info_objects.run)
    hess_inf_dfile = data_files.information(_FilePrefix.HESS,
                                            function=info_objects.run)
    # need addl vpt2 info file, one for job status and other for fermi
    vpt2_inf_dfile = data_files.information(_FilePrefix.VPT2,
                                            function=info_objects.vpt2)
    geom_inp_dfile = data_files.input_file(_FilePrefix.GEOM)
    grad_inp_dfile = data_files.input_file(_FilePrefix.GRAD)
    hess_inp_dfile = data_files.input_file(_FilePrefix.HESS)
    vpt2_inp_dfile = data_files.input_file(_FilePrefix.VPT2)
    ene_dfile = data_files.energy(_FilePrefix.GEOM)
    geom_dfile = data_files.geometry(_FilePrefix.GEOM)
    zmat_dfile = data_files.zmatrix(_FilePrefix.GEOM)
    grad_dfile = data_files.gradient(_FilePrefix.GRAD)
    hess_dfile = data_files.hessian(_FilePrefix.HESS)
    hfreq_dfile = data_files.harmonic_frequencies(_FilePrefix.HESS)
    anhfreq_dfile = data_files.anharmonic_frequencies(_FilePrefix.VPT2)
    anhzpve_dfile = data_files.anharmonic_zpve(_FilePrefix.VPT2)
    xmat_dfile = data_files.anharmonicity_matrix(_FilePrefix.VPT2)
    vibrot_mat_dfile = data_files.vibro_rot_alpha_matrix(_FilePrefix.VPT2)
    centrif_dist_dfile = data_files.quartic_centrifugal_dist_consts(
        _FilePrefix.VPT2)

    leaf_ds.add_data_files({
        _FileAttributeName.GEOM_INFO: geom_inf_dfile,
        _FileAttributeName.GRAD_INFO: grad_inf_dfile,
        _FileAttributeName.HESS_INFO: hess_inf_dfile,
        _FileAttributeName.GEOM_INPUT: geom_inp_dfile,
        _FileAttributeName.GRAD_INPUT: grad_inp_dfile,
        _FileAttributeName.HESS_INPUT: hess_inp_dfile,
        _FileAttributeName.ENERGY: ene_dfile,
        _FileAttributeName.GEOM: geom_dfile,
        _FileAttributeName.ZMAT: zmat_dfile,
        _FileAttributeName.GRAD: grad_dfile,
        _FileAttributeName.HESS: hess_dfile,
        _FileAttributeName.HFREQ: hfreq_dfile,
        _FileAttributeName.VPT2_INFO: vpt2_inf_dfile,
        _FileAttributeName.VPT2_INPUT: vpt2_inp_dfile,
        _FileAttributeName.ANHFREQ: anhfreq_dfile,
        _FileAttributeName.ANHZPVE: anhzpve_dfile,
        _FileAttributeName.XMAT: xmat_dfile,
        _FileAttributeName.VIBROT_MAX: vibrot_mat_dfile,
        _FileAttributeName.CENTIF_DIST: centrif_dist_dfile})

    return (trunk_ds, leaf_ds)


def single_point(prefix):
    """ construct the single-point filesystem (2 layers)

    specifiers:
        0 - []
                (no files)
        1 - [method, basis, orb_type]
                files:
                - info
                - input
                - energy

    :param prefix: sets the path where this filesystem will sit
    :type prefix: str
    """
    trunk_ds = data_series.single_point_trunk(prefix)
    leaf_ds = data_series.single_point_leaf(prefix, root_ds=trunk_ds)

    inp_dfile = data_files.input_file(_FilePrefix.SP)
    inf_dfile = data_files.information(_FilePrefix.SP,
                                       function=info_objects.run)
    ene_dfile = data_files.energy(_FilePrefix.SP)
    leaf_ds.add_data_files({
        _FileAttributeName.INFO: inf_dfile,
        _FileAttributeName.INPUT: inp_dfile,
        _FileAttributeName.ENERGY: ene_dfile})

    return (trunk_ds, leaf_ds)


def high_spin(prefix):
    """ construct the high-spin, single-point filesystem (2 layers)

    specifiers:
        0 - []
                (no files)
        1 - [method, basis, orb_type]
                files:
                - info
                - input
                - energy

    :param prefix: sets the path where this filesystem will sit
    :type prefix: str
    """
    trunk_ds = data_series.high_spin_trunk(prefix)
    leaf_ds = data_series.high_spin_leaf(prefix, root_ds=trunk_ds)

    inp_dfile = data_files.input_file(_FilePrefix.HS)
    inf_dfile = data_files.information(_FilePrefix.HS,
                                       function=info_objects.run)
    ene_dfile = data_files.energy(_FilePrefix.HS)
    leaf_ds.add_data_files({
        _FileAttributeName.INFO: inf_dfile,
        _FileAttributeName.INPUT: inp_dfile,
        _FileAttributeName.ENERGY: ene_dfile})

    return (trunk_ds, leaf_ds)


def scan(prefix):
    """ construct the scan filesystem (3 layers)

    three layers with the following specifiers:
        0 - []
                files:
                - vmatrix
        1 - [coo_names]
                files:
                - info
                - trajectory
        2 - [coo_names, coo_vals]
                files:
                - geometry_info
                - gradient_info
                - hessian_info
                - irc_info
                - geometry_input
                - gradient_input
                - hessian_input
                - irc_input
                - energy
                - geometry
                - zmatrix
                - gradient
                - hessian
                - harmonic_frequencies

    :param prefix: sets the path where this filesystem will sit
    :type prefix: str
    """
    trunk_ds = data_series.scan_trunk(prefix)
    branch_ds = data_series.scan_branch(prefix, root_ds=trunk_ds)
    leaf_ds = data_series.scan_leaf(prefix, root_ds=branch_ds)

    vma_dfile = data_files.vmatrix(_FilePrefix.SCAN)
    trunk_ds.add_data_files({
        _FileAttributeName.VMATRIX: vma_dfile})

    inf_dfile = data_files.information(_FilePrefix.SCAN,
                                       function=info_objects.scan_branch)
    traj_dfile = data_files.trajectory(_FilePrefix.SCAN)
    branch_ds.add_data_files({
        _FileAttributeName.INFO: inf_dfile,
        _FileAttributeName.TRAJ: traj_dfile})

    # Need an irc file in the branch!
    # Need an run irc file in the forward and backward direction

    geom_inf_dfile = data_files.information(_FilePrefix.GEOM,
                                            function=info_objects.run)
    grad_inf_dfile = data_files.information(_FilePrefix.GRAD,
                                            function=info_objects.run)
    hess_inf_dfile = data_files.information(_FilePrefix.HESS,
                                            function=info_objects.run)
    irc_inf_dfile = data_files.information(_FilePrefix.IRC,
                                           function=info_objects.run)
    geom_inp_dfile = data_files.input_file(_FilePrefix.GEOM)
    grad_inp_dfile = data_files.input_file(_FilePrefix.GRAD)
    hess_inp_dfile = data_files.input_file(_FilePrefix.HESS)
    irc_inp_dfile = data_files.input_file(_FilePrefix.IRC)
    ene_dfile = data_files.energy(_FilePrefix.GEOM)
    geom_dfile = data_files.geometry(_FilePrefix.GEOM)
    zmat_dfile = data_files.zmatrix(_FilePrefix.GEOM)
    grad_dfile = data_files.gradient(_FilePrefix.GRAD)
    hess_dfile = data_files.hessian(_FilePrefix.HESS)
    hfreq_dfile = data_files.harmonic_frequencies(_FilePrefix.HESS)
    leaf_ds.add_data_files({
        _FileAttributeName.GEOM_INFO: geom_inf_dfile,
        _FileAttributeName.GRAD_INFO: grad_inf_dfile,
        _FileAttributeName.HESS_INFO: hess_inf_dfile,
        _FileAttributeName.IRC_INFO: irc_inf_dfile,
        _FileAttributeName.GEOM_INPUT: geom_inp_dfile,
        _FileAttributeName.GRAD_INPUT: grad_inp_dfile,
        _FileAttributeName.HESS_INPUT: hess_inp_dfile,
        _FileAttributeName.IRC_INPUT: irc_inp_dfile,
        _FileAttributeName.ENERGY: ene_dfile,
        _FileAttributeName.GEOM: geom_dfile,
        _FileAttributeName.ZMAT: zmat_dfile,
        _FileAttributeName.GRAD: grad_dfile,
        _FileAttributeName.HESS: hess_dfile,
        _FileAttributeName.HFREQ: hfreq_dfile})

    return (trunk_ds, branch_ds, leaf_ds)


def cscan(prefix):
    """ construct the constrained scan filesystem (4 layers)

..    specifiers:
..        0 - []
..                files:
..                - vmatrix
..        1 - [coo_names]
..                files:
..                - info
..                - trajectory
..        2 - [coo_names, coo_vals]
..        3 - [coo_names, coo_vals, cons_coo_val_dct]
..                files:
..                - geometry_info
..                - gradient_info
..                - hessian_info
..                - geometry_input
..                - gradient_input
..                - hessian_input
..                - energy
..                - geometry
..                - zmatrix
..                - gradient
..                - hessian
..                - harmonic_frequencies

    :param prefix: sets the path where this filesystem will sit
    :type prefix: str
    """
    trunk_ds = data_series.cscan_trunk(prefix)
    branch1_ds = data_series.cscan_branch1(prefix, root_ds=trunk_ds)
    branch2_ds = data_series.cscan_branch2(prefix, root_ds=branch1_ds)
    leaf_ds = data_series.cscan_leaf(prefix, root_ds=branch2_ds)

    vma_dfile = data_files.vmatrix(_FilePrefix.SCAN)
    trunk_ds.add_data_files({
        _FileAttributeName.VMATRIX: vma_dfile})

    inf_dfile = data_files.information(_FilePrefix.SCAN,
                                       function=info_objects.scan_branch)
    traj_dfile = data_files.trajectory(_FilePrefix.SCAN)
    branch1_ds.add_data_files({
        _FileAttributeName.INFO: inf_dfile,
        _FileAttributeName.TRAJ: traj_dfile})

    geom_inf_dfile = data_files.information(_FilePrefix.GEOM,
                                            function=info_objects.run)
    grad_inf_dfile = data_files.information(_FilePrefix.GRAD,
                                            function=info_objects.run)
    hess_inf_dfile = data_files.information(_FilePrefix.HESS,
                                            function=info_objects.run)
    geom_inp_dfile = data_files.input_file(_FilePrefix.GEOM)
    grad_inp_dfile = data_files.input_file(_FilePrefix.GRAD)
    hess_inp_dfile = data_files.input_file(_FilePrefix.HESS)
    ene_dfile = data_files.energy(_FilePrefix.GEOM)
    geom_dfile = data_files.geometry(_FilePrefix.GEOM)
    zmat_dfile = data_files.zmatrix(_FilePrefix.GEOM)
    grad_dfile = data_files.gradient(_FilePrefix.GRAD)
    hess_dfile = data_files.hessian(_FilePrefix.HESS)
    hfreq_dfile = data_files.harmonic_frequencies(_FilePrefix.HESS)
    leaf_ds.add_data_files({
        _FileAttributeName.GEOM_INFO: geom_inf_dfile,
        _FileAttributeName.GRAD_INFO: grad_inf_dfile,
        _FileAttributeName.HESS_INFO: hess_inf_dfile,
        _FileAttributeName.GEOM_INPUT: geom_inp_dfile,
        _FileAttributeName.GRAD_INPUT: grad_inp_dfile,
        _FileAttributeName.HESS_INPUT: hess_inp_dfile,
        _FileAttributeName.ENERGY: ene_dfile,
        _FileAttributeName.GEOM: geom_dfile,
        _FileAttributeName.ZMAT: zmat_dfile,
        _FileAttributeName.GRAD: grad_dfile,
        _FileAttributeName.HESS: hess_dfile,
        _FileAttributeName.HFREQ: hfreq_dfile})

    return (trunk_ds, branch1_ds, branch2_ds, leaf_ds)


def tau(prefix):
    """ construct the tau filesystem (2 layers)

    specifiers:
        0 - []
                files:
                - vmatrix
                - info
                - trajectory
        0 - [tid]
                files:
                - geometry_info
                - gradient_info
                - hessian_info
                - geometry_input
                - gradient_input
                - hessian_input
                - energy
                - geometry
                - zmatrix
                - gradient
                - hessian
                - harmonic_frequencies

    :param prefix: sets the path where this filesystem will sit
    :type prefix: str
    """
    trunk_ds = data_series.tau_trunk(prefix)
    leaf_ds = data_series.tau_leaf(prefix, root_ds=trunk_ds)

    vma_dfile = data_files.vmatrix(_FilePrefix.TAU)
    inf_dfile = data_files.information(_FilePrefix.TAU,
                                       function=info_objects.tau_trunk)
    traj_dfile = data_files.trajectory(_FilePrefix.TAU)
    trunk_ds.add_data_files({
        _FileAttributeName.VMATRIX: vma_dfile,
        _FileAttributeName.INFO: inf_dfile,
        _FileAttributeName.TRAJ: traj_dfile})

    geom_inf_dfile = data_files.information(_FilePrefix.GEOM,
                                            function=info_objects.run)
    grad_inf_dfile = data_files.information(_FilePrefix.GRAD,
                                            function=info_objects.run)
    hess_inf_dfile = data_files.information(_FilePrefix.HESS,
                                            function=info_objects.run)
    geom_inp_dfile = data_files.input_file(_FilePrefix.GEOM)
    grad_inp_dfile = data_files.input_file(_FilePrefix.GRAD)
    hess_inp_dfile = data_files.input_file(_FilePrefix.HESS)
    ene_dfile = data_files.energy(_FilePrefix.GEOM)
    geom_dfile = data_files.geometry(_FilePrefix.GEOM)
    zmat_dfile = data_files.zmatrix(_FilePrefix.GEOM)
    grad_dfile = data_files.gradient(_FilePrefix.GRAD)
    hess_dfile = data_files.hessian(_FilePrefix.HESS)
    hfreq_dfile = data_files.harmonic_frequencies(_FilePrefix.HESS)
    leaf_ds.add_data_files({
        _FileAttributeName.GEOM_INFO: geom_inf_dfile,
        _FileAttributeName.GRAD_INFO: grad_inf_dfile,
        _FileAttributeName.HESS_INFO: hess_inf_dfile,
        _FileAttributeName.GEOM_INPUT: geom_inp_dfile,
        _FileAttributeName.GRAD_INPUT: grad_inp_dfile,
        _FileAttributeName.HESS_INPUT: hess_inp_dfile,
        _FileAttributeName.ENERGY: ene_dfile,
        _FileAttributeName.GEOM: geom_dfile,
        _FileAttributeName.ZMAT: zmat_dfile,
        _FileAttributeName.GRAD: grad_dfile,
        _FileAttributeName.HESS: hess_dfile,
        _FileAttributeName.HFREQ: hfreq_dfile})

    return (trunk_ds, leaf_ds)


def energy_transfer(prefix):
    """ construct the energy transfer filesystem (3 layers)

    specifiers:
        0 - []
                files:
                - info
        1 - [ich, chg, mul]
                (no files)
        2 - [ich, chg, mul, method, basis, orb_type]
                files:
                - energy
                - lennard_jones_epsilon
                - lennard_jones_sigma
                - trajectory

    :param prefix: sets the path where this filesystem will sit
    :type prefix: str
    """
    trunk_ds = data_series.energy_transfer_trunk(prefix)
    branch_ds = data_series.energy_transfer_branch(prefix, root_ds=trunk_ds)
    leaf_ds = data_series.energy_transfer_leaf(prefix, root_ds=branch_ds)

    # inp_dfile = data_files.input_file(_FilePrefix.LJ)
    inf_dfile = data_files.information(
        _FilePrefix.LJ, function=info_objects.lennard_jones)
    ene_dfile = data_files.energy(_FilePrefix.LJ)
    eps_dfile = data_files.lennard_jones_epsilon(_FilePrefix.LJ)
    sig_dfile = data_files.lennard_jones_sigma(_FilePrefix.LJ)
    traj_dfile = data_files.trajectory(_FilePrefix.LJ)

    trunk_ds.add_data_files({
        _FileAttributeName.INFO: inf_dfile})

    leaf_ds.add_data_files({
        _FileAttributeName.ENERGY: ene_dfile,
        _FileAttributeName.LJ_EPS: eps_dfile,
        _FileAttributeName.LJ_SIG: sig_dfile,
        _FileAttributeName.TRAJ: traj_dfile})

    return (trunk_ds, branch_ds, leaf_ds)


def reaction(prefix):
    """ construct the reaction filesystem (2 layers)

    specifiers:
        0 - []
                (no files)
        1 - [rxn_ichs, rxn_chgs, rxn_muls, ts_mul]
                (no files)

    :param prefix: sets the path where this filesystem will sit
    :type prefix: str
    """
    trunk_ds = data_series.reaction_trunk(prefix)
    leaf_ds = data_series.reaction_leaf(prefix, root_ds=trunk_ds)

    return (trunk_ds, leaf_ds)


def transition_state(prefix):
    """ construct the ts filesystem (1 layer)

    specifiers:
        0 - []
                files:
                - energy
                - geometry
                - zmatrix

    :param prefix: sets the path where this filesystem will sit
    :type prefix: str
    """
    trunk_ds = data_series.transition_state_trunk(prefix)

    geom_dfile = data_files.geometry(_FilePrefix.GEOM)
    ene_dfile = data_files.energy(_FilePrefix.GEOM)
    zmat_dfile = data_files.zmatrix(_FilePrefix.GEOM)
    trunk_ds.add_data_files({
        _FileAttributeName.ENERGY: ene_dfile,
        _FileAttributeName.GEOM: geom_dfile,
        _FileAttributeName.ZMAT: zmat_dfile})

    return (trunk_ds,)


def direction(prefix):
    """ filesystem object for reaction direction (1 layer)

    specifiers:
        0 - [forw]
                files:
                - geometry_info
                - geometry_input
                - energy
                - geometry
                - zmatrix

    :param prefix: sets the path where this filesystem will sit
    :type prefix: str
    """
    leaf_ds = data_series.direction_leaf(prefix)

    inf_dfile = data_files.information(_FilePrefix.GEOM,
                                       function=info_objects.run)
    inp_dfile = data_files.input_file(_FilePrefix.GEOM)
    ene_dfile = data_files.energy(_FilePrefix.GEOM)
    geom_dfile = data_files.geometry(_FilePrefix.GEOM)
    zmat_dfile = data_files.zmatrix(_FilePrefix.GEOM)

    leaf_ds.add_data_files({
        _FileAttributeName.GEOM_INFO: inf_dfile,
        _FileAttributeName.GEOM_INPUT: inp_dfile,
        _FileAttributeName.ENERGY: ene_dfile,
        _FileAttributeName.GEOM: geom_dfile,
        _FileAttributeName.ZMAT: zmat_dfile})

    return (leaf_ds,)


def run(prefix):
    """ construct the run filesystem (2 layers)

    specifiers:
        0 - []
                files:
                - info
        1 - [job]
                files:
                - info
                - input
                - output

    :param prefix: sets the path where this filesystem will sit
    :type prefix: str
    """
    trunk_ds = data_series.run_trunk(prefix)
    leaf_ds = data_series.run_leaf(prefix, root_ds=trunk_ds)

    inf_dfile = data_files.information(_FilePrefix.RUN,
                                       function=info_objects.run)
    inp_dfile = data_files.input_file(_FilePrefix.RUN)
    out_dfile = data_files.output_file(_FilePrefix.RUN)
    trunk_ds.add_data_files({
        _FileAttributeName.INFO: inf_dfile})
    leaf_ds.add_data_files({
        _FileAttributeName.INFO: inf_dfile,
        _FileAttributeName.INPUT: inp_dfile,
        _FileAttributeName.OUTPUT: out_dfile})

    return (trunk_ds, leaf_ds)


def subrun(prefix):
    """ construct the subrun filesystem (1 layer)

    specifiers:
        0 - [macro_idx, micro_idx]
                files:
                - info
                - input
                - output

    :param prefix: sets the path where this filesystem will sit
    :type prefix: str
    """
    leaf_ds = data_series.subrun_leaf(prefix)

    inf_dfile = data_files.information(_FilePrefix.RUN,
                                       function=info_objects.run)
    inp_dfile = data_files.input_file(_FilePrefix.RUN)
    out_dfile = data_files.output_file(_FilePrefix.RUN)
    leaf_ds.add_data_files({
        _FileAttributeName.INFO: inf_dfile,
        _FileAttributeName.INPUT: inp_dfile,
        _FileAttributeName.OUTPUT: out_dfile})

    return (leaf_ds,)


def build(prefix):
    """ construct the build filesystem (2 layers)

    specifiers:
        0 - [head]
                (no files)
        1 - [head, num]
                files:
                - input
                - output

    :param prefix: sets the path where this filesystem will sit
    :type prefix: str
    """
    trunk_ds = data_series.build_trunk(prefix)
    leaf_ds = data_series.build_leaf(prefix, root_ds=trunk_ds)

    inp_dfile = data_files.input_file(_FilePrefix.BUILD)
    out_dfile = data_files.output_file(_FilePrefix.BUILD)
    leaf_ds.add_data_files({
        _FileAttributeName.INPUT: inp_dfile,
        _FileAttributeName.OUTPUT: out_dfile})

    return (trunk_ds, leaf_ds)


def _process_root_args(root_fs=None, top_ds_name=None):
    if root_fs is not None:
        root_fs = dict(root_fs)
        assert top_ds_name in root_fs
        top_dsdir = root_fs[top_ds_name].dir
    else:
        root_fs = {}
        top_dsdir = None
    return root_fs, top_dsdir
