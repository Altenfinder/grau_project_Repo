import pandas as pd
import quandl
import pandas as pd
import cPickle as pickle


def state_list():
    fiddy_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
    return fiddy_states[0][0][1:]


def grab_initial_state_data():
    states = state_list()

    main_df = pd.DataFrame()

    for abbv in states:
        query = "FMAC/HPI_"+str(abbv)
        df = quandl.get(query, authtoken='o6y_9LNyaENy9Nh9C9Hr')
        print(query)
        if main_df.empty:
            main_df = df
        else:
            main_df = main_df.join(df, lsuffix=abbv)

    pickle_out = open('fiddy_states.pickle','wb')
    pickle.dump(main_df, pickle_out)
    pickle_in = open('fiddy_states.pickle','rb')
    HPI_data = pickle.load(pickle_in)
    print(HPI_data)
    pickle_out.close()


grab_initial_state_data()
