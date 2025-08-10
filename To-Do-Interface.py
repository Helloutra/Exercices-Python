# Interface PyQt5 pour une application de To-Do List, nécessite PyQt5
# Assurez-vous d'avoir installé PyQt5 avec `pip install PyQt5`
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QListWidget
from PyQt5.QtCore import Qt

class ToDoInterface(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("To-Do List")
        self.setGeometry(100, 100, 400, 300)
        self.initUI()
    def initUI(self):
        layout = QVBoxLayout()
        self.todo_input = QLineEdit(self)
        self.todo_input.setPlaceholderText("Ajouter une tâche...")
        layout.addWidget(self.todo_input)
        self.todo_input.returnPressed.connect(self.ajouter_tache)
        self.ajouter_bouton = QPushButton("Ajouter", self)
        self.ajouter_bouton.clicked.connect(self.ajouter_tache)
        layout.addWidget(self.ajouter_bouton)
        self.todo_list = QListWidget(self)
        layout.addWidget(self.todo_list)
        self.enlever_bouton = QPushButton("Supprimer", self)
        self.enlever_bouton.clicked.connect(self.enlever_tache)
        layout.addWidget(self.enlever_bouton)
        self.completee_bouton = QPushButton("Marquer comme terminé", self)
        self.completee_bouton.clicked.connect(self.marquer_tache_terminee)
        layout.addWidget(self.completee_bouton)
        self.enlever_completee_bouton = QPushButton("Supprimer les tâches terminées", self)
        self.enlever_completee_bouton.clicked.connect(self.enlever_taches_terminees)
        layout.addWidget(self.enlever_completee_bouton)
        self.setLayout(layout)
        self.todo_input.setFocus()

    def ajouter_tache(self):
        task = self.todo_input.text().strip()
        if task:
            for i in range(self.todo_list.count()):
                if self.todo_list.item(i).text() == task:
                    self.todo_input.setText("Tâche déjà existante !")
                    self.todo_input.selectAll()
                    return
            self.todo_list.addItem(task)
            self.todo_input.clear()
        self.todo_input.setFocus()
# Supprimer une tâche sélectionnée
    def enlever_tache(self):
        selected_items = self.todo_list.selectedItems()
        if not selected_items:
            return
        for item in selected_items:
            self.todo_list.takeItem(self.todo_list.row(item))
# Mettre en gris les tâches terminées et les ajouter en fin de la liste
    def marquer_tache_terminee(self):
        selected_items = self.todo_list.selectedItems()
        if not selected_items:
            return
        for item in selected_items:
            item.setFlags(item.flags() & ~Qt.ItemIsSelectable)
            item.setForeground(Qt.gray)
            self.todo_list.takeItem(self.todo_list.row(item))
            self.todo_list.addItem(item)
            item.setFlags(item.flags() | Qt.ItemIsSelectable)
            item.setForeground(Qt.gray)
            self.todo_input.setFocus()

# Bouton pour supprimer les tâches terminées
    def enlever_taches_terminees(self):
        for i in range(self.todo_list.count() - 1, -1, -1):
            item = self.todo_list.item(i)
            if item.foreground().color() == Qt.gray:
                self.todo_list.takeItem(i)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ToDoInterface()
    window.show()
    sys.exit(app.exec_())