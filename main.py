from kivy.app import App
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.animation import Animation

Window.size=(250,400)
Builder.load_file("main.kv")

#print(help(Button))

class Quiz(ScreenManager):
	def animate(self,anim):
		#print(anim)
		self.animating=Animation(
			background_color=(0,1,0,1),duration=1)
		self.animating+=Animation(
			background_color=(1,0,0,1),duration=1)

class Home(Screen):
	pass
class Help(Screen):
	pass
class Q1(Screen):
	pass		
class Q2(Screen):
	pass
			
class Q3(Screen):
	pass		
	
class Q4(Screen):
	pass	
		
class Q5(Screen):
	pass		
	
class FinalPage(Screen):
    pass


class QuizApp(App):
	Window.clearcolor="#001e1e"
	def build(self):
		return Quiz()

if __name__ == '__main__':
	QuizApp().run()
