import os
import json
import uuid
from api.redis_db import RedisDB

from langchain.llms import AI21

from core.models.website import Website, WebsiteDataBlock, \
    WebsiteContentBlock, WebsiteBlock, WebsitePage


def generate_website(idea) -> [str, dict]:
    website = Website()

    llm = AI21(model='j2-jumbo-instruct', maxTokens=152, temperature=0.9)

    path = os.getcwd()

    template_path = path + os.sep + 'templates' + os.sep + 'basic-template.json'

    with open(template_path, 'r') as file:
        template_json = file.read()
        file.close()

    template_json = json.loads(template_json)

    pages = template_json['website']['pages']

    for page in pages:
        page_name = page['pageName']
        blocks = page['blocks']
        website_page = WebsitePage(page_name)

        for block in blocks:
            name = block['name']
            content = block['content']
            website_block = WebsiteBlock(name)

            for item in content:
                block_data = item['block']
                website_block_content = WebsiteContentBlock()

                for data in block_data:
                    prompt: str = data['prompt']
                    kind = data['value']

                    if '{{businessIdea}}' in prompt:
                            prompt = prompt.replace('{{businessIdea}}', idea)
                        
                    if '{{feature}}' in prompt:
                        prompt = prompt.replace('{{feature}}', previousValue)

                    if '{{previousFeature}}' in prompt:
                         prompt = prompt.replace('{{previousFeature}}', previousValue)

                    result = llm.generate([prompt])
                    value = result.generations[0][0].text
                    value = value.replace('\n', '').replace('\"', '')

                    web_block = WebsiteDataBlock(kind, value)
                    previousValue = web_block.value
                    website_block_content.insert_data_block(web_block)

                website_block.insert_content(website_block_content)
            website_page.insert_block(website_block)
        website.insert_page(website_page)

    website_dict = website.to_dict()
    _id = str(uuid.uuid4())
    RedisDB().redis_db.set(_id, str(website_dict))

    return _id, website_dict
