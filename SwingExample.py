from javax.swing import JFrame , WindowConstants, JPanel, JLabel,JTextField, JButton , \
    JOptionPane
from java.awt import Dimension, Point, GridLayout
from java.lang import Integer, Long, String , Boolean , Double, Exception as JavaException


class SwingExample:
    def example1(self):
        class CustomFrame(JFrame):
            def __init__(self):
                self.initGUI()


            def initGUI(self):
                self.title = "Swing Example"
                self.size = Dimension(500, 500)
                self.setLocation(Point(10, 10))
                self.defaultCloseOperation = WindowConstants.EXIT_ON_CLOSE
                self.addComponents()
                self.registerEvents()
                self.visible = True

            def addComponents(self):
                # mainPanel
                self.mainPanel = JPanel()
                self.mainPanel.setLayout(GridLayout(7, 2, 1, 1))
                self.getContentPane().add(self.mainPanel)
                # title
                self.lblEmpty = JLabel("")
                self.lblTitle = JLabel("Simple Swing Form")
                self.mainPanel.add(self.lblEmpty)
                self.mainPanel.add(self.lblTitle)

                # id
                self.lblId = JLabel("Id: ")
                self.fieldId = JTextField()
                self.mainPanel.add(self.lblId)
                self.mainPanel.add(self.fieldId)

                # name
                self.lblName = JLabel("Name: ")
                self.fieldName = JTextField()
                self.mainPanel.add(self.lblName)
                self.mainPanel.add(self.fieldName)

                # age
                self.lblAge = JLabel("Age: ")
                self.fieldAge = JTextField()
                self.mainPanel.add(self.lblAge)
                self.mainPanel.add(self.fieldAge)

                # wage
                self.lblWage = JLabel("Wage: ")
                self.fieldWage = JTextField()
                self.mainPanel.add(self.lblWage)
                self.mainPanel.add(self.fieldWage)

                # active
                self.lblActive = JLabel("Active: ")
                self.fieldActive = JTextField()
                self.mainPanel.add(self.lblActive)
                self.mainPanel.add(self.fieldActive)

                # buttons
                self.btnOk = JButton("Ok")
                self.btnClear = JButton("Clear")
                self.mainPanel.add(self.btnOk)
                self.mainPanel.add(self.btnClear)







            def registerEvents(self):
                self.btnOk.addActionListener(lambda event: self.onBtnOkClicked())
                self.btnClear.addActionListener(lambda event: self.onBtnClearClicked())


            def onBtnOkClicked(self):
                try:
                    id = Long.parseLong(self.fieldId.text)
                    name = String.valueOf(self.fieldName.text)
                    age = Integer.parseInt(self.fieldAge.text)
                    wage = Double.parseDouble(self.fieldWage.text)
                    active = Boolean.parseBoolean(self.fieldActive.text)
                    title = "<<Information>>"
                    message = """id = {0}
name = {1}
age = {2}
wage = {3}
active = {4}
""".format(id, name, age, wage, active)
                    JOptionPane.showMessageDialog(self, message, title , JOptionPane.INFORMATION_MESSAGE)

                except JavaException as ex:
                    message = ex.message
                    title = "<<Error>>"
                    JOptionPane.showMessageDialog(self, message, title, JOptionPane.ERROR_MESSAGE)




            def onBtnClearClicked(self):
                self.fieldId.text = ""
                self.fieldName.text = ""
                self.fieldAge.text = ""
                self.fieldWage.text = ""
                self.fieldActive.text = ""


        clazz = CustomFrame()
