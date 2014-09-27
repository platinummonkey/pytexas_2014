// user ratings
i = 1
new File(path + '/ratings.dat').eachLine {def line ->
    def components = line.split('::');
    def ratedEdge = g.addEdge(g.V.has('user_id', components[0].toInteger()).next(), g.V.has('movie_id', components[1].toInteger()).next(), 'rated');
    ratedEdge.setProperty('stars', components[2].toInteger());
    i = i + 1
    if ( i % 3000 ) { g.commit(); i = 1 }
}
g.commit()
