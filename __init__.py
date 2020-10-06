from mycroft import MycroftSkill, intent_handler


class CommonVoice(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_handler('record.samples.intent')
    def handle_voice_common(self, message):
        self.speak_dialog('common.voice.record')
        self.gui.show_url('https://commonvoice.mozilla.org/en/speak')

    @intent_handler('review.samples.intent')
    def handle_review_samples(self, message):
        self.speak_dialog('common.voice.review')
        self.gui.show_url('https://commonvoice.mozilla.org/en/listen')


def create_skill():
    return CommonVoice()

