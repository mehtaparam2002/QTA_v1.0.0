import QTA.Signals.ClassifyBar


def create_bar_list(data_frame):
    """
    Converts a data frame to a list of bars
    :params: data_frame: pandas data frame of stock data
    :returns: List of bars
    """
    output = []
    i = 0
    for i in range(len(data_frame)):
        output.append(ClassifyBar(data_frame.iat[i,2], 
        data_frame.iat[i,3], data_frame.iat[i,0], 
        data_frame.iat[i,1], data_frame.iat[i,4], 
        data_frame.iloc[i].name))
    
    return output
    
def format_df(data):
    r = data['Adj Close'] / data['Close']
    ohlc_cols = ['Open', 'High', 'Low', 'Close']
    data[ohlc_cols] = data[ohlc_cols].mul(r, axis=0)
    data = data.drop('Adj Close', axis=1)
    data = data.rename(columns={'Open': 'O', 'High': 'H', 'Low': 'L',
                                'Close': 'C', 'Adj Close': 'AC',
                                'Volume': 'V'})
    return data