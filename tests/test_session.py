# -*- coding: utf-8 -*-
import unittest
from scuec_auth.session import Session, SessionCache

class TestSession(unittest.TestCase):
    def test_session(self):
        sc = SessionCache(5)
        sc.add('2021', Session())
        print(sc)
        s = sc.get_session('2021')
        print(s)
        sc.remove('2021')
        print(sc)

if __name__ == '__main__':
    unittest.main()
