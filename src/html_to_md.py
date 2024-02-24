import json
from bs4 import BeautifulSoup

class HTML_to_md():
    
    @classmethod
    def get_audio_transript(cls, raw_html):
        elements = (
            BeautifulSoup(raw_html, 'html.parser')
            .find_all(attrs={
                "class": "transcript-list-item"
            })
        )
        conversation = cls._get_conversation(elements)

        return conversation
    
    @classmethod
    def _get_conversation(cls, html_list):
        chat = map(
            lambda element: (
                cls._get_username(element),
                cls._get_text(element)
                ),
            html_list
        )

        conversation = []

        for name,text in chat:
            if not name:
                conversation[-1] += (f" {text}")
            else:
                conversation.append(
                    f"_{name}_: {text}"
                )

        return (2*"\n").join(conversation)

    @staticmethod
    def _get_class_content(html_element, class_tag):
        matches = html_element.find(attrs={"class": class_tag})
        return (
            matches.text.strip()
            if not (matches is None)
            else matches
        )
    
    @classmethod
    def _get_username(cls, html_element):
        return cls._get_class_content(html_element, "user-name-span")

    @classmethod
    def _get_text(cls, html_element):
        return cls._get_class_content(html_element, "text")

    def __str__(self):
        return json.dumps(
            self.raw_dict,
            indent=4
        )
