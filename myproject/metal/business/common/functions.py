import json


class Functions:

    def convert_json_string_to_dict(self, array_obj):

        if(array_obj is None): return None

        return json.loads(array_obj)