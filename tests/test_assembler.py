import unittest
import filecmp
import os

from hack_assembler import assembler
from pathlib import Path

res = Path("tests/resources")

class TestAssembler(unittest.TestCase):

    def test_invalidFile(self):
        with self.assertRaises(Exception):
            assembler.assemble_file(res/"notAsm.txt")

    def test_nonExistingFile(self):
        with self.assertRaises(OSError):
            assembler.assemble_file(res/"nonExisting.asm")

    def test_validFile_Empty(self):     # TODO - names in these tests could be auto-fetched or something similar
        expected_hack_fpath = res/"empty/expected/Empty.hack"

        assembler.assemble_file(res/"empty/Empty.asm")
        actual_hack_fpath = res/"empty/Empty.hack"

        try:
            self.assertTrue(filecmp.cmp(expected_hack_fpath, actual_hack_fpath))
        finally:
            os.remove(actual_hack_fpath)
    
    def test_validFile_Add(self):
        expected_hack_fpath = res/"add/expected/Add.hack"

        assembler.assemble_file(res/"add/Add.asm")
        actual_hack_fpath = res/"add/Add.hack"

        try:
            self.assertTrue(filecmp.cmp(expected_hack_fpath, actual_hack_fpath))
        finally:
            os.remove(actual_hack_fpath)
    
    def test_validFile_MaxL(self):
        expected_hack_fpath = res/"max/expected/MaxL.hack"

        assembler.assemble_file(res/"max/MaxL.asm")
        actual_hack_fpath = res/"max/MaxL.hack"

        try:
            self.assertTrue(filecmp.cmp(expected_hack_fpath, actual_hack_fpath))
        finally:
            os.remove(actual_hack_fpath)

    def test_validFile_PongL(self):
        expected_hack_fpath = res/"pong/expected/PongL.hack"

        assembler.assemble_file(res/"pong/PongL.asm")
        actual_hack_fpath = res/"pong/PongL.hack"

        try:
            self.assertTrue(filecmp.cmp(expected_hack_fpath, actual_hack_fpath))
        finally:
            os.remove(actual_hack_fpath)
    
    def test_validFile_RectL(self):
        expected_hack_fpath = res/"rect/expected/RectL.hack"

        assembler.assemble_file(res/"rect/RectL.asm")
        actual_hack_fpath = res/"rect/RectL.hack"

        try:
            self.assertTrue(filecmp.cmp(expected_hack_fpath, actual_hack_fpath))
        finally:
            os.remove(actual_hack_fpath)

if __name__ == '__main__':
    unittest.main()