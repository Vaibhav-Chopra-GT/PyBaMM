import pybamm
import matplotlib.pyplot as plt


parameters = [
    "Marquis2019",
    "NCA_Kim2011",
    "Prada2013",
    "Ramadass2004",
    "Chen2020",
    "Chen2020_plating",
    "Ecker2015",
]

npts = [4, 8, 16, 32, 64]


for params in parameters:
    
    solutions = []

    for N in npts:
        solver = pybamm.CasadiSolver()
        model = pybamm.lithium_ion.DFN()
        parameter_values = pybamm.ParameterValues(params)
        var_pts = {
        "x_n": N,  # negative electrode
        "x_s": N,  # separator 
        "x_p": N,  # positive electrode
        "r_n": N,  # negative particle
        "r_p": N,  # positive particle
        }    
        sim = pybamm.Simulation(
            model, solver=solver, parameter_values=parameter_values, var_pts=var_pts
        )
        time = 0
        for k in range(0, 5):

            solution = sim.solve([0, 3600])
            time += solution.solve_time.value
        time = time / 5
        
        solutions.append(time)

        
    plt.plot(npts, solutions)


plt.gca().legend(
    parameters,
    loc="upper right",
)
plt.title("Work Precision Sets")
plt.xlabel("mesh points")
plt.xticks(npts)
plt.ylabel("time(s)")
plt.show()
