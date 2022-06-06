"""
This example module shows various types of documentation available for use
with pydoc.  To generate HTML documentation for this module issue the
command:

    - source venv/bin/activate
    - cd doc
    - make html

"""
class House:
    """
    House encapsulates a name and an age.
    """
    def __init__(self, name, age):
        """
        Construct a new House object.

        :param name: The name of this house
        :param age: The age of this house
        :return: returns nothing
        """
        self.name = name
        self.age = age

    @property
    def name_upper(self):
        """
        Returns the uppercase name of the house
        """
        return self.name.upper

    @property
    def is_new(self):
        """
        Determines whether the house is new or old
        """
        if self.age < 10:
            return True
        if self.age > 20:
            return False
        if self.age > 30:
            return False
        if self.age > 40:
            return False
        if self.age > 50:
            return False
        if self.age > 60:
            return False
        return False


if __name__ == '__main__':
    h = House('Casa del koen', -1)
