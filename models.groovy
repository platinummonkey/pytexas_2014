
def obj_count(element_type) {
    return g.V.has('element_type', element_type)  // Filter by `element_type` vertices
              .count()                            // Count them!
}

def occupation_distribution(element_type) {
    def m = [:]
    g.V.has('element_type', element_type)                // Filter Users first
       .out('has_occupation')                            // Find Occupation Edges
       .groupCount(m).iterate()                          // Group unique vertices and count
    return m.sort{a, b -> b.value <=> a.value}[0..4]     // Sort by group count and return top N
}

def user_mean_age(element_type) {
    return g.V('element_type', element_type)  // Filter by Users
            .user_age                         // We only care about their age
            .mean()                           // Find the mean over all the User vertices
}

def users_given_movie_with_rating_above(id, stars, limit) {
    def v = g.v(id)                                      // Get the Movie
    return v.inE('rated')                                // Using a vertex centric query, find ratings
            .filter{ it.getProperty('stars') > stars }   // Filter to find ratings above criterion
            .outV[0..limit-1]                              // Return Users and return first N
}

def movies_with_user_ratings_above(id, stars, limit) {
    def v = g.v(id)                                      // Get the Movie
    return v.inE('rated')                                // Using a vertex centric query, find ratings
            .filter{ it.getProperty('stars') > stars }   // Filter to find ratings above criterion
            .outV.outE('rated')                          // Find other movie's ratings
            .filter{ it.getProperty('stars') > stars }   // Repeat filter to find ratings above criterion
            .inV                                         // Get the Movie associated
            .dedup[0..limit-1]                             // Deduplicate the Movie results and return top N
}

def corated_movie_from_movie(id, stars, limit) {
    def v = g.v(id)                                                // Get the Movie
    def m = [:]                                                    // Initialize Empty HashMap
    def r = [:]
    v.inE('rated')                                                 // Using a vertex centric query, find ratings
      .filter{ it.getProperty('stars') > stars }                   // Filter to find ratings above criterion
      .outV.outE('rated')                                          // Find other movie's ratings
      .filter{ it.getProperty('stars') > stars }                   // Repeat filter to find ratings above criterion
      .inV                                                         // Get the Movie associated
      .filter{ it != v }                                           // Don't allow the original Movie to show up
      .groupCount(m).iterate()                                     // Group by unique Movie and count
    return m.sort{a, b -> b.value <=> a.value}.take(limit.toInteger())   // Sort by group count and return top N
}

def corated_movie_by_genre(id, stars, limit) {
    def v = g.v(id)                                       // Get the Movie
    def m = [:]                                           // Initialize Empty HashMap
    def x = [] as Set                                     // Initialize empty Set
    v.out('has_genre')                                    // Using a vertex centric query, find genres
     .aggregate(x)                                        // Add genres to Set for reference
     .back(2)                                             // Go back 2 steps to the original Movie
     .inE('rated')                                        // Using a vertex centric query, find ratings
     .filter{ it.getProperty('stars') > stars }           // Filter to find ratings above criterion
     .outV.outE('rated')                                  // Find other movie's ratings
     .filter{ it.getProperty('stars') > stars }           // Repeat filter to find ratings above criterion
     .inV                                                 // Get the Movie associated
     .filter{ it != v }                                   // Don't allow the original Movie to show up
     .out('has_genre')                                    // Find Genres associated
     .retain(x)                                           // Only allow what was in the stored Set to pass validation (filter out movies without the genre in question)
     .back(2)                                             // Go Back 2 steps
     .groupCount(m).iterate()                             // Group by unique Movie and count
    return m.sort{a, b -> b.value <=> a.value}.take(limit.toInteger())   // Sort by group count and return top N
}

def corated_movie_by_genre_has_all(id, stars, limit) {
    def v = g.v(id)
    def m = [:]
    def x = [] as Set
    v.out('has_genre')
     .aggregate(x)
     .back(2)
     .inE('rated')
     .filter{ it.getProperty('stars') > stars }
     .outV.outE('rated')
     .filter{ it.getProperty('stars') > stars}
     .inV
     .filter{ it != v}
     .filter{ it.out('has_genre').toList() as Set == x}
     .groupCount(m).iterate()
    return m.sort{a, b -> b.value <=> a.value}.take(limit.toInteger())   // Sort by group count and return top N
}

