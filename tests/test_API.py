import unittest

import libs.API as API


class TestAPI(unittest.TestCase):

    def testGetProductFromBarcode(self):
        APIs = API.APIs()
        print(APIs.getProductFromBarcode('04820226161677'))
        # print(APIs.getProductFromBarcode('5900552058601'))
