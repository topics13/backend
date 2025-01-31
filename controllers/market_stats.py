from utility import resources

def market_stats(crop_attributes):
    import pandas as pd
    import math

    data = pd.read_csv(resources.MARKET_STATS_CSV)

    states = data.loc[:,'state'].unique()
    crops = data.loc[:,'crop'].unique()

    try:
        state = crop_attributes['state']
    except:
        state = 'All'
    
    try:
        crop = crop_attributes['crop']
    except:
        crop = 'All'

    if len(state) == 0 and len(crop) == 0:
        return []
    
    crop = 'All' if len(crop) == 0 else crop
    
    if len(state) != 0 and crop == 'All':
        result = data['state'].str.contains(state)
        result = data[result][:]

        lt = []
        for index, row in result.iterrows():
            lst = []
            lst = [row['state'],row['crop'],math.floor(row['profit'])]
            lt.append(lst)

    elif len(state) != 0 and crop != 'All':
        result = data['state'].str.contains(state)
        result = data[result][:]
        result = result[result['crop'] == crop]
        lt = []
        for index, row in result.iterrows():
            lst = []
            lst = [row['state'],row['crop'],row['profit']]
            lt.append(lst)
    
    lt = [item for item in lt if item[2] >= 0]

    return lt