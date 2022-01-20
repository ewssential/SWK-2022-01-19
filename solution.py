import unittest
 
def solver(participants):
    return participants

class TestStringMethods(unittest.TestCase):

    def test_solver(self):
        participants = {}
        result = solver(participants)
        self.assertIsNotNone(result)

if __name__ == '__main__':
    unittest.main()



## Ablauf
# csv einlesen
# optimierung
    # -> participant --> rollenzuordnung
# ausgabe
