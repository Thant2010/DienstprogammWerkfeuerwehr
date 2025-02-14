from PyQt6.QtWidgets import QHBoxLayout, QGridLayout

from elementsGui.inputWidgets.checkableComboBox import CheckableComboBox
from elementsGui.labels.captionLabel import CaptionLabel
from globals import reportSender, externalUnits
from utilityClasses.customMessageBox import CustomMessageBox


class InputRespondingUnitsRow(QGridLayout):

    def __init__(self):
        super().__init__()

        captionInternal = CaptionLabel("Einsatzkräfte intern")
        captionExternal = CaptionLabel("Einsatzkräfte extern")
        self.__inputInternalUnitsComboBox = CheckableComboBox(comboList=reportSender)
        self.__inputExternalUntisComboBox = CheckableComboBox(comboList=externalUnits)

        self.addWidget(captionInternal, 0, 0)
        self.addWidget(self.__inputInternalUnitsComboBox, 0, 1)
        self.addWidget(captionExternal, 1, 0)
        self.addWidget(self.__inputExternalUntisComboBox, 1, 1)

    def getValue(self):
        """
        Return a List of Checked Values
        :return:
        internal Units, external Units
        """
        internal = self.__inputInternalUnitsComboBox.getCheckedText()
        external = self.__inputExternalUntisComboBox.getCheckedText()

        if len(internal) == 0 and len(external) == 0:
            CustomMessageBox().showInfoMessage("Achtung",
                                             "Bitte mindestens 1 Einheit anwählen zum speichern")
            return None, None
        else:
            return internal, external