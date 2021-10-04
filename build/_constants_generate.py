"""Python Enum versions of some Strand7 constants. This script uses the Strand7 API to create const.py"""


import typing
import collections

import St7API


class ConstMeta(typing.NamedTuple):
    name: str  # What the class is going to be called
    example_member: str  # Any member of the enum.


_all_const_meta = [
    ConstMeta("Entity", "tyNODE"),
    ConstMeta("Property", "ptBEAMPROP"),
    ConstMeta("SolverType", "stLinearStatic"),
    ConstMeta("SolverMode", "smNormalRun"),
    ConstMeta("PreLoadType", "plPlatePreStrain"),
    ConstMeta("NodeResultType", "rtNodeDisp"),
    ConstMeta("PlateResultType", "rtPlateStress"),
    ConstMeta("PlateResultSubType", "stPlateLocal"),
    ConstMeta("SampleLocation", "spCentroid"),
    ConstMeta("PlateSurface", "psPlateMidPlane"),
    ConstMeta("SolverDefaultLogical", "spDoSturm"),
    ConstMeta("SolverDefaultInteger", "spTreeStartNumber"),
    ConstMeta("TableType", "ttVsTime"),
    ConstMeta("BeamContour", "ctBeamNone"),
    ConstMeta("PlateContour", "ctPlateNone"),
    ConstMeta("BrickContour", "ctBrickNone"),
    ConstMeta("AttributeType", "aoRestraint"),
    ConstMeta("ImageType", "itBitmap8Bit"),
    ConstMeta("ScaleType", "dsPercent"),
    ConstMeta("GlobalInteger", "ivAttachmentsCreated"),
    ConstMeta("WindowsRefreshMode", "wrAutoRefresh"),
]


def _parse_constants():
    """Read the code in St7API and parse out the constants."""

    def is_int(x):
        try:
            _ = int(x)
            return True

        except ValueError:
            return False

    with open(St7API.__file__) as f_st7api:
        current_comment = None
        seen_comments = set()

        f_stripped = (l.strip() for l in f_st7api)
        for l in f_stripped:
            is_comment_line = l.startswith("#")
            is_blank_line = not l
            is_constant_line = "=" in l and is_int(l.split("=")[1])

            if is_comment_line:
                if l in seen_comments:
                    raise ValueError(f"Duplicate comment {l}")

            if is_comment_line:
                current_comment = l

            elif is_blank_line:
                current_comment = None

            elif is_constant_line:
                if current_comment:
                    name, val = [x.strip() for x in l.split("=")]
                    yield current_comment, name, val


def _no_dupe_value_sanity_check(header_to_constants):
    """Warn about repeated constants and remove them from the set we're working with.
    At the moment I haven't needed to deal with the likes of this:

        # Load Path Template Vehicle - Integers
        ipLPTVehicleInstance = 0
        ipLPTVehicleDirection = 1
        lpVehicleSingleLane = 0
        lpVehicleDoubleLane = 1
        lpVehicleForward = 0
        lpVehicleBackward = 1

    Perhaps one day I will, but in the meantime remove such cases from the working data."""

    clean_data = dict()

    for comment, names_and_vals in header_to_constants.items():
        val_to_names = collections.defaultdict(list)
        for name, val in names_and_vals:
            val_to_names[val].append(name)

        for val, name_list in val_to_names.items():
            if len(name_list) == 1:
                clean_data[comment] = names_and_vals

            else:
                # Don't do anything with this warning - could print / raise if debugging...
                warning = Warning(f"Got duplicate constants {name_list} = {val} under {comment}.")

    return clean_data


def _produce_one_enum(const_meta: ConstMeta, names_and_vals):
    yield f"class {const_meta.name}(enum.Enum):"
    for name, _ in names_and_vals:
        yield f"    {name} = St7API.{name}"

    yield ""
    yield ""


def produce_constants() -> typing.Iterable[str]:
    header_to_constants = collections.defaultdict(list)

    for current_comment, name, val in _parse_constants():
        header_to_constants[current_comment].append((name, val))

    # clean_headers_to_constants = _no_dupe_value_sanity_check(header_to_constants)
    clean_headers_to_constants = header_to_constants

    # Be able to lookup the section this is in.
    name_to_header = dict()
    for header, names_and_vals in clean_headers_to_constants.items():
        for name, val in names_and_vals:
            name_to_header[name] = header

    yield '"""Some curated enum types auto-generated from St7API.py by _constants_generate.py"""'
    yield ""
    yield "import enum"
    yield ""
    yield "import St7API"
    yield ""
    yield ""

    yield "__all__ = ["
    for const_meta in sorted(_all_const_meta):
        yield f'    "{const_meta.name}",'

    yield "]"
    yield ""

    for const_meta in sorted(_all_const_meta):
        header = name_to_header[const_meta.example_member]
        names_and_vals = clean_headers_to_constants[header]
        yield from _produce_one_enum(const_meta, names_and_vals)


if __name__ == "__main__":
    for s in produce_constants():
        print(s)
