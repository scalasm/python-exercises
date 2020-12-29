import unittest
from json_helper import JsonHelper, EMPTY_JSON

from person import Person

class PersonTest(unittest.TestCase):

    def test_json_serialization(self):
        # given
        person = Person("John","Smith", 28)

        # when
        json_string = JsonHelper.to_jsons(person)

        # then
        person_check = JsonHelper.to_instance(json_string, Person)

        self.assertEqual(person, person_check, "Should be the same person!")

    def test_json_serialization_null_instance(self):
        # given
        person = None

        # when
        json_string = JsonHelper.to_jsons(person)

        # then
        self.assertEqual( EMPTY_JSON, json_string, "None should be mapped to `\{\} (empty JSON)" )

    def test_empty_json_serialization_deserialization_fails(self):
        """It is an error to try deserializing an empty JSON back to an object that needs construction-time parameters"""
        # given
        json_string = EMPTY_JSON

        # when

        # then
#        self.assertRaises( TypeError, JsonHelper.to_instance, json_string, Person )
        with self.assertRaises(TypeError, msg="Person should not be instantiable with empty JSON!"):
            JsonHelper.to_instance(json_string, Person)


# Run tests when this module is run directly
if __name__ == "__main__":
    unittest.main()