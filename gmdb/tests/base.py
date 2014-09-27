from mogwai.connection import setup
from unittest import TestCase


class BaseTestCase(TestCase):

    @classmethod
    def setUpClass(cls):
        super(BaseTestCase, cls).setUpClass()
        setup('localhost', concurrency='eventlet')

