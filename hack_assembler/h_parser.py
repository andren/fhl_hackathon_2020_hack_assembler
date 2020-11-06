import os
from pathlib import Path
import re
from enum import Enum
#from hack_assembler.hack_command_factory import hack_command_factory, HackCommandType, HackCommand
import h_command_factory as h_fac

class Parser:
    """Breaks each assembly command into its underlying components.

    Encapsulates access to the input code. Reads an assembly language command, parses it, and 
    provides convenient access to the command’s components (fields and symbols). In addition, 
    removes all white space and comments.

    Note: each line is a command.
    """

    # --- Properties ---
    commandList: [h_fac.HackCommand]
    currentCommand: h_fac.HackCommand

    # --- Methods ---
    # TODO 'in-line A-inst': implement support for "D=A [2]" format. Currently only "@2","D=A" format is supported.
    def __init__(self, asm_lines: [str]):
        """Constructor/Initializer - Opens the input file and gets ready to parse it

        Constructor/Initializer - Opens the input file and gets ready to parse it
        :param inputFilePath: Path to the .asm file to be parsed, relative to the assembler project root directory
        :type inputFilePath: Path
        """
        # remove comments and whitespace
        r_asmCommentsAndWhitespace = r"([^\n\S]*\/\/[^\n]*)|([\s]*)"
        for i in range(len(asm_lines)):
            asm_lines[i] = re.sub(r_asmCommentsAndWhitespace, '', asm_lines[i])    # ASM Comments and whitespace are replaced by nothing
            asm_lines[i] = re.sub('\n', '', asm_lines[i])             # \n is left over and replaced by nothing

        # remove empty elements from asm_lines
        asm_lines = list(filter(None, asm_lines))

        # use factory to translate a list of strings with potential Assembly commands to a list of Hack Assembly commands
        self.commandList = []
        for line in asm_lines:
            self.commandList.append(h_fac.hack_command_factory(line))
    
    def hasMoreCommands(self) -> bool:
        """Are there more commands in the input?
        """
        if not self.commandList:
            return False
        else:
            return True

    def advance(self):
        """Reads the next command from the input and makes it the current command.

        Should be called only if hasMoreCommands() is true. Initially there is no current command.
        """
        self.currentCommand = self.commandList.pop(0)

    def commandType(self) -> h_fac.HackCommandType:
        """Returns the type of the current command.

        A_COMMAND for @Xxx where Xxx is either a symbol or a decimal number.
        C_COMMAND for dest=comp;jump.
        L_COMMAND for (Xxx) where Xxx is a symbol (this is actually a pseudo-command).
        """
        return self.currentCommand.cmdType
    
    def symbol(self) -> str:
        """Returns the symbol or decimal Xxx of the current command @Xxx or (Xxx).

        Should be called only when commandType() is A_COMMAND or L_COMMAND.
        """
        if self.currentCommand.cmdType == h_fac.HackCommandType.C_COMMAND:
            raise ValueError("Invalid current command type:", self.currentCommand.cmdType)
        
        try:
            return int(self.currentCommand.symbol)
        except ValueError:
            raise NotImplementedError("Symbol Table not yet implemented, only asm literals supported for now")
    
    def dest(self) -> str:
        """Returns the dest mnemonic in the current C_COMMAND (8 possibilities).

        Should be called only when commandType() is C_COMMAND.
        """
        if self.currentCommand.cmdType != h_fac.HackCommandType.C_COMMAND:
            raise ValueError("Invalid current command type:", self.currentCommand.cmdType)

        return self.currentCommand.dest

    def comp(self) -> str:
        """Returns the comp mnemonic in the current C_COMMAND (28 possibilities).

        Should be called only when commandType() is C_COMMAND.
        """
        if self.currentCommand.cmdType != h_fac.HackCommandType.C_COMMAND:
            raise ValueError("Invalid current command type:", self.currentCommand.cmdType)

        return self.currentCommand.comp

    def jump(self) -> str:
        """Returns the jump mnemonic in the current C_COMMAND (8 possibilities).

        Should be called only when commandType() is C_COMMAND.
        """
        if self.currentCommand.cmdType != h_fac.HackCommandType.C_COMMAND:
            raise ValueError("Invalid current command type:", self.currentCommand.cmdType)

        return self.currentCommand.jump
        