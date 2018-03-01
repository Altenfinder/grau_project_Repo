import pandas as pd
import blpapi
import tia
import tia.bbg.datamgr as dm
from datetime import datetime
from datetime import timedelta
from datetime import date
from dateutil.relativedelta import relativedelta

class grau_bloomberg(dm):
    def __init__(self, ativos, initial_date='', final_date='', timedelta = ''):
        self.sessionOptions = blpapi.SessionOptions()
        self.sessionOptions.setServerHost("192.168.15.102")
        self.sessionOptions.setServerPort(8194)
        self.session = blpapi.Session(self.sessionOptions)

        if not self.session.start():
            raise Exception("Can't start session.")
        self.mgr = dm.BbgDataManager()
        self.now = datetime.now()

        if initial_date != '':
            self.initial_date = initial_date
            if isinstance(initial_date, str):
                self.initial_date = datetime.strptime(initial_date,'%Y-%m-%d')

        if final_date != '':
            self.final_date = final_date
            if isinstance(final_date, str):
                self.final_date = datetime.strptime(final_date,'%Y-%m-%d')

        if initial_date != '' and final_date != '':
            self.timedelta = self.final_date - self.initial_date

        elif final_date != '' and initial_date == '':
            self.timedelta = timedelta
            self.initial_date = self.final_date - relativedelta(days=timedelta)

        elif final_date == '' and initial_date == '':
            self.timedelta = timedelta
            self.final_date = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
            self.initial_date = self.final_date - relativedelta(days=timedelta)

        self.ativos = self.mgr[ativos]

    @staticmethod
    def columns_adj(px):
        columns = []
        for column in px.columns:
            columns = columns + [column[0]]
        px.columns = columns
        return px

    def px_last(self):
        return grau_bloomberg.columns_adj(self.ativos.get_historical(['PX_LAST'], self.initial_date, self.final_date))

    def px_mid(self):
        return self.ativos.get_historical(['PX_MID'], self.initial_date, self.final_date)

    def px_open(self):
        return self.ativos.get_historical(['PX_OPEN'], self.initial_date, self.final_date)


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
    ativos = ['VIX Index', 'SPX Index', 'USDBRLV5Y Curncy', 'BZIDINTL Index', 'BRLDDEBT Index', 'IBOV INDEX', 'TED3 Curncy','CBRZ1U5 CBIN Curncy', 'ITRXTX5I Index']
    bloomberg = grau_bloomberg(ativos, final_date=datetime.now(), timedelta=3650)
    print bloomberg.px_last()

    #bloomberg.final_date = '2017dadas'
    # print bloomberg.initial_date
    # print type(bloomberg.final_date)
