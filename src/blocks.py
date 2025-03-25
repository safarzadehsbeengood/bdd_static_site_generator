from enum import Enum
from htmlnode import *
from inline_markdown import *
from textnode import *

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block: str):
    if block.startswith('#'):
        return BlockType.HEADING
    elif block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    elif all([line.startswith(">") for line in block.split('\n')]):
        return BlockType.QUOTE
    elif all([line.startswith("- ") for line in block.split('\n')]):
        return BlockType.UNORDERED_LIST
    elif block[0] == '1':
        i = 1
        valid = True
        for line in block.split('\n'):
            if line.startswith(f'{i}. '):
                i += 1
            else:
                valid = False
                break 
        if valid:
            return BlockType.ORDERED_LIST 
        else:
            return BlockType.PARAGRAPH
    else:
        return BlockType.PARAGRAPH

