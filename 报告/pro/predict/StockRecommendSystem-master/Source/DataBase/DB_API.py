import os, datetime, pymongo, configparser
import pandas as pd
from bson import json_util

global_config = None
global_client = None
global_stocklist = None

def getConfig(root_path):
    global global_config
    if global_config is None:
        #print("initial Config...")
        global_config = configparser.ConfigParser()
        global_config.read(root_path + "/" + "config.ini")
    return global_config

def getClient():
    global global_client
    from pymongo import MongoClient
    if global_client is None: 
        #print("initial DB Client...")
        global_client = MongoClient('localhost', 27017)
    return global_client

def getCollection(database, collection):
    client = getClient()
    db = client[database]
    return db[collection]

def getStockList(root_path, database, sheet):
    global global_stocklist
    if global_stocklist is None:
        #print("initial Stock List...")
        global_stocklist = queryStockList(root_path, database, sheet)
    return global_stocklist

def setStockList(df):
    global global_stocklist
    df.set_index('symbol', inplace=True)
    global_stocklist = df
    return global_stocklist

def readFromCollection(collection, queryString=None):
    if queryString is None:
        result = collection.find()
    else:
        result = collection.find(queryString)
    
    df = pd.DataFrame(list(result))
    if df.empty == False: del df['_id']
    return df

def writeToCollection(collection, df, id = None):
    jsonStrings = df.to_json(orient='records')
    bsonStrings = json_util.loads(jsonStrings)
    for string in bsonStrings:
        if id is not None:
            id_string = ''.join([string[item] for item in id])
            string['_id'] = id_string
        collection.save(string)

def readFromCollectionExtend(collection, queryString=None):
    if queryString is None:
        result = collection.find()
    else:
        result = collection.find_one(queryString)

    if result is None:
        return pd.DataFrame(), {}

    return pd.read_json(result['data'], orient='records'), result['metadata']

def writeToCollectionExtend(collection, symbol, df, metadata=None):
    jsonStrings = {"_id":symbol, "symbol":symbol, "data":df.to_json(orient='records'), "metadata":metadata}
    #bsonStrings = json_util.loads(jsonStrings)
    collection.save(jsonStrings)

def writeToCSV(csv_dir, CollectionKey, df):
    if os.path.exists(csv_dir) == False:
        os.makedirs(csv_dir)
    filename = csv_dir + CollectionKey + '.csv'
    df.to_csv(filename)


def queryStockList(root_path, database, sheet):
    CollectionKey = sheet + "_LIST"
    config = getConfig(root_path)
    storeType = int(config.get('Setting', 'StoreType'))
    
    try:
        if storeType == 1:
            collection = getCollection(database, CollectionKey)
            df = readFromCollection(collection)
            if df.empty == False: df = setStockList(df)
            return df
            
        if storeType == 2:
            csv_dir = root_path + "/" + config.get('Paths', database) + config.get('Paths', sheet) + config.get('Paths', 'CSV_SHARE')
            filename = csv_dir + CollectionKey + '.csv'
            if os.path.exists(filename): 
                df = pd.read_csv(filename, index_col=0)
                if df.empty == False: df = setStockList(df)
                return df
            return pd.DataFrame()

    except Exception as e:
        print("queryStockList Exception", e)
        return pd.DataFrame()
    
    return pd.DataFrame()

def storeStockList(root_path, database, sheet, df, symbol = None):
    CollectionKey = sheet + "_LIST"
    config = getConfig(root_path)
    storeType = int(config.get('Setting', 'StoreType')) 

    try:
        if storeType == 1:
            collection = getCollection(database, CollectionKey)
            if symbol is not None:
                df = df[df.index == symbol].reset_index()

            writeToCollection(collection, df, ['symbol'])
            # try:
            #     index_info = collection.index_information()
            #     print("index info", index_info)
            # except Exception as e:
            #     print(e)
            #     writeToCollection(collection, df)
            #     #collection.create_index('symbol', unique=True, drop_dups=True)
            # else:
            #     writeToCollection(collection, df)

        if storeType == 2:
            csv_dir = root_path + "/" + config.get('Paths', database) + config.get('Paths', sheet) + config.get('Paths', 'CSV_SHARE')
            writeToCSV(csv_dir, CollectionKey, df)
    
    except Exception as e:
        print("storeStockList Exception", e)


