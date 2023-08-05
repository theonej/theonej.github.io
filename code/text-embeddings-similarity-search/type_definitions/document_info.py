from pydantic import BaseModel

class DocumentInfo(BaseModel):

    name : str
    url : str
    text : str
    
    def get_terms(self):
        term_array = self.clean_text(self.text)

        return term_array

    def clean_text(self, text_to_clean):
        term_array = text_to_clean.split(' ')
        
        term_array = list(map(lambda text: self.remove_newlines(text), term_array))
        term_array = list(filter(lambda text: text != '', term_array))

        return term_array

    def remove_newlines(self, text):
        text = text.replace('\n', '')

        return text