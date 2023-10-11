#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def dataFrameCleaner(data):
    """"
    parameter: A dataFrame
    
    
    It cleans the dataset, split it into target and input set, then clean the input data
    
    Return: A tuple containing (input, target)
    """
    data['RiskLevel'] = data['RiskLevel'].astype('category')
    data['BodyTemp'] = data['BodyTemp'].astype(np.float64)
    data['BS'] = data['BS'].astype(np.float64)
    # Changing the RiskLevel to a numerical Variable
    # Replace High Risk by 2
    data['RiskLevel'] = data['RiskLevel'].replace('high risk',2)
    # Replace Mid Risk by 1
    data['RiskLevel'] = data['RiskLevel'].replace('mid risk',1)
    # Replace Low Risk by 0
    data['RiskLevel'] = data['RiskLevel'].replace('low risk',0)
    # Convert the RiskLevel to the integer type
    data['RiskLevel'] = data['RiskLevel'].astype(int)
    targets = data['RiskLevel']
    inputs = data.drop('RiskLevel', axis=1)
    scaled_test_data = std_scaler.transform(inputs)
    return inputs, targets

