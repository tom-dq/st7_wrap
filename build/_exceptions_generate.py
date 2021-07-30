"""This is the code to generate the exceptions from the Strand7 API, which is in st7_wrap as exc.py"""


import ctypes
import textwrap
import typing


import St7API

_BASE_EXCEPTION_NAME = "St7BaseException"
_ERR_DICT = "_err_dict"
_SOLVER_TERM_DICT = "_solver_term_dict"

def __make_base_exception() -> typing.Iterable[str]:
    yield f"class {_BASE_EXCEPTION_NAME}(BaseException):"
    yield '    """Base class for all ERR7_ and SE_ errors"""'
    yield "    "
    yield "    def __repr__(self):"
    yield '        return f"{self.__class__.__name__}()"'
    yield "    "
    yield "    def __str__(self):"
    yield '        return f"{self.__class__.__name__}: {self.__doc__}"'
    yield ""
    yield ""


def __make_fallback_exception() -> typing.Iterable[str]:
    yield f"class St7UnknownException({_BASE_EXCEPTION_NAME}):"
    yield '    """Unknown St7 Error"""'
    yield "    pass"
    yield ""
    yield ""


def __make_one_exception(error_name: str, description_override: typing.Optional[str]=None) -> typing.Iterable[str]:
    """Write out the code for a native Python version of a Strand7 error code.
    To be pasted into the top if this file if it's changed."""

    iErr = getattr(St7API, error_name)

    def get_description() -> str:

        if description_override:
            return description_override

        sb = ctypes.create_string_buffer(St7API.kMaxStrLen)

        # Try API error code first
        api_iErr = St7API.St7GetAPIErrorString(iErr, sb, St7API.kMaxStrLen)
        if api_iErr == 0:
            return sb.value.decode()

        # Otherwise, try the solver error code
        solver_iErr = St7API.St7GetSolverErrorString(iErr, sb, St7API.kMaxStrLen)
        if solver_iErr == 0:
            return sb.value.decode()

        # Fallback - shouldn't happen!
        return f"Unknown Strand7 error {error_name} ({iErr})"

    yield f"class {error_name}({_BASE_EXCEPTION_NAME}):"

    description_text = get_description()
    if len(description_text) <= 90:
        yield f'    """{description_text}"""'

    else:
        yield '    """'
        for desc_line in textwrap.wrap(description_text, width=100):
            yield f"    {desc_line}"
        yield '    """'

    yield "    pass"


def __make_exceptions(error_names, should_override_description):
    # Sort alphabetically for the exception classes
    error_names.sort()
    for error_name in error_names:
        description_override = error_name if should_override_description else None
        yield from __make_one_exception(error_name, description_override=description_override)


def __make_exception_lookup_dict(error_names, dict_name):
    # Make the error lookup dictionary (in order of error code integer)
    error_names.sort(key=lambda error_name: getattr(St7API, error_name))
    yield f"{dict_name} = {{"
    for error_name in error_names:
        yield f"    {getattr(St7API, error_name)}: {error_name},"
    yield "}"



def __make_all_exceptions() -> typing.Iterable[str]:
    yield from __make_base_exception()
    yield from __make_fallback_exception()

    error_names = [err for err in dir(St7API) if err.startswith("ERR7_") or err.startswith("SE_")]
    term_code_names = [st_name for st_name in dir(St7API) if st_name.startswith("ST_")]

    yield from __make_exceptions(error_names, False)
    yield from __make_exceptions(term_code_names, True)

    yield from __make_exception_lookup_dict(error_names, _ERR_DICT)
    yield from __make_exception_lookup_dict(term_code_names, _SOLVER_TERM_DICT)
    

def __make_chk(func_name, dict_name) -> typing.Iterable[str]:
    chk_func = f'''def {func_name}(iErr: int):
    """Checks a Strand7 error code and raised an exception which inherits from
       {_BASE_EXCEPTION_NAME} if an error code was returned."""
    
    if iErr == 0:
        return

    exc = {dict_name}.get(iErr, St7UnknownException)

    raise exc()
    '''

    yield from chk_func.splitlines()



def __make_module() -> typing.Iterable[str]:

    yield '"""Exceptions auto-generated from error codes in St7API.py by _exceptions_generate.py"""'
    yield ""
    yield ""
    yield from __make_all_exceptions()
    yield ""
    yield ""
    yield from __make_chk("chk", _ERR_DICT)
    yield ""
    yield from __make_chk("chk_st", _SOLVER_TERM_DICT)
    yield ""


if __name__ == "__main__":
    for line in __make_module():
        print(line)
