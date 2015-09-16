"""Script for preparing the html output of the Sphinx documentation system for
github pages. """

from sys import version as pythonversion

VERSION = (1, 1, 0, 'dev')

__version__ = ".".join(map(str, VERSION[:-1]))
__release__ = ".".join(map(str, VERSION))
__author__ = "Michael Jones"
__contact__ = "http://github.com/michaeljones"
__homepage__ = "http://github.com/michaeljones/sphinx-to-github"
__docformat__ = "restructuredtext"


if pythonversion < '3':
    from sphinxtogithub import (
        setup,
        sphinx_extension,
        LayoutFactory,
        Layout,
        DirectoryHandler,
        VerboseRename,
        ForceRename,
        Remover,
        FileHandler,
        Replacer,
        DirHelper,
        FileSystemHelper,
        OperationsFactory,
        HandlerFactory
    )

else:
    from sphinxtogithub.sphinxtogithub import (
        setup,
        sphinx_extension,
        LayoutFactory,
        Layout,
        DirectoryHandler,
        VerboseRename,
        ForceRename,
        Remover,
        FileHandler,
        Replacer,
        DirHelper,
        FileSystemHelper,
        OperationsFactory,
        HandlerFactory
    )

