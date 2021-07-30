"""This is the code to generate the exceptions from the Strand7 API, which is in st7_wrap as exc.py"""


import ctypes
import textwrap
import typing


import St7API

_BASE_EXCEPTION_NAME = "St7BaseException"


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


def __make_one_exception(error_name: str) -> typing.Iterable[str]:
    """Write out the code for a native Python version of a Strand7 error code.
    To be pasted into the top if this file if it's changed."""

    iErr = getattr(St7API, error_name)

    def get_description() -> str:
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
    yield ""
    yield ""


def __make_all_exceptions() -> typing.Iterable[str]:
    yield from __make_base_exception()

    error_names = [err for err in dir(St7API) if err.startswith("ERR7_") or err.startswith("SE_")]

    # Sort alphabetically for the exception classes
    error_names.sort()
    for error_name in error_names:
        yield from __make_one_exception(error_name)

    yield from __make_fallback_exception()

    # Make the error lookup dictionary (in order of error code integer)
    error_names.sort(key=lambda error_name: getattr(St7API, error_name))
    yield "_err_dict = {"
    for error_name in error_names:
        yield f"    {getattr(St7API, error_name)}: {error_name},"
    yield "}"


def __make_chk() -> typing.Iterable[str]:
    chk_func = f'''def chk(iErr: int):
    """Checks a Strand7 error code and raised an exception which inherits from
       {_BASE_EXCEPTION_NAME} if an error code was returned."""
    
    if iErr == 0:
        return

    exc = _err_dict.get(iErr, St7UnknownException)

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
    yield from __make_chk()
    yield ""


if __name__ == "__main__":
    for line in __make_module():
        print(line)
