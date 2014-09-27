{% extends "base.tpl" %}

{% block title %} - About{% endblock %}

{% block content %}
<h2>About GMDB</h2>

<p>GMDB is a fake graph database, and illustrates using <a href="http://mogwai.readthedocs.org/">mogwai</a> an
    Object Graph Mapper for Python
</p>
<p> To install:
<code>
    pip install mogwai  # optional install with mogwai[eventlet] or mogwai[gevent] for eventlet/gevent concurrency support
</code>
</p>
<p> To connect to the database:
<code>
    from mogwai.connection import setup
    setup()
</code>
</p>
{% endblock %}