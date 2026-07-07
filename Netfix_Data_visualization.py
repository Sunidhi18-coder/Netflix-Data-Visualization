import pandas as pd
import matplotlib.pyplot as plt
pd.set_option("display.max_columns",None)
pd.set_option("display.max_rows",None)


# Load the dataset
df= pd.read_csv('netflix_titles.csv')

# clean data set
df= df.dropna(subset=["type", "release_year","rating","country","duration"])

type_counts = df["type"].value_counts()
plt.figure(figsize=(6,4))
plt.bar(type_counts.index, type_counts.values, color= ["skyblue","orange"])
plt.title("Number of Movies VS TV Shows on Netflix")
plt.xlabel("Type")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("Movies_vs_tvshows.png")
plt.show()

# findout rating 
rating_counts = df["rating"].value_counts()
plt.figure(figsize=(8,6))
plt.pie(rating_counts, labels=rating_counts.index, autopct="%1.1f%%", startangle=90)
plt.title("Percentage of Content Rating")
plt.tight_layout()
plt.savefig("content_ratings.png")
plt.show()

# distrubution of movie duration 

movie_df= df[df["type"] == "Movie"].copy()
movie_df["duration_int"]= movie_df["duration"].str.replace("min", "").astype(int)
plt.figure(figsize=(8,6))
plt.hist(movie_df['duration_int'], bins=30, color='purple', edgecolor= 'black')
plt.title("Distribution of Movie Distribution")
plt.xlabel("Duration(in minutes)")
plt.ylabel("Number of Movies")
plt.tight_layout()
plt.savefig("Movies_Duration.png")
plt.show()

release_count= df['release_year'].value_counts().sort_index()
plt.figure(figsize=(10,6))
plt.scatter(release_count.index,release_count.values, color= 'red')
plt.title('Release Year VS Number of Shows')
plt.xlabel('Release Year')
plt.ylabel('Number of Shows')
plt.tight_layout()
plt.savefig('Release_Year.png')
plt.show()

country_counts= df['country'].value_counts().head(10)
plt.figure(figsize=(8,6))
plt.barh(country_counts.index, country_counts.values, color= 'teal')
plt.title('Top 10 Countries by Number of Shows')
plt.xlabel('Number of Shows')
plt.ylabel('Countries')
plt.tight_layout()
plt.savefig('Top_10_Countries.png')
plt.show()

content_by_year= df.groupby(['release_year','type']).size().unstack().fillna(0)

fig, ax = plt.subplots(1,2, figsize= (12,5))
# first subplot : movies
ax[0].plot(content_by_year.index, content_by_year['Movie'], color= 'blue')
ax[0].set_title("Movie Release Per Year")
ax[0].set_xlabel('Year')
ax[0].set_ylabel('Number of Movies')

# second subplot : TV Shows
ax[1].plot(content_by_year.index, content_by_year['TV Show'], color= 'orange')
ax[1].set_title("TV Shows Release Per Year")
ax[1].set_xlabel('Year')
ax[1].set_ylabel('Number of TV Shows')

fig.suptitle("Comparison of Movies and TV Shows Released Over Years")
plt.tight_layout()
plt.savefig('Movies_TV_Shows_Comparison.png')
plt.show()