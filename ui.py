import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextBrowser, QLineEdit, QPushButton
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from threading import Thread
import time

class app(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        # Set up the main layout
        layout = QVBoxLayout()

        # Text browser for chat history
        self.chat_history = QTextBrowser()
        self.chat_history.setFont(QFont("Arial", 12))
        layout.addWidget(self.chat_history)

        # Input field for user messages
        self.user_input = QLineEdit()
        self.user_input.setFont(QFont("Arial", 12))
        layout.addWidget(self.user_input)

        # Send button
        send_button = QPushButton("Send")
        send_button.clicked.connect(self.send_message)
        layout.addWidget(send_button)

        self.setLayout(layout)

        # Create an instance of the BloodTestCenterChatbot
        self.chatbot = BloodTestCenterChatbot()

        # Display welcome message
        self.display_message("BloodBot: Welcome to the Metropolis Chatbot!\n"
                             "You can ask about available tests, their prices, or additional information.\n"
                             "Type 'exit' to end the conversation.\n")

        self.setWindowTitle('Blood Test Center Chatbot')
        self.setGeometry(100, 100, 800, 600)
        self.show()

    def send_message(self):
        user_input = self.user_input.text()
        self.display_message(f"You: {user_input}\n")

        if user_input.lower() in ['exit', 'quit', 'bye']:
            self.display_message("BloodBot: Goodbye! Have a great day.\n")
            self.close()
            return

        # Simulate thinking time (you can remove this line)
        self.display_message("BloodBot: Thinking...\n")
        time.sleep(1)

        response = self.chatbot.respond(user_input)
        self.display_message(f"BloodBot: {response}\n")

        # Clear user input
        self.user_input.clear()

    def display_message(self, message):
        self.chat_history.append(message)
        self.chat_history.verticalScrollBar().setValue(self.chat_history.verticalScrollBar().maximum())


class BloodTestCenterChatbot:
    # (Your existing chatbot class here)

 if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ChatbotUI()
    sys.exit(app.exec_())
