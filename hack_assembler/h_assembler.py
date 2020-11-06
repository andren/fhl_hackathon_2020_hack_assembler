#from hack_assembler.parser import Parser
import h_parser as h_parser
#from hack_assembler.code import comp, dest, jump
import h_code as h_code
#from hack_assembler.hack_command_factory import HackCommandType, HackCommand
import h_command_factory as hc_fac
from pathlib import Path
import os

def assemble_file(asm_file_path: Path):
    
    # Get file name, directory and extension
        # asm_file_path: 'WindowsPath('tests/resources/empty/empty.asm')'
        # file_ext:      '.asm'
        # file_dir:      'tests\\resources\\empty'
        # file_name_ext: 'empty.asm'
        # file_name:     'empty'
    _, file_ext = os.path.splitext(asm_file_path)
    file_dir, file_name_ext = os.path.split(asm_file_path)      # TODO - file_dir might break in Linux since it's a str from Win, maybe fix it later
    file_name = file_name_ext.replace(f"{file_ext}","")

    # Try to open file
    try:
        asm_file = open(asm_file_path)
    except OSError: # as e:
        # TODO Log - logger.error(e)
        raise
    
    # only .asm is valid format
    if file_ext != ".asm":
        raise Exception("Invalid file extension, should be *.asm:", file_ext)  # TODO 'Exception Handling': define nicer exceptions

    # read every single line in .asm file to a list of strings and close it
    asm_lines = asm_file.readlines()
    asm_file.close()
    
    # create an empty .hack file in the same directory as the .asm file and switch back to the previous directory
    prev_dir = os.getcwd()
    os.chdir(file_dir)
    hack_file = open(f"{file_name}.hack", "w+")
    os.chdir(prev_dir)

    # if source is empty, close the empty hack file and we're done!
    if asm_lines == []:
        hack_file.close()
        print(f"\n\"{file_dir}\\{file_name}.hack\" was assembled.")
        print("----- Assembly complete! -----")
        return
    else:
        #print("\n----- start of assembly -----")
        p = h_parser.Parser(asm_lines)
        binary_commands = []

        while p.hasMoreCommands():
            p.advance()
            if p.commandType() == hc_fac.HackCommandType.C_COMMAND:
                binary_commands.append(f"111{h_code.comp(p.comp())}{h_code.dest(p.dest())}{h_code.jump(p.jump())}\n")
            else:
                binary_commands.append(format(p.symbol(), '016b') + "\n")

        hack_file.writelines(binary_commands)
        hack_file.close()
        print(f"\n\"{file_dir}\\{file_name}.hack\" was assembled.")
        print("----- Assembly complete! -----")
        
        return

if __name__ == "__main__":
    import sys
    try:
        asm_file_path = str(sys.argv[1])
        if os.path.isfile(asm_file_path):
            assemble_file(asm_file_path)
        else:
            print ("This file doesn't exist...")
            print("Give me a path to a Hack Assembly file (.asm)")
    except IndexError:
        print("Give me a path to a Hack Assembly file (.asm)")
