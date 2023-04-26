from typing import List


class WebsiteDataBlock:
    def __init__(self, kind: str, value: str):
        self.kind: str = kind
        self.value: str = value

    def to_dict(self):
        return {
            'kind': self.kind,
            'value': self.value
        }


class WebsiteContentBlock:
    def __init__(self, block_list: List[WebsiteDataBlock] = None):

        if block_list is None:
            self.block = []
        else:
            self.block: List[WebsiteDataBlock] = block_list

    def insert_data_block(self, data_block: WebsiteDataBlock):
        self.block.append(data_block)

    def to_dict(self):
        return {
            'block': [i.to_dict() for i in self.block]
        }


class WebsiteBlock:
    def __init__(self, name: str, content: List[WebsiteContentBlock] = None):
        self.name: str = name

        if content is None:
            self.content = []
        else:
            self.content: List[WebsiteContentBlock] = content

    def insert_content(self, content_block: WebsiteContentBlock):
        self.content.append(content_block)

    def to_dict(self):
        return {
            'name': self.name,
            'content': [i.to_dict() for i in self.content]
        }


class WebsitePage:
    def __init__(self, page_name: str, blocks: List[WebsiteBlock] = None):
        self.page_name: str = page_name

        if blocks is None:
            self.blocks = []
        else:
            self.blocks: List[WebsiteBlock] = blocks

    def insert_block(self, block: WebsiteBlock):
        self.blocks.append(block)

    def to_dict(self):
        return {
            'page_name': self.page_name,
            'blocks': [i.to_dict() for i in self.blocks]
        }


class Website:
    def __init__(self, pages: List[WebsitePage] = None):

        if pages is None:
            self.pages = []
        else:
            self.pages = pages

    def insert_page(self, page: WebsitePage):
        self.pages.append(page)

    def to_dict(self):
        return {
            "pages": [i.to_dict() for i in self.pages]
        }
