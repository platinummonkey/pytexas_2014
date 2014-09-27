#!/bin/bash

echo "Setting up indexes..."
python data_index.py

echo "Setting up Movies..."
python data_load_movies.py

echo "Setting up Users..."
python data_load_users.py

echo "Setting up Ratings..."
python data_load_ratings.py

echo "Done"
