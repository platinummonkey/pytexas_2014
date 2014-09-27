from rexpro import RexProConnection
import os

cwd = os.path.dirname(os.path.realpath(__file__))

script = open(os.path.join(cwd, 'data_load_ratings.groovy'), 'r').read()
conn = RexProConnection('localhost', 8184, 'graph')
conn.execute(script, {'path': cwd})
