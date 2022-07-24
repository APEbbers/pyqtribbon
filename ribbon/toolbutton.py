import typing
from enum import IntEnum

from qtpy import QtWidgets, QtCore


class RibbonButtonStyle(IntEnum):
    """Button style, Small, Medium, or Large."""
    Small = 0
    Medium = 1
    Large = 2


class RibbonToolButton(QtWidgets.QToolButton):
    """Tool button that is showed in the ribbon."""
    _buttonStyle: RibbonButtonStyle
    _actions: typing.List[QtWidgets.QAction]

    _largeButtonIconSize = 64
    _mediumButtonIconSize = 48
    _smallButtonIconSize = 32

    def __init__(self, parent=None):
        """Create a new ribbon tool button.

        :param parent: The parent widget.
        """
        super().__init__(parent)
        self._actions = []

        # Styles
        self.setButtonStyle(RibbonButtonStyle.Large)
        self.setAutoRaise(True)
        self.setFocusPolicy(QtCore.Qt.NoFocus)

        # Connect signals
        self.triggered.connect(self.setDefaultAction)

    def setButtonStyle(self, style: RibbonButtonStyle):
        """Set the button style of the button.

        :param style: The button style of the button.
        """
        self._buttonStyle = style
        if style == RibbonButtonStyle.Small:
            height = self._smallButtonIconSize
            self.setIconSize(QtCore.QSize(height, height))
            self.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        elif style == RibbonButtonStyle.Medium:
            height = self._mediumButtonIconSize
            self.setIconSize(QtCore.QSize(height, height))
            self.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        elif style == RibbonButtonStyle.Large:
            height = self._largeButtonIconSize
            self.setIconSize(QtCore.QSize(height, height))
            self.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)

    def setMenu(self, menu: QtWidgets.QMenu):
        """Set the menu of the button.

        :param menu: The menu of the button.
        """
        super().setMenu(menu)
        self.setPopupMode(QtWidgets.QToolButton.InstantPopup)
        if self.menu().actions():
            self.setDefaultAction(self.menu().actions()[0])

    def addAction(self, action: QtWidgets.QAction) -> None:
        """Add an action to the button.

        :param action: The action to add.
        """
        if len(self._actions) == 0:
            self.setDefaultAction(action)
            self.setMenu(QtWidgets.QMenu())
        self._actions.append(action)
        self.menu().addAction(action)

    def addActions(self, actions: typing.Iterable[QtWidgets.QAction]) -> None:
        """Add actions to the button.

        :param actions: The actions to add.
        """
        for action in actions:
            self.addAction(action)
