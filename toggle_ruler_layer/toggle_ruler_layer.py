from krita import Krita, Extension

from PyQt5.QtWidgets import QWidget, QToolButton

# these three functions courtesy of AkiR https://krita-artists.org/t/discovering-which-toolbox-tool-is-active/10580/2
def find_tool_box(qwindow):
    for qobj in qwindow.findChildren(QWidget):
        if qobj.metaObject().className() == "KoToolBox":
            return qobj

def find_active_tool(qtoolbox):
    for qobj in qtoolbox.findChildren(QToolButton):
        if qobj.metaObject().className() == "KoToolBoxButton":
            if qobj.isChecked():
                return qobj

def find_my_current_tool():
    app = Krita.instance()
    qwindow = app.activeWindow().qwindow()
    tool_box = find_tool_box(qwindow)
    tool = find_active_tool(tool_box)
    return tool

# tool = find_my_current_tool()
# name = tool.objectName()
# checked = tool.isChecked()
# print("tool: {tool}, tool.objectName: {name}, checked: {checked}".format(**locals()))

class ToggleRulerLayer(Extension):

    def __init__(self, parent):
        super().__init__(parent)

    def activeTool(self):
       print("active tool is zoom")

    def setup(self):
        pass

    previousToolName = None

    def toggleRulerLayer(self):
        app = Krita.instance()
        doc = app.activeDocument()        

        currentLayer = doc.activeNode()
        rulerLayer   = doc.nodeByName("Ruler")        

        if rulerLayer.name() == "Ruler": # `nodeByName` returns an unnamed node if it couldn't find the one you asked for, not None?
            if currentLayer == rulerLayer:
                app.action('switchToPreviouslyActiveNode').trigger()
                if self.previousToolName:
                    app.action(self.previousToolName).trigger()
                else:
                    app.action('KritaShape/KisToolBrush').trigger()
            else:
                self.previousToolName = find_my_current_tool().objectName()
                doc.setActiveNode(rulerLayer)
                app.action('KisToolTransform').trigger()

    def createActions(self, window):
        action = window.createAction("toggleRulerLayer", "Toggle Ruler Layer", "tools/scripts")
        action.triggered.connect(self.toggleRulerLayer)

Krita.instance().addExtension(ToggleRulerLayer(Krita.instance()))
