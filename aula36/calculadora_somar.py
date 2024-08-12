from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

class CalculadoraSoma( App ):
    
    def build(self):
        box_pai = BoxLayout(orientation = 'vertical')

        box = BoxLayout(orientation = 'horizontal')
        lbl_numero1 = Label(text= "Digite o primeiro numero")
        txt_numero1 = TextInput()
        box.add_widget(lbl_numero1)
        box.add_widget(txt_numero1)

        box1 = BoxLayout(orientation = 'horizontal')
        lbl_numero2 = Label(text= "Digite o segundo numero")
        txt_numero2 = TextInput()   
        box1.add_widget(lbl_numero2)
        box1.add_widget(txt_numero2)

        box2 = BoxLayout(orientation = 'vertical')
        btn_somar = Button(text = "Somar")
        box2.add_widget(btn_somar)

        box_pai.add_widget(box)
        box_pai.add_widget(box1)
        box_pai.add_widget(box2) 
    
        return box_pai
    
obj_calculadora_soma = CalculadoraSoma()
obj_calculadora_soma.run()
        
