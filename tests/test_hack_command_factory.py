import unittest
from hack_assembler.hack_command_factory import hack_command_factory, HackCommandType
from pathlib import Path

res = Path("tests/resources")

invalid_cmd_list = ["",
                    "    ",
                    "@@",
                    "&s80d12m&&",
                    "D;LOL",
                    "//just a comment"]

valid_acmd_list = ["@123",
                   " @LABEL",
                   "    @91829182",
                   "		@LaBeL2 //@label comment"
                   "@test		// M=D"]

valid_ccmd_list = ["D=M",
                   " D=D-M  // D = first",
                   "		D;JGT//D=M",
                   "D;JEQ"]

valid_lcmd_list = ["(label)",
                   " (LaBeL2)   // label",
                   "		(1)//(comment)"
                   "(2)		// M=D"]

class TestHackCommand(unittest.TestCase):

    def test_invalid_command(self):
        with self.assertRaises(ValueError):
            for cmd in invalid_cmd_list:
                hack_command_factory(cmd)
    
    def test_valid_acommand(self):
        expected_raw_list = ["@123", "@LABEL", "@91829182", "@LaBeL2", "@test"]

        for i in range(len(valid_acmd_list)):
            actual_hc = hack_command_factory(valid_acmd_list[i])
            self.assertEquals(actual_hc.cmdType, HackCommandType.A_COMMAND)
            self.assertEquals(actual_hc.raw, expected_raw_list[i])
    
    def test_valid_ccommand(self):
        expected_raw_list = ["D=M", "D=D-M", "D;JGT", "D;JEQ"]
        expected_dest_list = ["D", "D", "null", "null"]
        expected_comp_list = ["M", "D-M", "D", "D"]
        expected_jump_list = ["null", "null", "JGT", "JEQ"]

        for i in range(len(valid_ccmd_list)):
            actual_hc = hack_command_factory(valid_ccmd_list[i])
            self.assertEquals(actual_hc.cmdType, HackCommandType.C_COMMAND)
            self.assertEquals(actual_hc.raw, expected_raw_list[i])
            self.assertEquals(actual_hc.dest, expected_dest_list[i])
            self.assertEquals(actual_hc.jump, expected_jump_list[i])
            self.assertEquals(actual_hc.comp, expected_comp_list[i])
                
    def test_valid_lcommand(self):
        expected_raw_list = ["(label)", "(LaBeL2)", "(1)", "(2)"]

        for i in range(len(valid_lcmd_list)):
            actual_hc = hack_command_factory(valid_lcmd_list[i])
            self.assertEquals(actual_hc.cmdType, HackCommandType.L_COMMAND)
            self.assertEquals(actual_hc.raw, expected_raw_list[i])
        
if __name__ == '__main__':
    unittest.main()