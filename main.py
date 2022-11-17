import base64
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
class MyMain(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def encode(self):
        string = self.inputdata.text
        try:
            string = string.encode("ascii")
            data = base64.b64encode(string)
            data = data.decode("ascii")
            self.outputdata.text = str(data)
        except:
            self.outputdata.text = "Not valid base64code"
    def decode(self):
        string = self.inputdata.text
        try:
            data = base64.b64decode(string)
            data = data.decode("ascii")
            self.outputdata.text = str(data)
        except:
            self.outputdata.text = "Invalid base64code"

class MyBase64decoderApp(App):
    pass

if __name__=="__main__":
    MyBase64decoderApp().run()
