def first_drop():
    data.dropna(axis=0, how = "all", inplace = True)
    return data