def queryStockPublishDay(root_path, database, sheet, symbol):
    CollectionKey = sheet + "_IPO"
    config = getConfig(root_path)
    storeType = int(config.get('Setting', 'StoreType'))

    try:
        if storeType == 1:
            collection = getCollection(database, CollectionKey)
            df = readFromCollection(collection)
            if df.empty == False:
                publishDay = df[df['symbol'] == symbol]
                if len(publishDay) == 1:
                    return publishDay['date'].values[0]
            return ''

        if storeType == 2:
            csv_dir = root_path + "/" + config.get('Paths', database) + config.get('Paths', sheet) + config.get('Paths', 'CSV_SHARE')
            filename = csv_dir + CollectionKey + '.csv'
            if os.path.exists(filename) == False: return ''
            df = pd.read_csv(filename, index_col=["index"])
            if df.empty == False:
                publishDay = df[df['symbol'] == symbol]
                if len(publishDay) == 1:
                    return publishDay['date'].values[0]
            return ''

    except Exception as e:
        print("queryStockPublishDay Exception", e)
        return ''
    return ''


def storePublishDay(root_path, database, sheet, symbol, date):
    CollectionKey = sheet + "_IPO"
    config = getConfig(root_path)
    storeType = int(config.get('Setting', 'StoreType'))

    try:
        if storeType == 1:
            collection = getCollection(database, CollectionKey)
            df = pd.DataFrame(columns = ['symbol', 'date'])
            df.index.name = 'index'
            df.loc[len(df)] = [symbol, date]
            writeToCollection(collection, df)

        if storeType == 2:
            csv_dir = root_path + "/" + config.get('Paths', database) + config.get('Paths', sheet) + config.get('Paths', 'CSV_SHARE')
            filename = csv_dir + CollectionKey + '.csv'
            if os.path.exists(filename):
                df = pd.read_csv(filename, index_col=["index"])
                publishDate = df[df['symbol'] == symbol]
                if publishDate.empty:
                    df.loc[len(df)] = [symbol, date]
            else:   
                df = pd.DataFrame(columns = ['symbol', 'date'])
                df.index.name = 'index'
                df.loc[len(df)] = [symbol, date]
            writeToCSV(csv_dir, CollectionKey, df)
    
    except Exception as e:
        print("storePublishDay Exception", e)


def queryStock(root_path, database, sheet_1, sheet_2, symbol, update_key):
    CollectionKey = sheet_1 + sheet_2 + '_DATA'
    config = getConfig(root_path)
    storeType = int(config.get('Setting', 'StoreType'))
    stockList = getStockList(root_path, database, sheet_1)
    lastUpdateTime = pd.Timestamp(stockList.loc[symbol][update_key])

    try:
        if storeType == 1:
            collection = getCollection(database, CollectionKey)
            queryString = { "symbol" : symbol }
            df, metadata = readFromCollectionExtend(collection, queryString)
            if df.empty: return pd.DataFrame(), lastUpdateTime
            df.set_index('date', inplace=True)
            if 'index' in df:
                del df['index']
            return df, lastUpdateTime
            
        if storeType == 2:
            csv_dir = root_path + "/" + config.get('Paths', database) + config.get('Paths', sheet) 
            filename = csv_dir + symbol + '.csv'
            if os.path.exists(filename) == False: return pd.DataFrame(), lastUpdateTime
            df = pd.read_csv(filename, index_col=["date"])
            return df, lastUpdateTime
        
    except Exception as e:
        print("queryStock Exception", e)
        return pd.DataFrame(), lastUpdateTime

    return pd.DataFrame(), lastUpdateTime


