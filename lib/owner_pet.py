class Pet:    
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"] 
    all = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type.lower() not in self.PET_TYPES:
            raise Exception("Error")

        self.name = name
        self.owner = owner
        self.pet_type = pet_type

        Pet.all.append(self)


class Owner:
    def __init__(self, name):
        self.name = name
    
    def pets(self):
        return [pet for pet in Pet.all if pet.owner.name == self.name]
        #Returns a full list of the owner's pets 
    
    def add_pet(self, pet): 
        if not isinstance(pet, Pet): 
            raise Exception("Error")
        pet.owner = self 

    def get_sorted_pets(self):
        owner_pets = self.pets() 
        return sorted(owner_pets, key=lambda pet: pet.name)
        #Returns sorted list of pets by their names 
    

