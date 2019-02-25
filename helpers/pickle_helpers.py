import pickle

'''
Store and load anything to and from pickle
'''

def convert_to_pickle(item, directory):
    '''
    Usage: convert dictionary object to pickle format
    pickle_helpers.convert_to_pickle(cat_list,"data/liwc_pickle/liwc_cat.p")
    '''

    pickle.dump(item, open(directory,"wb"))


def load_from_pickle(directory):
    '''
    Usage: Load pickle file
    pickle_helpers.load_from_pickle("data/liwc_pickle/liwc_cat.p")
    '''

    return pickle.load(open(directory,"rb"))
