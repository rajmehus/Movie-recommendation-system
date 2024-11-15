

# import streamlit as st
# import pandas as pd
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics.pairwise import linear_kernel
# import os

# # Load datasets
# @st.cache_data
# def load_data():
#     try:
#         # Update paths if necessary
#         movies_path = 'movies.csv'
#         ratings_path = 'ratings.csv'
        
#         if not os.path.exists(movies_path):
#             raise FileNotFoundError(f"File not found: {movies_path}")
#         if not os.path.exists(ratings_path):
#             raise FileNotFoundError(f"File not found: {ratings_path}")
        
#         movies = pd.read_csv(movies_path)
#         ratings = pd.read_csv(ratings_path)
#         return movies, ratings
#     except FileNotFoundError as e:
#         st.error(str(e))
#         return None, None

# # Prepare data
# @st.cache_resource
# def prepare_data(movies, ratings):
#     if movies is None or ratings is None:
#         return None, None, None, None
    
#     # Merge datasets
#     df = pd.merge(ratings, movies, how='left', on='movieId')
    
#     # Calculate cosine similarity matrix based on genres
#     cv = TfidfVectorizer()
#     tfidf_matrix = cv.fit_transform(movies['genres'])
#     cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
    
#     # Create index for movie titles
#     indices = pd.Series(movies.index, index=movies['title'])
#     return df, cosine_sim, indices, movies['title']

# # Recommendation function
# def get_recommendations(title, cosine_sim, indices, titles):
#     if indices is None or title not in indices:
#         return []
    
#     idx = indices[title]
#     sim_scores = list(enumerate(cosine_sim[idx]))
#     sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
#     sim_scores = sim_scores[1:6]  # Get top 5 recommendations
#     movie_indices = [i[0] for i in sim_scores]
#     return titles.iloc[movie_indices].tolist()

# # Streamlit app
# st.title("Movie Recommendation System")

# # Load data
# movies, ratings = load_data()
# if movies is not None and ratings is not None:
#     df, cosine_sim, indices, titles = prepare_data(movies, ratings)

#     # User input
#     st.sidebar.header("Enter a Movie Name")
#     user_movie = st.sidebar.text_input("Movie Name", "")

#     # Display recommendations
#     if user_movie and movies is not None and ratings is not None:
#         recommendations = get_recommendations(user_movie, cosine_sim, indices, titles)
#         if len(recommendations) > 0:  # Check if recommendations are not empty
#             st.subheader(f"Recommendations for '{user_movie}':")
#             for i, movie in enumerate(recommendations, start=1):
#                 st.write(f"{i}. {movie}")
#         else:
#             st.subheader("No recommendations found. Please enter a valid movie name.")
# else:
#     st.warning("Please ensure both 'movies.csv' and 'rating.csv' files are available.")


#the second code we have get


# import streamlit as st
# import pandas as pd
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics.pairwise import linear_kernel
# import os

# # Load datasets
# @st.cache_data
# def load_data():
#     try:
#         # Update paths if necessary
#         movies_path = 'movies.csv'
#         ratings_path = 'ratings.csv'
        
#         if not os.path.exists(movies_path):
#             raise FileNotFoundError(f"File not found: {movies_path}")
#         if not os.path.exists(ratings_path):
#             raise FileNotFoundError(f"File not found: {ratings_path}")
        
#         movies = pd.read_csv(movies_path)
#         ratings = pd.read_csv(ratings_path)
#         return movies, ratings
#     except FileNotFoundError as e:
#         st.error(str(e))
#         return None, None

# # Prepare data
# @st.cache_resource
# def prepare_data(movies, ratings):
#     if movies is None or ratings is None:
#         return None, None, None, None
    
#     # Merge datasets
#     df = pd.merge(ratings, movies, how='left', on='movieId')
    
#     # Calculate cosine similarity matrix based on genres
#     cv = TfidfVectorizer()
#     tfidf_matrix = cv.fit_transform(movies['genres'])
#     cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
    
#     # Create index for movie titles
#     indices = pd.Series(movies.index, index=movies['title'])
#     return df, cosine_sim, indices, movies['title']

# # Recommendation function
# def get_recommendations(title, cosine_sim, indices, titles):
#     if indices is None or title not in indices:
#         return []
    
#     idx = indices[title]
#     sim_scores = list(enumerate(cosine_sim[idx]))
#     sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
#     sim_scores = sim_scores[1:11]  # Get top 10 recommendations
#     movie_indices = [i[0] for i in sim_scores]
#     return titles.iloc[movie_indices].tolist()

# # Streamlit app
# st.title("Movie Recommendation System")

# # Load data
# movies, ratings = load_data()
# if movies is not None and ratings is not None:
#     df, cosine_sim, indices, titles = prepare_data(movies, ratings)

#     # User input
#     st.sidebar.header("Enter a Movie Name")
#     partial_movie = st.sidebar.text_input("Movie Name (or partial name)", "").strip()

