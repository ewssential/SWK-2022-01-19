import unittest
 
def solver(participants):
    return {'zeitnehmer': 1}

class TestStringMethods(unittest.TestCase):

    def test_solver(self):
        participants = {}
        result = solver(participants)
        self.assertIsNotNone(result)

    def test_minimal_zeitnehmer(self):
        participants = [{
            'name': 'Eins',
            'number': 1,
            'zeitnehmer': True
        }]
        result = solver(participants)
        self.assertEqual(result['zeitnehmer'], 1)

    def test_two_zeitnehmer(self):
        participants = [{
            'name': 'Eins',
            'number': 1,
            'zeitnehmer': True
        },{
            'name': 'Zwei',
            'number': 2,
            'zeitnehmer': True
        }]
        result = solver(participants)
        self.assertEqual(result['zeitnehmer'], 1)

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
