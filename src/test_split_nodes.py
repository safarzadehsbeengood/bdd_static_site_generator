import unittest
from textnode import *
from inline_markdown import *

class TestHTMLNode(unittest.TestCase):
    def test_italic(self):
        node = TextNode("This is an _italic_ word", TextType.TEXT) 
        actual = split_nodes_delimiter([node], "_", TextType.ITALIC)
        expected = [
            TextNode("This is an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(actual, expected)

    def test_bold(self):
        node = TextNode("This is a **bold** word", TextType.TEXT) 
        actual = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected = [
            TextNode("This is a ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(actual, expected)
        
    def test_code(self):
        node = TextNode("This is a `code block` in markdown", TextType.TEXT) 
        actual = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
            TextNode("This is a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" in markdown", TextType.TEXT),
        ]
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()