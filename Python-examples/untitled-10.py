PL = parser.Plist()

class EC_Conf_App(QDialog):

def __init__(self,parent = None,name = None,modal = 0,fl = 0):
    QDialog.__init__(self,parent,name,modal,fl)

    self.gridLayout = QGridLayout(self)        
    self.scrollArea = QScrollView(self)        
    self.scrollArea.setGeometry(0, 0, 369, 286)            
    self.Form1Layout = QGridLayout(self.scrollArea)        
    self.gridLayout.addWidget(self.scrollArea, 0, 0)  

    for item in PL.plist:
        self.section_create(item.name, item.variables)

def section_create(self, name, variables):


    # ADD ROW BUTTON 
    for key, value in sorted(variables.iteritems()):
        if len(value) > 3:  # if there is more than one option for the combobox
            self.addButton = QPushButton(self.scrollArea, name + '_AddButton')


            self.addButton.setText('Add Row')
            self.Form1Layout.addWidget(self.addButton, self.Ay, self.Ax)
            self.addButton.show()                
           self.connect(self.addButton,SIGNAL("clicked()"),self.add_rows)

def add_rows(self):
    self.addButton = self.sender()
    self.addButton.name()
    copy_class = self.addButton.name()
    clean_name = copy_class[:-10]
    for item in PL.plist:
        if item.name == clean_name:
            PL.insert(item.name, item.heading, item.variables)
            self.remove_widgets()
            break

def remove_widgets(self):
    for item in self.widgets:
        item.deleteLater()
        self.Form1Layout.remove(item)             

    self.construct()

def construct(self):
    for item in PL.plist:
        self.section_create(item.name, item.variables)
        