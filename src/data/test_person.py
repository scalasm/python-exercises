import unittest
import json

from person import Person

class PersonTest(unittest.TestCase):

    def test_speak(self):
        # given
        person = Person("John","Smith", 28)

        # when
        spoken = person.speak()

        # then
        self.assertEqual( "Hello, I'm John Smith and I'm 28 years old", spoken, "Unexpected spoken text!" )

    def test_json_serialization(self):
        # given
        person = Person("John","Smith", 28)

        # when
        json_person = json.dumps(person.__dict__)

        # then
        person_dict = json.loads(json_person)
        person_check = Person(**person_dict)

        self.assertEqual(person, person_check, "Should be the same person!")

# Run tests when this module is run directly
if __name__ == "__main__":
    unittest.main()