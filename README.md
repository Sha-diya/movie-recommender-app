# Movie Recommendation System

## Overview
This is a content-based movie recommendation system built in Python. It suggests movies based on the similarity of their features, such as genres, keywords, and cast. By using natural language processing techniques and the cosine similarity measure, this system identifies the most similar movies to a given movie title.

## Features Used
The following columns from the dataset are used to create a single tag for each movie:
1. **Genres**
2. **ID**
3. **Keywords**
4. **Title**
5. **Overview**
6. **Cast**
7. **Crew**

These features are combined and processed to form a meaningful representation of each movie.

## How It Works
1. **Data Preprocessing:**
   - Extract the necessary columns and combine them into a single tag for each movie.
   - Clean the text data and remove any unnecessary information.

2. **Vectorization:**
   - Convert the combined text tags into numerical vectors using a technique like CountVectorizer.

3. **Similarity Matrix:**
   - Calculate the similarity between movies using the cosine similarity metric.

4. **Movie Recommendations:**
   - When a user inputs a movie title, the system searches for the most similar movies in the dataset.
   - It returns the top 5 most similar movies based on the calculated similarity scores.

## How to Use
1. Clone this repository.
2. Install the necessary libraries:
   ```bash
   pip install pandas numpy sklearn
   ```
3. Run the Python script:
   ```bash
   python movie_recommender.py
   ```
4. Enter the name of a movie when prompted.
5. Get a list of 5 recommended movies based on their similarity to the entered movie.

## Explore the App Here: https://huggingface.co/spaces/shadia112/movie-recommender-app

## Future Enhancements
- Include more advanced NLP techniques for better feature extraction.
- Use different similarity measures for comparison.
- Build a web interface for better user experience.

## Contributing
Feel free to fork this project and submit pull requests with any improvements or new features.

