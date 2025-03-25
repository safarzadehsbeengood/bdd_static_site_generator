from textnode import *
from inline_markdown import *
import os
import shutil

def text_to_textnodes(text: str):
    res = [TextNode(text, TextType.TEXT)]

    # filter bold
    res = split_nodes_delimiter(res, "**", TextType.BOLD)
    
    # filter italics
    res = split_nodes_delimiter(res, '_', TextType.ITALIC)

    # filter code
    res = split_nodes_delimiter(res, '`', TextType.CODE)

    # filter images
    res = split_nodes_image(res)

    # filter links
    res = split_nodes_link(res)

    return res

def copy_files(src, dst):
    if not os.path.exists(dst):
        os.mkdir(dst)
    for filename in os.listdir(src):
        from_path = os.path.join(src, filename)
        dest_path = os.path.join(dst, filename)
        print(f' * {from_path} -> {dest_path}')
        if os.path.isfile(from_path):
            shutil.copy(from_path, dest_path)
        else:
            copy_files(from_path, dest_path)