def storeStock(root_path, database, sheet_1, sheet_2, symbol, df, update_key):
    CollectionKey = sheet_1 + sheet_2 + '_DATA'
    config = getConfig(root_path)
    storeType = int(config.get('Setting', 'StoreType'))
    
    now_date = datetime.datetime.now().strftime("%Y-%m-%d")
    stockList = getStockList(root_path, database, sheet_1)
    
    if (stockList[stockList.index == symbol][update_key][0] != now_date):
        stockList.set_value(symbol, update_key, now_date)
        storeStockList(root_path, database, sheet_1, stockList, symbol)

    #     df.set_index('date')  
    #     df.index = df.index.astype(str)
    #     df.sort_index(ascending=True, inplace=True)
    
    try:
        if storeType == 1:
            collection = getCollection(database, CollectionKey)
            df = df.reset_index()
            if 'date' in df: df.date = df.date.astype(str)
            writeToCollectionExtend(collection, symbol, df, {})

        if storeType == 2:
            csv_dir = root_path + "/" + config.get('Paths', database)+ config.get('Paths', sheet) 
            writeToCSV(csv_dir, symbol, df)

    except Exception as e:
        print("storeStock Exception", e)

def queryNews(root_path, database, sheet, symbol):
    config = getConfig(root_path)
    storeType = int(config.get('Setting', 'StoreType'))
    lastUpdateTime = pd.Timestamp(getStockList(root_path, database, 'SHEET_US_DAILY').loc[symbol]['news_update'])

    try:
        if storeType == 1:
            collection = getCollection(database, sheet)
            queryString = { "symbol" : symbol }
            df = readFromCollection(collection, queryString)
            if df.empty: return pd.DataFrame(), lastUpdateTime
            #df.set_index('date', inplace=True)
            return df, lastUpdateTime

        if storeType == 2:
            dir = root_path + "/" + config.get('Paths', database) + config.get('Paths', sheet)
            filename = dir + symbol + '.csv'
            if os.path.exists(filename) == False: return pd.DataFrame(), lastUpdateTime
            df = pd.read_csv(filename)
            return df, lastUpdateTime
    
    except Exception as e:
        print("queryNews Exception", e)
        return pd.DataFrame(), lastUpdateTime

    return pd.DataFrame(), lastUpdateTime


def storeNews(root_path, database, sheet, symbol, df):
    config = getConfig(root_path)
    storeType = int(global_config.get('Setting', 'StoreType'))
    now_date = datetime.datetime.now().strftime("%Y-%m-%d")
    
    now_date = datetime.datetime.now().strftime("%Y-%m-%d")
    stockList = getStockList(root_path, database, 'SHEET_US_DAILY')
    stockList.set_value(symbol, 'news_update', now_date)
    storeStockList(root_path, database, "SHEET_US_DAILY", stockList.reset_index())

    df = df.drop_duplicates(subset=['uri'], keep='first')
    #df.set_index(['date'], inplace=True)
    #df.sort_index(ascending=True, inplace=True)
    
    try:
        if storeType == 1:
            collection = getCollection(database, sheet)
            #df = df.reset_index()
            df['symbol'] = symbol
            writeToCollection(collection, df, ['symbol', 'uri'])

        if storeType == 2:
            csv_dir = root_path + "/" + config.get('Paths', database) + config.get('Paths', sheet)
            writeToCSV(csv_dir, symbol, df)
    
    except Exception as e:
        print("storeNews Exception", e)


def queryEarnings(root_path, database, sheet, date):
    config = getConfig(root_path)
    storeType = int(config.get('Setting', 'StoreType'))

    try:
        if storeType == 1:
            collection = getCollection(database, sheet)
            queryString = { "symbol" : date }
            df, metadata = readFromCollectionExtend(collection, queryString)
            return df
        
        if storeType == 2:
            dir = root_path + "/" + config.get('Paths', database) + config.get('Paths', sheet)
            filename = dir + date + ".csv"
            if os.path.exists(filename): return pd.read_csv(filename)
            return pd.DataFrame()

    except Exception as e:
        print("queryEarnings Exception", e)
        return pd.DataFrame()

    return pd.DataFrame()

