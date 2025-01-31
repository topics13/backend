from utility import resources

def fertilizer_predict(crop_attributes):
    import pandas as pd

    crop_name = str(crop_attributes['cropname']).lower()
    N = int(crop_attributes['nitrogen'])
    P = int(crop_attributes['phosphorus'])
    K = int(crop_attributes['pottasium'])

    df = pd.read_csv(resources.FERTILIZER_DATA_CSV)

    nr = df[df['Crop'] == crop_name]['N'].iloc[0]
    pr = df[df['Crop'] == crop_name]['P'].iloc[0]
    kr = df[df['Crop'] == crop_name]['K'].iloc[0]

    n = nr - N
    p = pr - P
    k = kr - K

    temp = {abs(n): "N", abs(p): "P", abs(k): "K"}

    max_value = temp[max(temp.keys())]

    if max_value == "N":
        if n < 0:
            key = 'NHigh'
        else:
            key = "Nlow"
    elif max_value == "P":
        if p < 0:
            key = 'PHigh'
        else:
            key = "Plow"
    else:
        if k < 0:
            key = 'KHigh'
        else:
            key = "Klow"

    prediction = str(resources.fertilizer_dic[key])

    return prediction