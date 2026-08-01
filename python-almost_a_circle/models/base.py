#!/usr/bin/python3
"""Module that defines the Base class."""
import json
import csv


class Base:
    """Base class to manage id attribute in all future classes."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base instance.

        Args:
            id: the id of the instance (int or None).
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of list_dictionaries."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to a file."""
        filename = "{}.json".format(cls.__name__)
        if list_objs is None:
            list_objs = []
        list_dicts = [obj.to_dictionary() for obj in list_objs]
        with open(filename, "w") as f:
            f.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Return the list represented by a JSON string."""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes already set."""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = cls()
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Return a list of instances loaded from <Class name>.json."""
        filename = "{}.json".format(cls.__name__)
        try:
            with open(filename, "r") as f:
                list_dicts = cls.from_json_string(f.read())
            return [cls.create(**d) for d in list_dicts]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serialize list_objs to a CSV file <Class name>.csv."""
        filename = "{}.csv".format(cls.__name__)
        if list_objs is None:
            list_objs = []
        with open(filename, "w", newline="") as f:
            writer = csv.writer(f)
            if cls.__name__ == "Rectangle":
                fields = ["id", "width", "height", "x", "y"]
            else:
                fields = ["id", "size", "x", "y"]
            for obj in list_objs:
                d = obj.to_dictionary()
                writer.writerow([d[key] for key in fields])

    @classmethod
    def load_from_file_csv(cls):
        """Deserialize instances from a CSV file <Class name>.csv."""
        filename = "{}.csv".format(cls.__name__)
        try:
            with open(filename, "r", newline="") as f:
                reader = csv.reader(f)
                if cls.__name__ == "Rectangle":
                    fields = ["id", "width", "height", "x", "y"]
                else:
                    fields = ["id", "size", "x", "y"]
                instances = []
                for row in reader:
                    d = {fields[i]: int(row[i]) for i in range(len(fields))}
                    instances.append(cls.create(**d))
            return instances
        except FileNotFoundError:
            return []