#     # Suggest matching movies
#     if partial_movie and movies is not None:
#         matching_movies = movies[movies['title'].str.contains(partial_movie, case=False, na=False)]['title'].tolist()
#         if matching_movies:
#             user_movie = st.sidebar.selectbox("Select a Movie from the Matches", options=matching_movies)
#         else:
#             st.sidebar.warning("No matching movies found. Please refine your search.")
#             user_movie = None
#     else:
#         user_movie = None

#     # Display recommendations
#     if user_movie:
#         recommendations = get_recommendations(user_movie, cosine_sim, indices, titles)
#         if recommendations:
#             st.subheader(f"Recommendations for '{user_movie}':")
#             for i, movie in enumerate(recommendations, start=1):
#                 st.write(f"{i}. {movie}")
#         else:
#             st.subheader("No recommendations found. Please try another movie.")
# else:
#     st.warning("Please ensure both 'movies.csv' and 'rating.csv' files are available.")



# the third code we get
import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import os

# Load datasets
@st.cache_data
def load_data():
    try:
        # Update paths if necessary
        movies_path = 'movies.csv'
        ratings_path = 'ratings.csv'
        
        if not os.path.exists(movies_path):
            raise FileNotFoundError(f"File not found: {movies_path}")
        if not os.path.exists(ratings_path):
            raise FileNotFoundError(f"File not found: {ratings_path}")
        
        movies = pd.read_csv(movies_path)
        ratings = pd.read_csv(ratings_path)
        return movies, ratings
    except FileNotFoundError as e:
        st.error(str(e))
        return None, None

# Prepare data
@st.cache_resource
def prepare_data(movies, ratings):
    if movies is None or ratings is None:
        return None, None, None, None
    
    # Merge datasets
    df = pd.merge(ratings, movies, how='left', on='movieId')
    
    # Calculate cosine similarity matrix based on genres
    cv = TfidfVectorizer()
    tfidf_matrix = cv.fit_transform(movies['genres'])
    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
    
    # Create index for movie titles
    indices = pd.Series(movies.index, index=movies['title'])
    return df, cosine_sim, indices, movies['title']

# Recommendation function
def get_recommendations(title, cosine_sim, indices, titles):
    if indices is None or title not in indices:
        return []
    
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]  # Get top 10 recommendations
    movie_indices = [i[0] for i in sim_scores]
    return titles.iloc[movie_indices].tolist()

# Streamlit app
# Hero section
st.markdown(
    """
    <style>
    .hero {
        text-align: center;
        padding: 2rem;
        background-color: #f7c800;
        color: #1c1c1e;
        border-radius: 10px;
        margin-bottom: 1rem;
    }
    .hero h1 {
        font-size: 3rem;
        margin-bottom: 0.5rem;
    }
    .hero p {
        font-size: 1.2rem;
        color: #444;
    }
    .recommendations {
        background: #fff5cc;
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
    .recommendations h2 {
        color: #444;
    }
    .card {
        # background: #000;
        # border-radius: 8px;
        # padding: 1rem;
        # box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        # margin-bottom: 1rem;
        background: #d4edda; /* Light green background */
        color: #000; /* Dark green text for readability */
        border-radius: 8px; /* Smooth rounded corners */
        padding: 1rem; /* Padding inside the card */
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); /* Subtle shadow effect */
        margin-bottom: 1rem; /* Spacing between cards */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="hero">
        <h1>Welcome to Movie Buddy 🎥</h1>
        <p>Find movies you love and discover recommendations tailored to you!</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# Load data
movies, ratings = load_data()
if movies is not None and ratings is not None:
    df, cosine_sim, indices, titles = prepare_data(movies, ratings)

    # Sidebar for input
    st.sidebar.header("Enter a Movie Name")
    partial_movie = st.sidebar.text_input("Movie Name (or partial name)", "").strip()

    # Suggest matching movies
    if partial_movie and movies is not None:
        matching_movies = movies[movies['title'].str.contains(partial_movie, case=False, na=False)]['title'].tolist()
        if matching_movies:
            user_movie = st.sidebar.selectbox("Select a Movie from the Matches", options=matching_movies)
        else:
            st.sidebar.warning("No matching movies found. Please refine your search.")
            user_movie = None
    else:
        user_movie = None

    # Display recommendations
    if user_movie:
        recommendations = get_recommendations(user_movie, cosine_sim, indices, titles)
        if recommendations:
            st.markdown("<div class='recommendations'><h2>Recommendations</h2>", unsafe_allow_html=True)
            for movie in recommendations:
                st.markdown(f"<div class='card'><strong>{movie}</strong></div>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)
        else:
            st.subheader("No recommendations found. Please try another movie.")
else:
    st.warning("Please ensure both 'movies.csv' and 'rating.csv' files are available.")
