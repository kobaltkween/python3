"""
Test the animalFarm animals
"""
import unittest
from animalFarm import Animal, Pig, Dog, Chicken

class Test(unittest.TestCase):
    
    def testBaseAnimalClass(self):
        "Tests the basics of the Animal class."
        animal  = Animal("Orwell")
        self.assertRaises(NotImplementedError, animal.sound)
        self.assertFalse(animal.hasWings())
        
    def testPig(self):
        "Tests the inhabitants of the farm"
        pig = Pig("Napoleon")
        self.assertEqual(pig.sound(), "oink!")
        self.assertFalse(pig.hasWings())
        
    def testDog(self):
        dog = Dog("Bluebell")
        self.assertEqual(dog.sound(), "woof!")
        self.assertFalse(dog.hasWings())
        
    def testChicken(self):
        chicken = Chicken("Kulak")
        self.assertEqual(chicken.sound(), "bok bok!")
        self.assertTrue(chicken.hasWings())
        
if __name__ == "__main__":
    unittest.main()