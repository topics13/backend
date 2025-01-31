
def generate_dataset(values):
    import numpy as np

    values_intermediate = [int(value) for value in values]
    values_final = np.array(values_intermediate)

    return [values_final]