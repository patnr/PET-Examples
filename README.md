# Examples
Folder containing example cases for PIPT and POPT

**Cases:**

- LinearModel   : Fast test for data assimilation methods that does not require an external simulator.
- 3Spot         : Simple case to test optimization methods that runs in less than one minute. The test require OPM or Eclipse. 
- 3SpotRobust   : Simple case to test optimization methods including multiple geo-models.
- 5SpotInverted : Test case of optimize bottom hole pressures in 4 injectors. The model is 2D with 2500 gridcells, and the model has three phase flow. 
- 3dBox         : Data assimilation of a 3D reservoir with 3 injectors and 3 producers. Four different fidelity levels. Set up with ES.
- Rosenbrock    : Minimize the Rosenbrock function (https://en.wikipedia.org/wiki/Rosenbrock_function) in any dimension
