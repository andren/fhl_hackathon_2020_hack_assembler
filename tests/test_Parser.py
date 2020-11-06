# import unittest
# from hack_assembler.parser import Parser
# from pathlib import Path
# from hack_assembler.hack_command_factory import hack_command_factory, HackCommandType

# res = Path("tests/resources")

# class TestParser(unittest.TestCase):

#     def test_init_invalidFile(self):
#         with self.assertRaises(Exception):
#             Parser(res/"notAsm.txt")

#     def test_init_nonExistingFile(self):
#         with self.assertRaises(OSError):
#             Parser(res/"nonExisting.asm")

#     def test_init_validFile_Empty(self):
#         expected_commandList = []

#         p = Parser(res/"empty/empty.asm")
#         actual_commandList = p.commandList

#         self.assertListEqual(expected_commandList, actual_commandList)

#     def test_init_validFile_Add(self):
#         expected_commandList = [hack_command_factory('@2'), hack_command_factory('D=A'), hack_command_factory('@3'), hack_command_factory('D=D+A'),
#                                 hack_command_factory('@0'), hack_command_factory('M=D')]

#         p = Parser(res/"add/Add.asm")
#         actual_commandList = p.commandList

#         self.assertListEqual(expected_commandList, actual_commandList)
    
#     def test_init_validFile_Max(self):
#         expected_commandList = [hack_command_factory('@R0'), hack_command_factory('D=M'), hack_command_factory('@R1'), hack_command_factory('D=D-M'),
#                                 hack_command_factory('@OUTPUT_FIRST'), hack_command_factory('D;JGT'), hack_command_factory('@R1'), hack_command_factory('D=M'),
#                                 hack_command_factory('@OUTPUT_D'), hack_command_factory('0;JMP'), hack_command_factory('(OUTPUT_FIRST)'), hack_command_factory('@R0'),
#                                 hack_command_factory('D=M'), hack_command_factory('(OUTPUT_D)'), hack_command_factory('@R2'), hack_command_factory('M=D'),
#                                 hack_command_factory('(INFINITE_LOOP)'), hack_command_factory('@INFINITE_LOOP'), hack_command_factory('0;JMP')]

#         p = Parser(res/"max/Max.asm")
#         actual_commandList = p.commandList

#         self.assertListEqual(expected_commandList, actual_commandList)
        
# if __name__ == '__main__':
#     unittest.main()