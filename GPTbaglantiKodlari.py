# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 08:45:33 2023

@author: Simge
"""
import sys
import openai
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QTextEdit, QVBoxLayout, QWidget

openai.api_key = "API-KEY" # API KEY'inizi yazın


class RichTextButtonApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Ana pencere
        self.setWindowTitle("ChatGPT Chat Bot")
        self.setGeometry(100, 100, 800, 400)

        # Merkez widget 
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Dikey bir düzen oluştur
        layout = QVBoxLayout()

        # İlk rich text kutusu (metin girişi için)
        self.input_text = QTextEdit(self)
        layout.addWidget(self.input_text)

        # İkinci rich text kutusu (ChatGPT'nin cevabı için)
        self.output_text = QTextEdit(self)
        layout.addWidget(self.output_text)

        # Buton ve tıklama olayı
        button = QPushButton("Sohbet Et")
        button.clicked.connect(self.chatWithGPT)
        layout.addWidget(button)

        central_widget.setLayout(layout)

    def GPT(self, text):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": f"{text}"}
            ]
        )
        l_text = response.choices[0].message['content']
        return l_text

    def chatWithGPT(self):
        # Kullanıcının girdisi
        user_input = self.input_text.toPlainText()

        # GPT cevap
        response = self.GPT(user_input)

        # Cevap için ikinci text 
        self.output_text.setPlainText(response)

def main():
    app = QApplication(sys.argv)
    window = RichTextButtonApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

