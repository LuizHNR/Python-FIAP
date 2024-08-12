from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

class Cadastro( App ):
    
    def build(self):
        box_pai = BoxLayout(orientation = 'vertical')

        box = BoxLayout(orientation = 'horizontal')
        lbl_nome1 = Label(text= "Digite o nome")
        txt_nome1 = TextInput()
        box.add_widget(lbl_nome1)
        box.add_widget(txt_nome1)

        box1 = BoxLayout(orientation = 'horizontal')
        lbl_telefone = Label(text= "Digite o Telefone")
        txt_telefone = TextInput()   
        box1.add_widget(lbl_telefone)
        box1.add_widget(txt_telefone)

        box2 = BoxLayout(orientation = 'horizontal')
        lbl_email = Label(text= "Digite o seu email")
        txt_email = TextInput()   
        box2.add_widget(lbl_email)
        box2.add_widget(txt_email)

        box3 = BoxLayout(orientation = 'horizontal')
        btn_salvar = Button(text = "Salvar")
        btn_pesquisar = Button(text = "Pesquisar")
        box3.add_widget(btn_salvar)
        box3.add_widget(btn_pesquisar)

        box_pai.add_widget(box)
        box_pai.add_widget(box1)
        box_pai.add_widget(box2)
        box_pai.add_widget(box3) 
    
        return box_pai
    
obj_cadastro = Cadastro()
obj_cadastro.run()