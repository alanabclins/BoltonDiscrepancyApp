from kivy.app import App 
from kivy.uix.gridlayout import GridLayout 
from kivy.uix.label import Label 
from kivy.uix.image import Image 
from kivy.uix.button import Button 
from kivy.uix. textinput import TextInput
from kivy.graphics import Color, Rectangle
from kivy.uix.boxlayout import BoxLayout


class Bolton (App):
    def build (self):
        box = BoxLayout()
        self.window = GridLayout ()
        with box.canvas.before:
            Color(1, 1, 1, 1) 
            self.rect = Rectangle(size=(100000,100000))
        self.window.cols = 1
        #add widgets to window
        self.window.add_widget(Image(source="Logo.png", size_hint_y=None, height=200))
        #measures
        label_color = (0.33, 0.78, 0.80, 1)
        text_input_color = (0.87, 0.93, 0.93, 1)
        self.pergunta_md_superior = Label(text="Medida mésio-distal dos 12 dentes superiores", font_size=20, color=label_color)
        self.window.add_widget(self.pergunta_md_superior)
        self.md_superior=TextInput(multiline=False,background_normal='', background_color=text_input_color)
        self.window.add_widget(self.md_superior)

        self.pergunta_md_inferior = Label(text="Medida mésio-distal dos 12 dentes inferiores", font_size=20, color=label_color)
        self.window.add_widget(self.pergunta_md_inferior)
        self.md_inferior = TextInput(multiline=False,background_normal='', background_color=text_input_color)
        self.window.add_widget(self.md_inferior)

        self.pergunta_md_anterior_superior = Label(text="Medida mésio-distal dos 6 dentes anteriores superiores",font_size=20,  color=label_color)
        self.window.add_widget(self.pergunta_md_anterior_superior)
        self.md_anterior_superior = TextInput(multiline=False,background_normal='', background_color=text_input_color)
        self.window.add_widget(self.md_anterior_superior)

        self.pergunta_md_anterior_inferior = Label(text="Medida mésio-distal dos 6 dentes anteriores inferiores", font_size=20, color=label_color)
        self.window.add_widget(self.pergunta_md_anterior_inferior)
        self.md_anterior_inferior = TextInput(multiline=False,background_normal='', background_color=text_input_color)
        self.window.add_widget(self.md_anterior_inferior)

        

        #calculate
        self.window.add_widget(Label(height=5))
        self.calculate = Button(text="Calcular", font_size=25, background_color=(0.337, 0.784, 0.804, 1))
        self.window.add_widget(self.calculate)
        self.calculate.bind(on_press=self.calculate_bolton_discrepancy)
        self.result_label = Label(text="", font_size=20, color=(0.9, 0.5, 0.2, 1))
        self.result_anterior_label = Label(text="", font_size=20, color=(0.9, 0.5, 0.2, 1))
        self.window.add_widget(self.result_label)
        self.window.add_widget(self.result_anterior_label)
        box.add_widget(self.window)

        return box
    #function
    def calculate_bolton_discrepancy(self, instance):
        try:
            md_superior_value = float(self.md_superior.text)
            md_inferior_value = float(self.md_inferior.text)
            md_anterior_superior_value = float(self.md_anterior_superior.text)
            md_anterior_inferior_value = float(self.md_anterior_inferior.text)

            if md_superior_value <= 0 or md_inferior_value <= 0 or md_anterior_superior_value <= 0 or md_anterior_inferior_value <= 0:
                self.result_label.text = "Insira medidas válidas para os dentes."
            else:
                bolton_discrepancy= (md_inferior_value/md_superior_value)*100;  
                if( 89.39 <= bolton_discrepancy <= 93.21):
                    self.result_label.text = "Paciente não apresenta discrepância de Bolton total"
                else:
                    """
                    X= 12 Maxila do paciente - (12 mandibula do paciente / 0,8939)
                    Y= (12 Maxila do paciente / 0,8939) - mandibula do paciente
                    Z=  12 mandibula do paciente - (12 maxila do paciente / 0,9321)
                    W= (12 mandibula do paciente / 0,9321) - maxila do paciente
                    """
                    x=12*md_superior_value-(12*md_inferior_value/0.8939);
                    y= (12*md_superior_value/0.8939) - md_inferior_value; 
                    z=12*md_superior_value-(12*md_inferior_value/0.9321)
                    w=(12*md_superior_value/0.0321) - md_inferior_value;
                    if(bolton_discrepancy<89.39):  
                        self.result_label.text = f"O paciente apresenta discrepância de Bolton total, podendo ser interpretada como excesso de {x:.2f}mm no arco superior ou deficiência de {y:.2f}mm no arco inferior."
                    else:
                        self.result_label.text = f"O paciente apresenta discrepância de Bolton total, podendo ser interpretada como deficiência de {z:.2f}mm no arco superior ou excesso de {w:.2f}mm no arco inferior."
                #calculate canines, dont consider yet
            if 1+1==2:
                bolton_discrepancy= (md_anterior_inferior_value/md_anterior_superior_value)*100;  
                if( 89.39 <= bolton_discrepancy <= 93.21):
                    self.result_anterior_label.text = "Paciente não apresenta discrepância de Bolton anterior"
                else:
                    x=12*md_anterior_superior_value-(12*md_anterior_inferior_value/0.8939);
                    y= (12*md_anterior_superior_value/0.8939) - md_anterior_inferior_value; 
                    z=12*md_anterior_superior_value-(12*md_anterior_inferior_value/0.9321)
                    w=(12*md_anterior_superior_value/0.0321) - md_anterior_inferior_value;
                    if(bolton_discrepancy<89.39):  
                        self.result_anterior_label.text = f"O paciente apresenta discrepância de Bolton anterior, podendo ser interpretada como excesso de {x:.2f}mm no arco superior ou deficiência de {y:.2f}mm no arco inferior."
                    else:
                        self.result_anterior_label.text = f"O paciente apresenta discrepância de Bolton anterior, podendo ser interpretada como deficiência de {z:.2f}mm no arco superior ou excesso de {w:.2f}mm no arco inferior."
                    
        except ValueError:
            self.result_label.text = "Insira apenas números para as medidas."
        
        return self.window


Bolton().run()
