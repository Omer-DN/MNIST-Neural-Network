
import wx
from googletrans import Translator

# List of popular languages
popular_languages = {
    'en': 'English',
    'he': 'Hebrew',
    'es': 'Spanish',
    'fr': 'French',
    'de': 'German',
    'zh-cn': 'Chinese',
    'ja': 'Japanese',
    'it': 'Italian'
}


class TranslationApp(wx.Frame):
    def __init__(self, *args, **kw):
        super(TranslationApp, self).__init__(*args, **kw)

        self.init_ui()

    def init_ui(self):
        panel = wx.Panel(self)

        main_sizer = wx.BoxSizer(wx.VERTICAL)

        # Source language selection
        src_lang_sizer = wx.BoxSizer(wx.HORIZONTAL)
        src_lang_label = wx.StaticText(panel, label="Select source language:")
        self.src_lang_choice = wx.Choice(panel, choices=list(popular_languages.values()))
        self.src_lang_choice.SetSelection(0)
        src_lang_sizer.Add(src_lang_label, 0, wx.ALL | wx.CENTER, 5)
        src_lang_sizer.Add(self.src_lang_choice, 0, wx.ALL, 5)

        # Destination language selection
        dest_lang_sizer = wx.BoxSizer(wx.HORIZONTAL)
        dest_lang_label = wx.StaticText(panel, label="Select destination language:")
        self.dest_lang_choice = wx.Choice(panel, choices=list(popular_languages.values()))
        self.dest_lang_choice.SetSelection(1)
        dest_lang_sizer.Add(dest_lang_label, 0, wx.ALL | wx.CENTER, 5)
        dest_lang_sizer.Add(self.dest_lang_choice, 0, wx.ALL, 5)

        # Sentence input
        sentence_sizer = wx.BoxSizer(wx.HORIZONTAL)
        sentence_label = wx.StaticText(panel, label="Enter sentence:")
        self.sentence_input = wx.TextCtrl(panel)
        sentence_sizer.Add(sentence_label, 0, wx.ALL | wx.CENTER, 5)
        sentence_sizer.Add(self.sentence_input, 1, wx.ALL | wx.EXPAND, 5)

        # Translate button
        self.translate_button = wx.Button(panel, label="Translate")
        self.translate_button.Bind(wx.EVT_BUTTON, self.on_translate)

        # Exit button
        self.exit_button = wx.Button(panel, label="Exit")
        self.exit_button.Bind(wx.EVT_BUTTON, self.on_exit)

        # Translation result
        self.translation_result = wx.StaticText(panel, label="", style=wx.ALIGN_CENTER_HORIZONTAL)

        # Add to main sizer
        main_sizer.Add(src_lang_sizer, 0, wx.EXPAND)
        main_sizer.Add(dest_lang_sizer, 0, wx.EXPAND)
        main_sizer.Add(sentence_sizer, 0, wx.EXPAND)
        main_sizer.Add(self.translate_button, 0, wx.ALL | wx.CENTER, 5)
        main_sizer.Add(self.exit_button, 0, wx.ALL | wx.CENTER, 5)
        main_sizer.Add(self.translation_result, 0, wx.ALL | wx.EXPAND, 5)

        panel.SetSizer(main_sizer)

        self.SetTitle("Sentence Translation")
        self.SetSize((400, 300))
        self.Centre()

    def on_translate(self, event):
        src_lang = list(popular_languages.keys())[self.src_lang_choice.GetSelection()]
        dest_lang = list(popular_languages.keys())[self.dest_lang_choice.GetSelection()]
        sentence = self.sentence_input.GetValue()

        if not sentence:
            self.show_error_dialog("Please enter a sentence to translate.")
            return

        try:
            translator = Translator()
            translation = translator.translate(sentence, src=src_lang, dest=dest_lang).text
            back_translation = translator.translate(translation, src=dest_lang, dest=src_lang).text
            self.translation_result.SetLabel(f"Translation: {back_translation}")
        except Exception as e:
            self.show_error_dialog(str(e))

    def show_error_dialog(self, error_text):
        wx.MessageBox(error_text, 'Error', wx.OK | wx.ICON_ERROR)

    def on_exit(self, event):
        self.Close()


def main():
    app = wx.App()
    frm = TranslationApp(None)
    frm.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()