import spacy
from sklearn.metrics.pairwise import cosine_similarity
def read_movies_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return [line.strip() for line in file.readlines()]
    
def get_similarity(description1, description2, nlp):
    doc1 = nlp(description1)
    doc2 = nlp(description2)
    return cosine_similarity(doc1.vector.reshape(1, -1), doc2.vector.reshape(1, -1))[0][0]

def recommend_movie(user_description, movie_descriptions):
    nlp = spacy.load('en_core_web_md')
    similarities = [(movie, get_similarity(user_description, movie, nlp)) for movie in movie_descriptions]
    similarities.sort(key=lambda x: x[1], reverse=True)
    return similarities[1][0]  # Excluding the first movie (user input)

if __name__ == "__main__":
    movie_descriptions = read_movies_file("movies.txt")
    user_description = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."
    recommended_movie = recommend_movie(user_description, movie_descriptions)
    print("Recommended movie:", recommended_movie)
