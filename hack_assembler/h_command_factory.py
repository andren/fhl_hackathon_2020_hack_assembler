import re
from enum import Enum
from abc import ABC, abstractclassmethod

class HackCommandType(Enum):
    A_COMMAND = 1
    C_COMMAND = 2
    L_COMMAND = 3

def hack_command_factory(inp: str):

    # remove comments and whitespace        # TODO - duplicate code here, could be refactored later
    r_asmCommentsAndWhitespace = r"([^\n\S]*\/\/[^\n]*)|([\s]*)"
    inp = re.sub(r_asmCommentsAndWhitespace, '', inp)    # ASM Comments and whitespace are replaced by nothing      # TODO - maybe RegEx could be improved to a single-step
    inp = re.sub('\n', '', inp)             # \n is left over and replaced by nothing

    # remove empty elements
    if inp == "":
        raise ValueError(f"input is invalid:{inp}")

    # Assumption for these RegEx patterns is that they have a list of possible commands without comments, whitespace nor empty elements
    a_re = r"^@.*"
    c_re = r"^[^@(].*"
    l_re = r"^\(.*\)$"

    if re.match(a_re, inp):
        return ACommand(inp)
    elif re.match(c_re, inp):
        return CCommand(inp)
    elif re.match(l_re, inp):
        return LCommand(inp)
    else:
        raise ValueError(f"Invalid Hack command:{inp}")

class HackCommand(ABC):
    pass

class ACommand(HackCommand):
    # Properties
    raw: str
    cmdType = HackCommandType.A_COMMAND
    symbol: str

    # Methods
    def __init__(self, inp: str):
        self.raw = inp
        self.symbol = self.raw.replace("@","")

    def __eq__(self, other):
        if not isinstance(other, ACommand):  # don't compare with unrelated types
            return NotImplemented
        else:
            return self.cmdType == other.cmdType and self.raw == other.raw

class CCommand(HackCommand):

    # Properties
    raw: str
    cmdType = HackCommandType.C_COMMAND
    dest: str
    comp: str
    jump: str

    # Methods
    def __init__(self, inp: str):
        self.raw = inp

        re_c = r"(^.*)([=;])(.*)"
        commandPartsList = re.match(re_c, self.raw).groups()
        if commandPartsList[1] == '=':
            self.dest = commandPartsList[0]
            self.comp = commandPartsList[2]
            self.jump = "null"
        elif commandPartsList[1] == ';':
            self.dest = "null"
            self.comp = commandPartsList[0]
            self.jump = commandPartsList[2]
        else:
            raise Exception("Something very wrong has happened")

    def __eq__(self, other):
        if not isinstance(other, CCommand):  # don't compare with unrelated types
            return NotImplemented
        else:
            return self.cmdType == other.cmdType and self.raw == other.raw

class LCommand(HackCommand):
    # Properties
    raw: str
    cmdType = HackCommandType.L_COMMAND
    symbol: str

    # Methods
    def __init__(self, inp: str):
        self.raw = inp
        self.symbol = "symbol"
    
    def __eq__(self, other):
        if not isinstance(other, LCommand):  # don't compare with unrelated types
            return NotImplemented
        else:
            return self.cmdType == other.cmdType and self.raw == other.raw