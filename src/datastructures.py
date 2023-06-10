
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint
import random

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = [
        
            {

                "id": self._generateId(),
                "first_name": "John",
                "last_name": last_name,
                "age": "33",
                "lucky_numbers": [7, 13, 22]
            },
            {
                "id": self._generateId(),
                "first_name": "Jane",
                "last_name": last_name,
                "age": "35",
                "lucky_numbers": [10, 14, 3]
            },
            {
                "id": self._generateId(),
                "first_name": "Jimmy",
                "last_name": last_name,
                "age": "5",
                "lucky_numbers": [1]
            }
        
        ]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        names = ["Alejandro", "José", "Pedro", "Sara", "María", "Judith"]

        # fill this method and update the return
        def randomName(name):
            random_name = random.choice(name)
            return random_name
        
        def random_age():
            randomAge = randint(1, 130)
            return randomAge
        
        def random_lucky_number():
            luckyNumber1 = randint(1, 99)
            luckyNumber2 = randint(1, 99)
            luckyNumber3 = randint(1, 99)

            luckyNumber = [luckyNumber1, luckyNumber2, luckyNumber3]

            return luckyNumber
        
        lucky_number = random_lucky_number()
        
        random_age = random_age()
        
        random_member = randomName(names)

        newMember = {
            "id": self._generateId(),
            "first_name": random_member,
            "last_name": self.last_name,
            "age": random_age,
            "lucky_numbers": lucky_number,
        }

        self._members.append(newMember)

        return newMember

    def delete_member(self, id):
        # fill this method and update the return
        pass

    def get_member(self, id):
        # fill this method and update the return
        data = request.json
        memberID = self._members.filter_by(memberID = id)
        pass

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