def storeEarnings(root_path, database, sheet, date, df):
    config = getConfig(root_path)
    storeType = int(config.get('Setting', 'StoreType'))
    now_date = datetime.datetime.now().strftime("%Y-%m-%d")
    
    try:
        if storeType == 1:
            collection = getCollection(database, sheet)
            writeToCollectionExtend(collection, date, df)

        if storeType == 2:
            csv_dir = root_path + "/" + config.get('Paths', database) + config.get('Paths', sheet)
            writeToCSV(csv_dir, date, df)

    except Exception as e:
        print("storeNews Exception", e)


def queryTweets(root_path, database, sheet, symbol, col):
    config = getConfig(root_path)
    storeType = int(config.get('Setting', 'StoreType'))
    lastUpdateTime = pd.Timestamp('1970-01-01')

    try:
        if storeType == 1:
            collection = getCollection(database, sheet)
            queryString = { "symbol" : symbol }
            df, metadata = readFromCollectionExtend(collection, queryString)
            if 'last_update' in metadata:
                lastUpdateTime = pd.Timestamp(metadata['last_update'])
            if df.empty: return pd.DataFrame(columns=col), lastUpdateTime
            df.set_index('Date')
            return df, lastUpdateTime

        if storeType == 2:
            dir = root_path + "/" + config.get('Paths', database) + config.get('Paths', sheet)
            filename = dir + symbol + ".csv"
            if os.path.exists(filename) == False: return pd.DataFrame(columns=col), lastUpdateTime
            df = pd.read_csv(filename)
            if df.empty: return pd.DataFrame(columns=col), lastUpdateTime
            if 'last_update' in df:
                lastUpdateTime = pd.Timestamp(df['last_update'].iloc[0])
            return df, lastUpdateTime

    except Exception as e:
        print("queryTweets Exception", e)
        return pd.DataFrame(columns=col), lastUpdateTime

    return pd.DataFrame(columns=col), lastUpdateTime


def storeTweets(root_path, database, sheet, symbol, df):
    config = getConfig(root_path)
    storeType = int(config.get('Setting', 'StoreType'))
    now_date = datetime.datetime.now().strftime("%Y-%m-%d")
    df = df.drop_duplicates(keep='last')
    df = df.sort_values(['Date'], ascending=[False]).reset_index(drop=True)
    
    try:
        if storeType == 1:
            collection = getCollection(database, sheet)
            metadata = {'last_update':now_date}
            df = df.reset_index()
            writeToCollectionExtend(collection, symbol, df, metadata)
        
        if storeType == 2:
            df['last_update'] = now_date
            csv_dir = root_path + "/" + config.get('Paths', database) + config.get('Paths', sheet)
            writeToCSV(csv_dir, symbol, df)

    except Exception as e:
        print("storeTweets Exception", e)


def queryCorrelation(root_path, database, sheet):
    config = getConfig(root_path)
    storeType = int(global_config.get('Setting', 'StoreType'))

    try:
        if storeType == 1:
            collection = getCollection(database, sheet)
            return readFromCollection(collection)
        
        if storeType == 2:
            dir = root_path + "/" + config.get('Paths', database) + config.get('Paths', sheet)
            filename = dir + "Correlation" + ".csv"
            if os.path.exists(filename): return pd.read_csv(filename, index_col=0)
            return pd.DataFrame()

    except Exception as e:
        print("queryCorrelation Exception", e)
        return pd.DataFrame()

    return pd.DataFrame()


def storeCorrelation(root_path, database, sheet, df):
    config = getConfig(root_path)
    storeType = int(global_config.get('Setting', 'StoreType'))

    now_date = datetime.datetime.now().strftime("%Y-%m-%d")

    try:
        if storeType == 1:
            collection = getCollection(database, sheet)
            writeToCollection(collection, df)
        
        if storeType == 2:
            csv_dir = root_path + "/" + config.get('Paths', database) + config.get('Paths', sheet)
            writeToCSV(csv_dir, "Correlation", df)
    
    except Exception as e:
        print("storeCorrelation Exception", e)