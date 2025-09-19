from ..interfaces.multilingual_support import MultilingualSupportInterface

class MultilingualSupportService(MultilingualSupportInterface):
    def __init__(self, ai_client):
        self.ai_client = ai_client

    def translate(self, text, target_language):
        return self.ai_client.translate(text, target_language)
