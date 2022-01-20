import unittest
 
def solver(participants):
    return participants

class TestStringMethods(unittest.TestCase):

    def test_solver(self):
        participants = {}
        result = solver(participants)
        self.assertIsNotNone(result)

    def test_minimal_set(self):
        participants = {
            {}
        }

if __name__ == '__main__':
    unittest.main()



## Ablauf
# csv einlesen
    # -> csv --> participants
# preprocessing
    # -> participants --> reduced participants (hard kernel)
# optimierung (solver)
    # -> reduced participants --> rollenzuordnung
# ausgabe
    # -> rollenzuordnung --> Ausgabe
