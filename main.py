from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        label = Label(text='Hello! My first APK works.', font_size=24)
        button = Button(text='Tap me', font_size=20, size_hint=(1, 0.3))
        button.bind(on_press=self.on_button_press)
        layout.add_widget(label)
        layout.add_widget(button)
        return layout

    def on_button_press(self, instance):
        instance.text = 'You tapped it!'

if __name__ == '__main__':
    MyApp().run()