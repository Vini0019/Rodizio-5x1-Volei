import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.animation import Animation

kivy.require('2.1.0')  # Certifique-se de usar uma versão compatível do Kivy

class MyApp(App):
    def build(self):
        # Layout principal como FloatLayout
        layout = FloatLayout(size=(820, 400))

        # Adicione a imagem de fundo à tela
        background_image = Image(source='fundomodificado.png', allow_stretch=True, keep_ratio=False, size_hint=(1, 1), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        layout.add_widget(background_image)

        # Adicione a imagem 'bola.png' sobre a imagem de fundo
        self.ball_image = Image(source='bola.png', size_hint=(None, None), size=(100, 100), pos_hint={'center_x': 0.1, 'center_y': 0.2})
        layout.add_widget(self.ball_image)

        enemy_image = Image(source='enemy.png', size_hint=(None, None), size=(100, 100),
        pos_hint={'center_x': 0.5, 'center_y': 0.2})
        layout.add_widget(enemy_image)

        # Adicione 4 botões na tela
        button1 = Button(text='Saque', size_hint=(0.25, 0.1), pos_hint={'x': 0, 'top': 1})
        button2 = Button(text='Ataque', size_hint=(0.25, 0.1), pos_hint={'right': 1, 'top': 1})
        button3 = Button(text='Próxima Rotação', size_hint=(0.25, 0.1), pos_hint={'x': 0, 'y': 0})
        button4 = Button(text='Botão 4', size_hint=(0.25, 0.1), pos_hint={'right': 1, 'y': 0})

        button1.bind(on_press=self.move_ball)  # Vincula o evento de pressionar ao método move_ball

        layout.add_widget(button1)
        layout.add_widget(button2)
        layout.add_widget(button3)
        layout.add_widget(button4)

        return layout

    def move_ball(self, instance):
        # Move a imagem ball_image quando o button1 é pressionado de forma gradual
        animation = Animation(pos_hint={'center_x': 0.5, 'center_y': 0.5}, duration=1)
        animation.start(self.ball_image)

if __name__ == '__main__':
    MyApp().run()