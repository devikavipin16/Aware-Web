'''
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGridLayout(GridLayout):
    # Initialize infinite keywords
    def init(self, kwargs):
        # Call grid layout constructor
        super(MyGridLayout, self).init(kwargs)

        # Set columns
        self.cols = 2

        # Add widgets
        self.add_widget(Label(text="topic: "))
        # Add Input Box
        self.name = TextInput(multiline=True)
        self.add_widget(self.name)



        # Create a Submit Button
        self.submit = Button(text="Submit", font_size=32)
        # Bind the button
        self.submit.bind(on_press=self.press)
        self.add_widget(self.submit)

    def press(self, instance):
        Topic = self.name.text
        # this code thats hashed on the bottem is for the out put modify it to fit our code 

        #print(f'Hello {name}, you like {pizza} pizza, and your favorite color is {color}!')
        # Print it to the screen
        #self.add_widget(Label(text=f'Hello {name}, you like {pizza} pizza, and your favorite color is {color}!'))

        # Clear the input boxes
        self.name.text = ""

class MyApp(App):
    def build(self):
        return MyGridLayout()
        if self.name == 'main':
            MyApp().run()
'''
#Commented out so it doens't load package every time 