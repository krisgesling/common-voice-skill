from mycroft import MycroftSkill, intent_file_handler


class CommonVoice(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('voice.common.intent')
    def handle_voice_common(self, message):
        self.speak_dialog('voice.common')


def create_skill():
    return CommonVoice()

