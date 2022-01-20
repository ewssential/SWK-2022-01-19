import unittest
 
def solver(participants):
    zeitnehmer = list(filter(lambda x: x['zeitnehmer'] == True, participants))
    saaldiener = list(filter(lambda x: x['saaldiener'] == True, participants))
    if (len(zeitnehmer) == 0):
        return {
            'zeitnehmer': None,
            'saaldiener': saaldiener[0]['number']
            }

    if (len(saaldiener) == 0):
        return {
        'zeitnehmer': zeitnehmer[0]['number'],
        'saaldiener': None
            }

    return {
        'zeitnehmer': zeitnehmer[0]['number'],
        'saaldiener': saaldiener[0]['number']
        }

class TestStringMethods(unittest.TestCase):

    def test_solver(self):
        participants = [{
            'name': 'Eins',
            'number': 1,
            'zeitnehmer': True,
            'saaldiener': False
        }]
        result = solver(participants)
        self.assertIsNotNone(result)

    def test_minimal_zeitnehmer(self):
        participants = [{
            'name': 'Eins',
            'number': 1,
            'zeitnehmer': True,
            'saaldiener': False
        }]
        result = solver(participants)
        self.assertEqual(result['zeitnehmer'], 1)

    def test_two_zeitnehmer(self):
        participants = [{
            'name': 'Zwei',
            'number': 2,
            'zeitnehmer': True,
            'saaldiener': False
        },{
            'name': 'Eins',
            'number': 1,
            'zeitnehmer': True,
            'saaldiener': False
        }]
        result = solver(participants)
        self.assertEqual(result['zeitnehmer'], 2)

    def test_two_zeitnehmer_with_invalid_zeitnehmer(self):
        participants = [{
            'name': 'Zwei',
            'number': 2,
            'zeitnehmer': False,
            'saaldiener': False
        },{
            'name': 'Eins',
            'number': 1,
            'zeitnehmer': True,
            'saaldiener': False
        }]
        result = solver(participants)
        self.assertEqual(result['zeitnehmer'], 1)

    def test_just_one_saaldiener(self):
        participants = [{
            'name': 'Zwei',
            'number': 3,
            'zeitnehmer': False,
            'saaldiener': True
        },{
            'name': 'Eins',
            'number': 4,
            'zeitnehmer': True,
            'saaldiener': False
        }]
        result = solver(participants)
        self.assertEqual(result['saaldiener'], 3)

    def test_just_one_saaldiener(self):
        participants = [{
            'name': 'Zwei',
            'number': 3,
            'zeitnehmer': True,
            'saaldiener': False
        },{
            'name': 'Eins',
            'number': 4,
            'zeitnehmer': True,
            'saaldiener': True
        }]
        result = solver(participants)
        self.assertEqual(result['saaldiener'], 4)

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
