import unittest
from blocks import *
from markdown import *

class TestTextNode(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
        """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )        

    def test_block_to_blocktype(self):
        # UL
        block = "- This is a list\n- with items"
        actual = block_to_block_type(block)
        expected = BlockType.UNORDERED_LIST
        self.assertEqual(actual, expected)

        # OL
        block = "1. one\n2. two\n3. three"
        actual = block_to_block_type(block)
        expected = BlockType.ORDERED_LIST
        self.assertEqual(actual, expected)

        # code
        block = "```\nint main() {\n\treturn 0;\n}\n```"
        actual = block_to_block_type(block)
        expected = BlockType.CODE
        self.assertEqual(actual, expected)

        # quote
        block = "> hello\n> this is a quote"
        actual = block_to_block_type(block)
        expected = BlockType.QUOTE
        self.assertEqual(actual, expected)

        # heading
        block = "### heading\nthis is a heading with 3 pound signs"
        actual = block_to_block_type(block)
        expected = BlockType.HEADING
        self.assertEqual(actual, expected)

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )