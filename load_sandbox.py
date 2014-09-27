from rexpro import RexProConnection

script = '''mgmt = g.getManagementSystem()

// Setup Property Keys and Edge Labels

element_type = mgmt.makePropertyKey('element_type').dataType(String.class).make()


//---Basic intro
//--MyVertex test keys
myvertex_name = mgmt.makePropertyKey('myvertex_name').dataType(String.class).make()
myvertex_test_val = mgmt.makePropertyKey('myvertex_val').dataType(Integer.class).make()
myvertex_test_date = mgmt.makePropertyKey('myvertex_date').dataType(Long.class).make()

//--MyEdge test keys
myedge_name = mgmt.makePropertyKey('myedge_name').dataType(String.class).make()
myedge_test_val = mgmt.makePropertyKey('myedge_val').dataType(Integer.class).make()
myedge_test_date = mgmt.makePropertyKey('myedge_date').dataType(Long.class).make()

//---Belongings Example
//--Person
person_name = mgmt.makePropertyKey('person_name').dataType(String.class).make()
person_email = mgmt.makePropertyKey('person_email').dataType(String.class).make()

//--Trinket
trinket_name = mgmt.makePropertyKey('trinket_name').dataType(String.class).make()
trinket_engraving = mgmt.makePropertyKey('trinket_engraving').dataType(String.class).make()

//--Owns Edge
ownsobject_since = mgmt.makePropertyKey('ownsobject_since').dataType(Long.class).make()

//--IsFriendsWith Edge
isfriendswith_since = mgmt.makePropertyKey('isfriendswith_since').dataType(Long.class).make()


//---- Build Indices
//-- Composite Indices
mgmt.buildIndex('byElementType', Vertex.class).addKey(element_type).buildCompositeIndex()

//-MyVertex
mgmt.buildIndex('byMyVertexName', Vertex.class).addKey(myvertex_name).buildCompositeIndex()
mgmt.buildIndex('byMyVertexTestVal', Vertex.class).addKey(myvertex_test_val).buildCompositeIndex()
mgmt.buildIndex('byMyVertexTestDate', Vertex.class).addKey(myvertex_test_date).buildCompositeIndex()

//-MyEdge
mgmt.buildIndex('byMyEdgeName', Edge.class).addKey(myedge_name).buildCompositeIndex()
mgmt.buildIndex('byMyEdgeTestVal', Edge.class).addKey(myedge_test_val).buildCompositeIndex()
mgmt.buildIndex('byMyEdgeTestDate', Edge.class).addKey(myedge_test_date).buildCompositeIndex()

//-Person
mgmt.buildIndex('byPersonName', Vertex.class).addKey(person_name).buildCompositeIndex()
mgmt.buildIndex('byPersonEmail', Vertex.class).addKey(person_email).unique().buildCompositeIndex()

//-Trinket
mgmt.buildIndex('byTrinketName', Vertex.class).addKey(trinket_name).buildCompositeIndex()
mgmt.buildIndex('byTrinketEngraving', Vertex.class).addKey(trinket_engraving).buildCompositeIndex()

//-Owns Edge
mgmt.buildIndex('byOwnsObjectSince', Edge.class).addKey(ownsobject_since).buildCompositeIndex()

//-IsFriendsWith Edge
mgmt.buildIndex('byIsFriendsWithSince', Edge.class).addKey(isfriendswith_since).buildCompositeIndex()


mgmt.commit()

g.commit()
'''

conn = RexProConnection('localhost', 8184, 'sandbox')
conn.execute(script, {})