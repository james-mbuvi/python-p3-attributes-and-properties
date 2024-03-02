
# class Dog:
#     APPROVED_BREEDS = [
#         "Mastiff",
#         "Chihuahua",
#         "Corgi",
#         "Shar Pei",
#         "Beagle",
#         "French Bulldog",
#         "Pug",
#         "Pointer"
#     ]

#     def __init__(self, name="Dog", breed="Unknown"):
#         self.name = name
#         self.breed = breed

#     @property
#     def name(self):
#         return self._name

#     @name.setter
#     def name(self, value):
#         if not isinstance(value, str) or not (1 <= len(value) <= 25):
#             raise ValueError("Name must be a string between 1 and 25 characters.")
#         else:
#             self._name = value

#     @property
#     def breed(self):
#         return self._breed

#     @breed.setter
#     def breed(self, value):
#         if value not in self.APPROVED_BREEDS:
#             raise ValueError("Breed must be in list of approved breeds.")
#         else:
#             self._breed = value

#             pass








APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]


class Dog:
    def __init__(self, name='Fido', breed='Mastiff'):
        self.name = name
        self.breed = breed

    def get_name(self):
        return self._name

    def set_name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 25:
            self._name = name.title()
        else:
            raise ValueError(
                "Name must be string between 1 and 25 characters.")

    name = property(get_name, set_name)

    def get_breed(self):
        return self._breed

    def set_breed(self, breed):
        if breed in APPROVED_BREEDS:
            self._breed = breed
        else:
            raise ValueError("Breed must be in list of approved breeds.")

    breed = property(get_breed, set_breed)























