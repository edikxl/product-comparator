import unittest

from tests.testlibs import Case, errorTest
from libs.db import FileDS, Serializer, JSONEncoder, ProductNormalizer, DataBase

class TestDB(unittest.TestCase):
  def testDataBase(self):
    fds = FileDS('tests/test_db.json', Serializer(JSONEncoder(), ProductNormalizer()))
    db = DataBase(fds)

    db.load()
    """
    cases = [
      Case(True, {'day': 30}, dict),
      Case(True, '1', str),
      Case(False, {'day': 30}, list),
      Case(False, '1', int)
    ]

    errorTest(self, Validator.type, cases, TypeError)
    """