# PyPlateModification - Part (b)

This repository contains the conceptual modifications needed to incorporate relative quantities in PyPlate.

## Conceptual Changes

### 1. Modify the Reagent Class
- Update the `Reagent` class to include parameters for equivalents and mol percentages in addition to absolute quantities.
- Ensure validation logic to confirm that only one of the attributes (absolute quantity, equivalents, or mol percentage) is specified.

### 2. Add Methods to Calculate Absolute Quantities
- Implement methods within the `Reagent` class to convert equivalents and mol percentages into absolute quantities based on the limiting reagent.

### 3. Update the Experimental Setup Function
- Modify the experimental setup function to handle the new `Reagent` attributes and ensure the correct conversion of relative quantities to absolute quantities.

### 4. Ensuring Logical and Chemical Reasonableness
- **Validation in the Reagent Class:**
  - Validate that only one of the attributes (`quantity`, `equivalents`, or `mol_percent`) is specified during initialization.
  - Raise an error if multiple attributes are specified or if none are specified.
- **Conversion Method:**
  - Implement a method to accurately convert relative quantities (equivalents and mol percentages) to absolute quantities based on the limiting reagent’s quantity.
- **Error Handling:**
  - Provide appropriate error messages and handling mechanisms to address any issues with specifying relative quantities.

## Docstrings for New or Modified Functions

### Reagent Class Initialization

```plaintext
def __init__(self, name, molecular_weight, quantity=None, equivalents=None, mol_percent=None):
    """
    Initialize a reagent with its name, molecular weight, and optional quantity, equivalents, or mol_percent.

    Parameters:
    name (str): Name of the reagent.
    molecular_weight (float): Molecular weight of the reagent in g/mol.
    quantity (float): Absolute quantity of the reagent in mmol (default is None).
    equivalents (float): Relative quantity of the reagent in equivalents (default is None).
    mol_percent (float): Relative quantity of the reagent in mol% (default is None).

    Note: Either quantity, equivalents, or mol_percent must be specified.
    """
