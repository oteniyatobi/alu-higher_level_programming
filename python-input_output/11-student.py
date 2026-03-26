def reload_from_json(self, json):
    """Replace attributes from dictionary"""
    for key, value in json.items():
        setattr(self, key, value)
