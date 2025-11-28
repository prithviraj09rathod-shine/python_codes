import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import pickle

books = pd.read_csv('books.csv')
users = pd.read_csv('users.csv')
ratings = pd.read_csv('ratings.csv')
print(ratings.shape)
print(users.shape)
print(books.isnull().sum())
print(users.isnull().sum())

print(ratings.isnull().sum())
print(books.duplicated().sum())

print(ratings.duplicated().sum())
print(users.duplicated().sum())

#Popularity Based Recommender System#######
ratings_with_name = ratings.merge(books,on='ISBN')
# Data Cleaning and Merging
#df['your_column'] = pd.to_numeric(df['your_column'], errors='coerce')
#df.groupby('col').mean()

#ratings_with_name['Book-Title'] = pd.to_numeric(ratings_with_name['Book-Title'], errors='coerce')
num_rating_df = ratings_with_name.groupby('Book-Title').count()['Book-Rating'].reset_index()
num_rating_df.rename(columns={'Book-Rating':'num_ratings'},inplace=True)
print(num_rating_df)
print("RESHMA HERE")

#avg rating
#ratings_with_name['Book-Title'] = pd.to_numeric(ratings_with_name['Book-Title'], errors='coerce')
""" avg_rating_df = ratings_with_name.groupby('Book-Title').mean()['Book-Rating'].reset_index()
avg_rating_df.rename(columns={'Book-Rating':'avg_rating'},inplace=True) """
# avg rating
avg_rating_df = ratings_with_name.groupby('Book-Title')['Book-Rating'].mean().reset_index()
avg_rating_df.rename(columns={'Book-Rating': 'avg_rating'}, inplace=True)

print(avg_rating_df)
print("REshma 2nd time")
#popular 
ratings_with_name['Book-Title'] = ratings_with_name['Book-Title'].astype(str)
avg_rating_df['Book-Title'] = avg_rating_df['Book-Title'].astype(str)
final_df = ratings_with_name.merge(avg_rating_df, on='Book-Title', how='left')
print("REshma 3rd time")

#ratings_with_name['Book-Title'] = pd.to_numeric(ratings_with_name['Book-Title'], errors='coerce')
popular_df = num_rating_df.merge(avg_rating_df,on='Book-Title')
popular_df = popular_df.merge(books,on='Book-Title')
popular_df = popular_df[['Book-Title','Book-Author','Image-URL-M','num_ratings','avg_rating']]
popular_df = popular_df[popular_df['num_ratings']>=250].sort_values('avg_rating',ascending=False).head(50)
print(popular_df)
popular_df.to_pickle('popular.pkl')

#Collaborative Filtering Based Recommender System#######
ratings_with_name['Book-Title'] = pd.to_numeric(ratings_with_name['Book-Title'], errors='coerce')
x = ratings_with_name.groupby('User-ID').count()['Book-Rating'] > 200
padhe_likhe_users = x[x].index
filtered_rating = ratings_with_name[ratings_with_name['User-ID'].isin(padhe_likhe_users)]

ratings_with_name['Book-Title'] = pd.to_numeric(ratings_with_name['Book-Title'], errors='coerce')
y = filtered_rating.groupby('Book-Title').count()['Book-Rating']>=50
famous_books = y[y].index
final_ratings = filtered_rating[filtered_rating['Book-Title'].isin(famous_books)]
pt = final_ratings.pivot_table(index='Book-Title',columns='User-ID',values='Book-Rating').fillna(0)
print(pt)
pt.fillna(0,inplace=True)
  
pt.to_pickle('pt.pkl')


similarity_scores = cosine_similarity(pt)
similarity_scores.shape

pickle.dump(popular_df,open('popular.pkl','wb'))
pickle.dump(pt,open('pt.pkl','wb'))
books.drop_duplicates('Book-Title')
pickle.dump(books,open('books.pkl','wb'))
pickle.dump(similarity_scores,open('similarity_scores.pkl','wb'))