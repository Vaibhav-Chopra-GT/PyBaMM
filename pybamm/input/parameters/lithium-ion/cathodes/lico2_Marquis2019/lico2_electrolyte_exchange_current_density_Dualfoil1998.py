from pybamm import exp, constants, standard_parameters_lithium_ion, Scalar


def lico2_electrolyte_exchange_current_density_Dualfoil1998(c_e, c_s_surf, T):
    """
    Exchange-current density for Butler-Volmer reactions between lico2 and LiPF6 in
    EC:DMC.

    References
    ----------
    .. [2] http://www.cchem.berkeley.edu/jsngrp/fortran.html

    Parameters
    ----------
    c_e : :class:`pybamm.Symbol`
        Electrolyte concentration [mol.m-3]
    c_s_surf : :class:`pybamm.Symbol`
        Particle concentration [mol.m-3]
    T : :class:`pybamm.Symbol`
        Temperature [K]

    Returns
    -------
    :class:`pybamm.Symbol`
        Exchange-current density [A.m-2]
    """
    m_ref = Scalar(
        6 * 10 ** (-7), {"A": 1, "m": 2.5, "mol": -1.5}
    )  # (A/m2)(m3/mol)**1.5 - includes ref concentrations
    E_r = Scalar(39570, "[J.mol-1]")
    arrhenius = exp(E_r / constants.R * (1 / Scalar(298.15, "[K]") - 1 / T))

    c_p_max = standard_parameters_lithium_ion.c_p_max

    return (
        m_ref * arrhenius * c_e ** 0.5 * c_s_surf ** 0.5 * (c_p_max - c_s_surf) ** 0.5
    )
