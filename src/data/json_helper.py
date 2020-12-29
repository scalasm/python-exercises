import json
from typing import Any, Final

EMPTY_JSON: Final = "{}"

class JsonHelper(object):
    @staticmethod
    def to_jsons(instance: Any) -> str:
        """Returns a JSON representation of the given instance"""
        if instance != None:
            return json.dumps(instance.__dict__)
        else:
            return EMPTY_JSON

    @staticmethod
    def to_instance(json_string: str, wanted_type ) -> Any:
        """Returns an Python object of a wanted type for the given JSON string"""
        json_object = json.loads( json_string )

        instance = wanted_type(**json_object)

        return instance
