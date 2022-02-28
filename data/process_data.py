import sys
import pandas as pd
from sqlalchemy import create_engine

def load_data(messages_filepath, categories_filepath):
    '''load data from message and categries data from csv,
    and return merged pandas dataframe'''
    messages = pd.read_csv(messages_filepath)
    categories = pd.read_csv(categories_filepath)
    
    # merge datasets
    df = pd.merge(messages, categories, on="id")
    
    return df


def clean_data(df):
    ''' clean and return dataframe'''
    # create a dataframe of the 36 individual category columns
    categories = df["categories"].str.split(";", expand=True)
    
    # select the first row of the categories dataframe
    row = categories.iloc[0]
    
    # remove last 2 characters of catergory names
    category_colnames = [val[:-2] for val in row]
    
    # rename the columns of `categories`
    categories.columns = category_colnames
    
    for column in categories:
        # set each value to be the last character of the string
        categories[column] = categories[column].str[-1]
    
        # convert column from string to numeric
        categories[column] = pd.to_numeric(categories[column], downcast="integer")
    
    # drop the original categories column from `df`
    df.drop("categories", axis=1, inplace=True)
    
    # concatenate the original dataframe with the new `categories` dataframe
    df = pd.concat([df, categories], axis=1, sort=False)
    
    # drop duplicates
    df.drop(df[df.duplicated(keep="first")].index, inplace=True)
    
    # There is a category 2 in 'related' column. This could be an error. 
    # In the absense of any information, we assume it to be 1 as the majority class.
    df['related']=df['related'].map(lambda x: 1 if x == 2 else x)
    
    return df

def save_data(df, database_filename):
    '''save dataframe as sql database file'''
    engine = create_engine('sqlite:///' + database_filename)
    df.to_sql('DisasterResponseDatabase', engine, if_exists='replace', index=False)  


def main():
    if len(sys.argv) == 4:

        messages_filepath, categories_filepath, database_filepath = sys.argv[1:]

        print('Loading data...\n    MESSAGES: {}\n    CATEGORIES: {}'
              .format(messages_filepath, categories_filepath))
        df = load_data(messages_filepath, categories_filepath)

        print('Cleaning data...')
        df = clean_data(df)
        
        print('Saving data...\n    DATABASE: {}'.format(database_filepath))
        save_data(df, database_filepath)
        
        print('Cleaned data saved to database!')
    
    else:
        print('Please provide the filepaths of the messages and categories '\
              'datasets as the first and second argument respectively, as '\
              'well as the filepath of the database to save the cleaned data '\
              'to as the third argument. \n\nExample: python process_data.py '\
              'disaster_messages.csv disaster_categories.csv '\
              'DisasterResponse.db')


if __name__ == '__main__':
    main()
