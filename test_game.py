""" Game Test Setup """
import unittest
import tests.test_solver

def suite():
    """ Run tests cmd: $ python test_game.py """
    s = unittest.TestSuite()
    s.addTest(unittest.makeSuite(tests.test_solver.TestGameGridSolver))
    return s

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
