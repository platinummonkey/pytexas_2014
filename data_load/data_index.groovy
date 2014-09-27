mgmt = g.getManagementSystem()

// Setup Property Keys and Edge Labels

element_type = mgmt.makePropertyKey('element_type').dataType(String.class).make()
// movie keys
movie_id = mgmt.makePropertyKey('movie_id').dataType(Integer.class).make()
movie_title = mgmt.makePropertyKey('movie_title').dataType(String.class).make()

// genres
genre_genre = mgmt.makePropertyKey('genre_genre').dataType(String.class).make()
has_genre = mgmt.makeEdgeLabel('has_genre').make()

// users
user_id = mgmt.makePropertyKey('user_id').dataType(Integer.class).make()
user_gender = mgmt.makePropertyKey('user_gender').dataType(String.class).make()
user_age = mgmt.makePropertyKey('user_age').dataType(Integer.class).make()

// occupation
occupation_occupation = mgmt.makePropertyKey('occupation_occupation').dataType(String.class).make()
has_occupation = mgmt.makeEdgeLabel('has_occupation').make()

// ratings
rated = mgmt.makeEdgeLabel('rated').make()
stars = mgmt.makePropertyKey('stars').dataType(Integer.class).make()

//---- Build Indices
//-- Composite Indices
mgmt.buildIndex('byElementType', Vertex.class).addKey(element_type).buildCompositeIndex()

// movies
mgmt.buildIndex('byMovieId', Vertex.class).addKey(movie_id).unique().buildCompositeIndex()
mgmt.buildIndex('byMovieTitle', Vertex.class).addKey(movie_title).buildCompositeIndex()

// genres
mgmt.buildIndex('byGenreGenre', Vertex.class).addKey(genre_genre).buildCompositeIndex()

// users
mgmt.buildIndex('byUserId', Vertex.class).addKey(user_id).unique().buildCompositeIndex()
mgmt.buildIndex('byUserGender', Vertex.class).addKey(user_gender).buildCompositeIndex()
mgmt.buildIndex('byUserAge', Vertex.class).addKey(user_age).buildCompositeIndex()
mgmt.buildIndex('byGenderAndAge', Vertex.class).addKey(user_gender).addKey(user_age).buildCompositeIndex()

// occupation
mgmt.buildIndex('byOccupationOccupation', Vertex.class).addKey(occupation_occupation).buildCompositeIndex()

// ratings
mgmt.buildIndex('byStars', Edge.class).addKey(stars).buildCompositeIndex()

//-- Mixed Indices
// ratings
mgmt.buildEdgeIndex(rated, 'ratingByStars', Direction.BOTH, Order.DESC, stars)
// movie titles search
mgmt.buildIndex('byMovieTitleSearch', Vertex.class).addKey(movie_title).buildMixedIndex("search")

mgmt.commit()

g.commit()
