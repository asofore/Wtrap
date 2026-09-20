from kivy.core.window import Window
from kivy.app import App
from kivy.uix.bubble import BubbleButton
from kivy.uix.widget import Widget
from kivy.animation import Animation
from kivy.properties import ObjectProperty
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.lang.builder import Builder
from random import choice
from kivy.uix.popup import Popup
from kivy.graphics import Line,Color
from kivy.core.audio import SoundLoader
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.uix.screenmanager import FadeTransition
from kivy.core.audio import SoundLoader





### ###
h,w=Window.size

d_w=w/8
d_h=500


x_p1=0
x_p2=w/8
x_p3=w/4
x_p4=w/4+w/8

gv=[h+(d_h*3),h+(d_h*2),h+(d_h*4)]
#gv=[2800,3000]

####

def cy(original_duration, original_distance, new_distance):
    speed = original_distance / original_duration
    new_duration = new_distance / speed
    return new_duration


####
KV="""
#:import Clock kivy.clock.Clock

<B1>:
	lose:lambda:app.open_p()
<R1>:
	rt:lambda:app.reloads1()
	cr:lambda:app.cu('mainmenu')
	
<Tb@TouchRippleButtonBehavior+Label>:
	size_hint:None,None
	pos_hint:{'center_x':0.5,'center_y':0.5}
	width:app.w/4+100
	height:app.w/8
	canvas.before:
		Rectangle:
			pos:self.pos
			size:self.size
			source:'bt.png'
		

<MainMenu>:
	orientation:'vertical'
	spacing:50
	Label:
	Tb:
		text:'Start'
		on_press:
			Clock.schedule_once(lambda e:app.cu('game'),0.2)
			
	#Tb:
	#	text:'Settings'
		
	Tb:
		text:'Exit'
		on_press:
			Clock.schedule_once(lambda e:exit(),0.2)
	Label:
	Label:
		size_hint_y:None
		#color:1,1,0,1
		text:'Version : 0.1' 
	
	
		


<M1>:
	orientation:'vertical'
	
	BoxLayout:
		size_hint_y:None
		canvas:
			Color:
				rgba:1,0,0,0.01
			Rectangle:
				pos:self.pos
				size:self.size
		
		
				
		
	M2:
		D1:
			id:line1
			
		D2:
			id:line2
			#B1:
				#parnetes:line2
		D3:
			id:line3
			#B1:
				#parnetes:line3
		D4:
			id:line4
			#B1:
				#parnetes:line4
			
			

"""
Builder.load_string(KV)

#########


class S1(object):
	def __init__(self):
		self.color=[1,1,0,5]
		self.d2rm=0.2
		self.speed=1.5
		self.dftc=[1,0,0,1]
		self.dfbc=[0,0,1,5]
		
		
class M1(BoxLayout):
	pass
class M2(Widget):
	def __init__(self,*args,**kwargs):
		super().__init__(*args,**kwargs)
		
class D1(Widget):
	def __init__(self,*args,**kwargs):
		super().__init__(*args,**kwargs)
		Clock.schedule_once(lambda e:self.add_widget(B1(parentes=self)),choice([0.7,1,0.1]))
		
		with self.canvas:
			Color(1,0,0,1)
			Line(points=[x_p2,0,x_p2,h*2+150],width=2)
			
class D2(Widget):
	def __init__(self,*args,**kwargs):
		super().__init__(*args,**kwargs)
		Clock.schedule_once(lambda e:self.add_widget(B1(parentes=self)),choice([0.7,1,0.1]))
		
		with self.canvas:
			Color(1,0,0,1)
			Line(points=[x_p3,0,x_p3,h*2+150],width=2)
		
class D3(Widget):
	def __init__(self,*args,**kwargs):
		super().__init__(*args,**kwargs)
		Clock.schedule_once(lambda e:self.add_widget(B1(parentes=self)),choice([0.7,1,0.1]))
		
		with self.canvas:
			Color(1,0,0,1)
			Line(points=[x_p4,0,x_p4,h*2+150],width=2)
		
class D4(Widget):
	def __init__(self,*args,**kwargs):
		super().__init__(*args,**kwargs)
		Clock.schedule_once(lambda e:self.add_widget(B1(parentes=self)),choice([0.7,1,0.1]))
