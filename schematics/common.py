from .compat import * # pylint: disable=redefined-builtin
from .compat import __all__ as compat_exports
from .util import module_exports, Constant


NATIVE    = Constant('NATIVE',     0)
PRIMITIVE = Constant('PRIMITIVE',  1)

DROP      = Constant('DROP',       0)
NONEMPTY  = Constant('NONEMPTY',   1)
NOT_NONE  = Constant('NOT_NONE',   2)
DEFAULT   = Constant('DEFAULT',   10)
ALL       = Constant('ALL',       99)


__all__ = module_exports(__name__) + compat_exports; __all__.append('module_exports')

