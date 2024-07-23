import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Set random seed for reproducibility
np.random.seed(42)

# Constants
NUM_REACTIONS = 12
REACTION_VOLUME = 200  # uL
WELL_PLATE_MAX_VOLUME = 500  # uL

# Fixed molecular weights for Pd(OAc)2 and ligands
MW_PdOAc2 = 224.50  # g/mol (real molecular weight of Pd(OAc)2)
MW_XPhos = 586.51  # g/mol (real molecular weight of XPhos)
MW_SPhos = 568.47  # g/mol (real molecular weight of SPhos)
MW_dppf = 746.54  # g/mol (real molecular weight of dppf)

# Generate random molecular weights for Ai and Bi
MW_Ai = np.random.uniform(100, 500, NUM_REACTIONS)  # g/mol
MW_Bi = np.random.uniform(100, 500, NUM_REACTIONS)  # g/mol

# Experimental conditions
temperatures = [60, 80]  # °C
solvents = ['toluene', 'glyme', 'TBME', 'dichloroethane']
ligands = ['XPhos', 'SPhos', 'dppf']

# Function to calculate the amounts of reagents
def calculate_amounts(mw_A, mw_B, mol_fraction_A, mol_fraction_B, mol_fraction_Pd, mol_fraction_ligand):
    """
    Calculate the amounts of reagents in milligrams based on their molecular weights and molar fractions.

    Parameters:
    mw_A (float): Molecular weight of reagent A (g/mol).
    mw_B (float): Molecular weight of reagent B (g/mol).
    mol_fraction_A (float): Molar fraction of reagent A.
    mol_fraction_B (float): Molar fraction of reagent B.
    mol_fraction_Pd (float): Molar fraction of Pd(OAc)2.
    mol_fraction_ligand (float): Molar fraction of the ligand.

    Returns:
    tuple: Amounts of A, B, Pd(OAc)2, XPhos, SPhos, and dppf in milligrams.
    """
    mmol_A = mol_fraction_A
    mmol_B = mol_fraction_B * mol_fraction_A
    mmol_Pd = mol_fraction_Pd * mol_fraction_A
    mmol_ligand = mol_fraction_ligand * mol_fraction_A
    
    mg_A = mmol_A * mw_A
    mg_B = mmol_B * mw_B
    mg_Pd = mmol_Pd * MW_PdOAc2
    mg_ligand_XPhos = mmol_ligand * MW_XPhos
    mg_ligand_SPhos = mmol_ligand * MW_SPhos
    mg_ligand_dppf = mmol_ligand * MW_dppf
    
    return mg_A, mg_B, mg_Pd, mg_ligand_XPhos, mg_ligand_SPhos, mg_ligand_dppf

# Create a DataFrame to store the experimental design
columns = ['Reaction', 'Ai (mg)', 'Bi (mg)', 'Pd(OAc)2 (mg)', 'Ligand (mg)', 'Temperature (°C)', 'Solvent', 'Ligand Type']
data = []

# Generate the experimental design
for i in range(NUM_REACTIONS):
    for temp in temperatures:
        for solvent in solvents:
            for ligand in ligands:
                mg_A, mg_B, mg_Pd, mg_XPhos, mg_SPhos, mg_dppf = calculate_amounts(
                    MW_Ai[i], MW_Bi[i], 0.1, 1.1, 0.1, 0.15)
                
                ligand_amount = {'XPhos': mg_XPhos, 'SPhos': mg_SPhos, 'dppf': mg_dppf}
                data.append([f'Reaction {i+1}', mg_A, mg_B, mg_Pd, ligand_amount[ligand], temp, solvent, ligand])

df_experiment = pd.DataFrame(data, columns=columns)

# Save the design to a CSV file
df_experiment.to_csv('experimental_design_a.csv', index=False)

# Plotting the experimental design concept
fig, ax = plt.subplots(figsize=(10, 6))
num_conditions = len(temperatures) * len(solvents) * len(ligands)
y_pos = np.arange(NUM_REACTIONS)
bar_width = 0.2

# Create stacked bar chart to show distribution of conditions
for i, temp in enumerate(temperatures):
    for j, solvent in enumerate(solvents):
        for k, ligand in enumerate(ligands):
            ax.barh(y_pos + (i*len(solvents)*len(ligands) + j*len(ligands) + k)*bar_width, [1]*NUM_REACTIONS, height=bar_width, label=f'T: {temp}°C, S: {solvent}, L: {ligand}')

ax.set_yticks(y_pos + bar_width * num_conditions / 2)
ax.set_yticklabels([f'Reaction {i+1}' for i in range(NUM_REACTIONS)])
ax.set_xlabel('Experimental Conditions')
ax.set_title('Experimental Design for Cross-Coupling Reactions')
ax.legend()

plt.tight_layout()
plt.show()