class B1(BubbleButton):
	parentes=ObjectProperty()
	def __init__(self,*args,**kwargs):
		super().__init__(*args,**kwargs)
		self.s=S1()
		self.stoped=False
		self.background_normal='bkc.png'
		#self.background_down='bkc.png'
		
		
		###
		self.background_color=[0,0,1,1]
		self.width=d_w
		self.height=d_h
		#self.y=h+(d_h*2)
		self.y=choice(gv)
		
		#self.text=int(selt.y)
		#self.text=str(self.y)
		
		
		##
	def on_touch_down(self,t):
		self.background_color=0,0,1,2
		return super().on_touch_down(t)
	def on_parent(self,m,p):
		if p.__class__==D1:
			self.x=x_p1
		elif p.__class__==D2:
			self.x=x_p2
		elif p.__class__==D3:
			self.x=x_p3
		elif p.__class__==D4:
			self.x=x_p4
		else:
			self.x=x_p1
			
		self.start()
		
	def on_press(self):
		self.remove()
		Clock.schedule_once(self.addb,choice([0.7,1,0.1]))
		#print(self.parent)
		
		self.disabled=True
		

		return super().on_press()
	
	def start(self):
		self.animy()
		
	
	def remove(self):
		self.stoped=True
		self.animation.stop(self)
		Clock.schedule_once(lambda d:self.parent.remove_widget(self),0.2)
	def animy(self):
		'''
		g=cy(
		h+d_h,
		-500,
		self.s.speed,
		choice(gv)
		)'''
		self.speed=cy(self.s.speed,h+d_h,self.y)
		
		self.animation=Animation(y=-500,duration=self.speed)
		self.animation.start(self)
		#self.animation.on_progress
		
		self.animation.bind(on_complete=lambda *dt:self.tr())
	def lose(self):
		pass
		
	def tr(self):
		if self.stoped:
			#print(0)
			pass
		else:
			self.lose()
		
	def addb(self,dt):
		self.parentes.add_widget(B1(parentes=self.parentes))
		#print(self.parentes)
		#self.parent.add_widget(B1())
class R1(BubbleButton):
	def __init__(self,*args,**kwargs):
		super().__init__(*args,**kwargs)
		self.s=S1()
		self.color=self.s.dftc
		self.background_color=self.s.dfbc
		self.background_color=1,0,0,3
		self.background_normal='bt.png'
		#self.background='bt.png'
		
	
	def on_disabled(self,z,x):
		pass
		
	def on_press(self):
		if self.text=='exit':
			Clock.schedule_once(lambda s:exit(),0.2)
		elif self.text=='restart':
			self.rt()
		elif self.text=='menu':
			self.cr()
		else:
			pass
		
		
	def rt(self):
		pass
	def cr(self):
		pass

class P1(Popup):
	def __init__(self,*args,**kwargs):
		super().__init__(*args,**kwargs)
		s=S1()
		self.title='Game Over'
		self.title_color=s.dftc
		self.size_hint=None,None
		self.size=w/3+200,w/3
		self.auto_dismiss=False
		self.background_color=1,1,0,1
		#self.background='popup.jpg'
		
		
		self.is_open=False
		
		b=BoxLayout()
		j=BoxLayout()
		self.k=BoxLayout()
		b.orientation='vertical'
		
		self.t=Label()
		
		self.t.text='0'
		self.t.font_size=100
		
		j.add_widget(self.t)
		
		self.k.height=self.height/3
		
		self.k.add_widget(R1(text='menu'))
		self.k.add_widget(R1(text='restart'))
		self.k.add_widget(R1(text='exit'))
		
		b.add_widget(j)
		b.add_widget(self.k)
		
		
		self.content=b
	
	def on_dismiss(self):
		self.is_open=False
		
		return super().on_dismiss()
	def on_open(self):
		self.is_open=True
		
		for i in self.k.children:
			i.disabled=True
		
		Clock.schedule_once(self.one,1)
		
	def one(self,dt):
		Clock.schedule_once(self.two,1)
		self.t.text='1'
	def two(self,dt):
		Clock.schedule_once(self.rtv,1)
		self.t.text='2'
	
	def rtv(self,dt):
		self.t.text='3'
		
		for i in self.k.children:
			i.disabled=False
		
class MainMenu(BoxLayout):
	pass

	
########



class Main(App):
	lose=P1()
	sm=ScreenManager()
	w,h=w,h
	def reloads1(self):
		self.s1.clear_widgets()
		self.s1.add_widget(M1())
		self.close_p()
	
	def cu(self,name):
		self.sm.current=name
		if self.lose.is_open:
			self.lose.dismiss()
		
	def open_p(self):
		if not self.lose.is_open:
			self.lose.open()
			
	def close_p(self):
			if self.lose.is_open:
				Clock.schedule_once(lambda dt:self.lose.dismiss(),0.2)

	def build(self):
		
		self.sm.transition=FadeTransition()

		
		g=SoundLoader.load('/sdcard/bdf/file/Powerful-Trap-(chosic.com).mp3')

		self.s1=Screen()
		self.s1.name='game'
		#self.s1.add_widget(M1())
		
		#self.s1.on_enter
		
		self.s1.bind(on_enter=lambda e:self.s1.add_widget(M1()))
		
		
		
		self.s2=Screen()
		self.s2.name='mainmenu'
		self.s2.add_widget(MainMenu())
		
		
		
		self.sm.add_widget(self.s2)
		self.sm.add_widget(self.s1)
		
		return self.sm

Main().run()


