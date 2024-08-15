from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class AppNome( App ):
    
    txtNome = Nome

    def submit(self, e):
        print("Botão pressionado")
        print(self.txtNome.text)

    def build(self):
        box = BoxLayout(orientation="vertical")
        boxNome = BoxLayout(orientation="horizontal",
                            size_hint = (1.0, 0.2))
        lblNome = Label(text="Digite um nome", 
                        size_hint = (0.3, 1.0))
        self.txtNome = TextInput(size_hint = (0.7, 1.0))
        btnSalvar = Button(text="Salvar", size_hint = (1, 1),on_release = self.submit)

        boxNome.add_widget(lblNome)
        boxNome.add_widget(self.txtNome)
        box.add_widget(boxNome)
        box.add_widget(btnSalvar)
        return box
    

if __name__ == "__main__":
    app = AppNome()
    app.run()
    # AppNome().run()