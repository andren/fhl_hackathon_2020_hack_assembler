import unittest
import hack_assembler.code

valid_comp_mne = ["0",
                  "1",
                  "-1",
                  "D",
                  "A",
                  "!D",
                  "!A",
                  "-D",
                  "-A",
                  "D+1",
                  "A+1",
                  "D-1",
                  "A-1",
                  "D+A",
                  "D-A",
                  "A-D",
                  "D&A",
                  "D|A",
                  "M",
                  "!M",
                  "-M",
                  "M+1",
                  "M-1",
                  "D+M",
                  "D-M",
                  "M-D",
                  "D&M",
                  "D|M"]

valid_jump_mne = ["null",
                  "JGT",
                  "JEQ",
                  "JGE",
                  "JLT",
                  "JNE",
                  "JLE",
                  "JMP"]

valid_dest_mne = ["null",
                  "M",
                  "D",
                  "MD",
                  "A",
                  "AM",
                  "AD",
                  "AMD"]

class TestParser(unittest.TestCase):

    def test_invalid_mnemonic(self):
        with self.assertRaises(KeyError):
            hack_assembler.code.dest("-invalid-")
        with self.assertRaises(KeyError):
            hack_assembler.code.comp("-invalid-")
        with self.assertRaises(KeyError):
            hack_assembler.code.jump("-invalid-")
        
    def test_valid_dest(self):
        expected_dest_bin = ["000","001","010","011","100","101","110","111"]

        actual_dest_bin = []
        for mne in valid_dest_mne:
            actual_dest_bin.append(hack_assembler.code.dest(mne))

        self.assertListEqual(expected_dest_bin, actual_dest_bin)

    def test_valid_comp(self):
        expected_comp_bin = ["0101010","0111111","0111010","0001100","0110000","0001111",
                             "0110011","0001111","0110011","0011111","0110111","0001110",
                             "0110010","0000010","0010011","0000111","0000000","0010101",
                             "1110000","1110001","1110011","1110111","1110010","1000010",
                             "1010011","1000111","1000000","1010101",]

        actual_comp_bin = []
        for mne in valid_comp_mne:
            actual_comp_bin.append(hack_assembler.code.comp(mne))

        self.assertListEqual(expected_comp_bin, actual_comp_bin)

    def test_valid_jump(self):
        expected_jump_bin = ["000","001","010","011","100","101","110","111"]

        actual_jump_bin = []
        for mne in valid_jump_mne:
            actual_jump_bin.append(hack_assembler.code.jump(mne))

        self.assertListEqual(expected_jump_bin, actual_jump_bin)

if __name__ == '__main__':
    unittest.main()