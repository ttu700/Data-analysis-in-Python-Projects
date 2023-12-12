import numpy as np

def calculate(list):
    if len(list) < 9:
        raise ValueError("List must contain nine numbers.")
    else:
        array = np.array(list)
        reshaped_array = np.reshape(list, (3,3))
        
        flattened_array = reshaped_array.flatten()

        calculations = {
        'mean': [np.mean(reshaped_array,axis=0).tolist(), np.mean(reshaped_array,axis=1).tolist(), np.mean(flattened_array).tolist()],
        'variance': [np.var(reshaped_array,axis=0).tolist(), np.var(reshaped_array,axis=1).tolist(), np.var(flattened_array).tolist()],
        'standard deviation': [np.std(reshaped_array,axis=0).tolist(), np.std(reshaped_array,axis=1).tolist(), np.std(flattened_array).tolist()],
        'max': [np.max(reshaped_array,axis=0).tolist(), np.max(reshaped_array,axis=1).tolist(), np.max(flattened_array).tolist()],
        'min': [np.min(reshaped_array,axis=0).tolist(), np.min(reshaped_array,axis=1).tolist(), np.min(flattened_array).tolist()],
        'sum': [np.sum(reshaped_array,axis=0).tolist(), np.sum(reshaped_array,axis=1).tolist(), np.sum(flattened_array).tolist()]
    }


    return calculations