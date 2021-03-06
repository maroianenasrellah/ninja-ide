from unittest import mock
from ninja_ide.gui.editor import editor
from ninja_ide.gui.editor import neditable
from ninja_ide.core.file_handling import nfile
from ninja_ide.gui.ide import IDE

IDE.register_service("ide", mock.Mock())


def create_editor(language=None):
    nfile_ref = nfile.NFile()
    neditable_ref = neditable.NEditable(nfile_ref)
    editor_ref = editor.create_editor(neditable_ref)
    return editor_ref
