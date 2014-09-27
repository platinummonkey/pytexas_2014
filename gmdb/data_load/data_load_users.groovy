// setup occupation map
occupations = [0:'other', 1:'academic/educator', 2:'artist',
    3:'clerical/admin', 4:'college/grad student', 5:'customer service',
    6:'doctor/health care', 7:'executive/managerial', 8:'farmer',
    9:'homemaker', 10:'K-12 student', 11:'lawyer', 12:'programmer',
    13:'retired', 14:'sales/marketing', 15:'scientist', 16:'self-employed',
    17:'technician/engineer', 18:'tradesman/craftsman', 19:'unemployed', 20:'writer']


// load users
new File(path + '/users.dat').eachLine {def line ->
    def components = line.split('::');
    def userVertex = g.addVertex(['element_type': 'user', 'user_id': components[0].toInteger(), 'user_gender': components[1], 'user_age': components[2].toInteger()]);
    def occupation = occupations[components[3].toInteger()];
    def hits = g.V.has('occupation_occupation', occupation);
    def occupationVertex = hits.hasNext() ? hits.next() : g.addVertex(['element_type':'occupation', 'occupation_occupation': occupation]);
    g.addEdge(userVertex, occupationVertex, 'has_occupation');
}

g.commit()
