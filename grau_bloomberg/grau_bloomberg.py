import pandas as pd
import blpapi
import tia
import tia.bbg.datamgr as dm
from datetime import datetime
from datetime import timedelta

class grau_bloomberg:
    def __init__(self):
        self.sessionOptions = blpapi.SessionOptions()
        self.sessionOptions.setServerHost("192.168.15.102")
        self.sessionOptions.setServerPort(8194)
        self.session = blpapi.Session(self.sessionOptions)
        if not session.start():
            raise Exception("Can't start session.")
        self.mgr = dm.BbgDataManager()
        self.now = datetime.now()
        self.delta = timedelta(days=200)


    '''
    def get_historical(self, atiovs, delta_days=self.delta):
        pass


        range = 60
        final_date = '%s/%s/%s' % (now.month, now.day, now.year)
        initial_date = '%s/%s/%s' % ((now - delta).month, (now - delta).day, (now - delta).year)

        ticker_bloomberg = pd.DataFrame()
        ticker_bloomberg['ticker'] = df_fundo[pd.notnull(df_fundo["bloomberg_ticker"])]['bloomberg_ticker']
        print ticker_bloomberg
        ticker_bloomberg = ticker_bloomberg.dropna(how='all')
        print ticker_bloomberg

        ativo = ['']

        ### FAZ A BUSCA NA BLOOMBERG
        if (ticker_bloomberg['ticker'] == '').all():
            print 'LISTA VAZIA'
            # ativo = mgr[False]
            df_bloomberg = pd.DataFrame()
        else:
            ativo = mgr[ticker_bloomberg['ticker']]
            df_bloomberg = ativo.get_historical(['PX_LAST'], initial_date, final_date)
    '''
    @staticmethod
    def isin_bloomberg(isin):
        db = pd.read_csv('/usr/lib/python2.7/dist-packages/grau_project/grau_bloomberg/isin_database.csv',dtype={'ticker': str}).set_index('isin')
        if pd.notnull(isin):

            if isin in db.index:
                ticker = db.loc[isin, 'ticker']
                result = ''

                if isinstance(ticker, pd.Series):
                    if (db.loc[isin, 'ticker_type'][0] == 'Equity') or any(db.loc[isin, 'ticker_type'] == 'Equity'):

                        if any(db.loc[isin, 'exchange'] == 'BZ'):
                            result = ticker[np.where(db['exchange'][isin] == 'BZ')[0][0]]

                        elif np.where(db['exchange'][isin] == 'US')[0].size != 0:
                            result = ticker[np.where(db['exchange'][isin] == 'US')[0][0]]

                        elif np.where(db['exchange'][isin] == 'EU')[0].size != 0:
                            result = ticker[np.where(db['exchange'][isin] == 'EU')[0][0]]

                        return result


                    elif (db.loc[isin, 'ticker_type'][0] == 'Corp') or (db.loc[isin, 'ticker_type'][0] == 'Govt'):
                        result = db.loc[isin, 'ticker'][0]
                        return result

                else:
                    return ticker

            else:
                return np.nan

        else:
            return np.nan



if __name__=='__main__':
    pass
