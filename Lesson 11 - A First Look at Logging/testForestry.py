import unittest

from forestry import Lumberjack, Tree, startLogging

sizes = (("S", 1), ("M", 2), ("L", 3), ("XL", 4), ("XXL", 5))

class TestTree(unittest.TestCase):
    
    def testLumber(self):
        for code, boards in sizes:
            tree = Tree(code)
            self.assertEqual(boards, tree.getBoards())
            
    def testString(self):
        tree = Tree("L")
        self.assertEqual(str(tree), "Tree: Size L")
        
    def testExceptions(self):
        self.assertRaises(ValueError, Tree, "parrot")
        self.assertRaises(TypeError, Lumberjack().cutDownTree)
        
class TestLumberjack(unittest.TestCase):
    
    def testLumberjack(self):
        for code, boards in sizes:
            tree = Tree(code)
            graham = Lumberjack()
            self.assertIsNone(graham.tree)
            graham.tree = tree
            brds = graham.cutDownTree()
            self.assertIsNone(graham.tree)
            self.assertEqual(boards, brds)


if __name__ == "__main__":
    startLogging(level = "info")
    unittest.main()
    