class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value 
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        if self.props:
            return f" {' '.join([f'{k}="{v}"' for k, v in self.props.items()])}"
        return ''

    def __repr__(self):
        return f'tag: {self.tag}\nvalue: {self.value}\nchildren: {self.children}\nprops: {self.props}'

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if not self.tag:
            return self.value
        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError("Parent node does not have a tag!")
        if not self.children:
            raise ValueError("Parent node does not have children!")
        children_html = []
        for child in self.children:
            children_html.append(child.to_html())
        return f'<{self.tag}{self.props_to_html()}>{''.join(children_html)}</{self.tag}>'