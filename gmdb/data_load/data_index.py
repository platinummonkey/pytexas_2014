from rexpro import RexProConnection

conn = RexProConnection('localhost', 8184, 'graph')

script = open('data_index.groovy', 'r').read()

conn.execute(script, {})
