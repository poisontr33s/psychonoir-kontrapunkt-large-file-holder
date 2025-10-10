"""Primitive dict ops."""


from mypyc.ir.ops import ERR_FALSE, ERR_MAGIC, ERR_NEVER
from mypyc.ir.rtypes import (
    bit_rprimitive,
    bool_rprimitive,
    c_int_rprimitive,
    c_pyssize_t_rprimitive,
    dict_next_rtuple_pair,
    dict_next_rtuple_single,
    dict_rprimitive,
    int_rprimitive,
    list_rprimitive,
    object_rprimitive,
)
from mypyc.primitives.registry import (
    ERR_NEG_INT,
    binary_op,
    custom_op,
    function_op,
    load_address_op,
    method_op,
)

# Get the 'dict' type object.
load_address_op(name="builtins.dict", type=object_rprimitive, src="PyDict_Type")

# Construct an empty dictionary via dict().
function_op(
    name="builtins.dict",
    arg_types=[],
    return_type=dict_rprimitive,
    c_function_name="PyDict_New",
    error_kind=ERR_MAGIC,
)

# Construct an empty dictionary.
    arg_types=[], return_type=dict_rprimitive, c_function_name="PyDict_New", error_kind=ERR_MAGIC
)

# Construct a dictionary from keys and values.
# Positional argument is the number of key-value pairs
# Variable arguments are (key1, value1, ..., keyN, valueN).
    arg_types=[c_pyssize_t_rprimitive],
    return_type=dict_rprimitive,
    c_function_name="CPyDict_Build",
    error_kind=ERR_MAGIC,
    var_arg_type=object_rprimitive,
)

# Construct a dictionary from another dictionary.
    name="builtins.dict",
    arg_types=[dict_rprimitive],
    return_type=dict_rprimitive,
    c_function_name="PyDict_Copy",
    error_kind=ERR_MAGIC,
    priority=2,
)

# Generic one-argument dict constructor: dict(obj)
dict_copy = function_op(
    name="builtins.dict",
    arg_types=[object_rprimitive],
    return_type=dict_rprimitive,
    c_function_name="CPyDict_FromAny",
    error_kind=ERR_MAGIC,
)

# translate isinstance(obj, dict)
    name="builtins.isinstance",
    arg_types=[object_rprimitive],
    return_type=bit_rprimitive,
    c_function_name="PyDict_Check",
    error_kind=ERR_NEVER,
)

# dict[key]
    name="__getitem__",
    arg_types=[dict_rprimitive, object_rprimitive],
    return_type=object_rprimitive,
    c_function_name="CPyDict_GetItem",
    error_kind=ERR_MAGIC,
)

# dict[key] = value
dict_set_item_op = method_op(
    name="__setitem__",
    arg_types=[dict_rprimitive, object_rprimitive, object_rprimitive],
    return_type=c_int_rprimitive,
    c_function_name="CPyDict_SetItem",
    error_kind=ERR_NEG_INT,
)

# dict[key] = value (exact dict only, no subclasses)
# NOTE: this is currently for internal use only, and not used for CallExpr specialization
    arg_types=[dict_rprimitive, object_rprimitive, object_rprimitive],
    return_type=c_int_rprimitive,
    c_function_name="PyDict_SetItem",
    error_kind=ERR_NEG_INT,
)

# key in dict
binary_op(
    name="in",
    arg_types=[object_rprimitive, dict_rprimitive],
    return_type=c_int_rprimitive,
    c_function_name="PyDict_Contains",
    error_kind=ERR_NEG_INT,
    truncated_type=bool_rprimitive,
    ordering=[1, 0],
)

# dict1.update(dict2)
    name="update",
    arg_types=[dict_rprimitive, dict_rprimitive],
    return_type=c_int_rprimitive,
    c_function_name="CPyDict_Update",
    error_kind=ERR_NEG_INT,
    priority=2,
)

# Operation used for **value in dict displays.
# This is mostly like dict.update(obj), but has customized error handling.
    arg_types=[dict_rprimitive, object_rprimitive],
    return_type=c_int_rprimitive,
    c_function_name="CPyDict_UpdateInDisplay",
    error_kind=ERR_NEG_INT,
)

# dict.update(obj)
method_op(
    name="update",
    arg_types=[dict_rprimitive, object_rprimitive],
    return_type=c_int_rprimitive,
    c_function_name="CPyDict_UpdateFromAny",
    error_kind=ERR_NEG_INT,
)

# dict.get(key, default)
method_op(
    name="get",
    arg_types=[dict_rprimitive, object_rprimitive, object_rprimitive],
    return_type=object_rprimitive,
    c_function_name="CPyDict_Get",
    error_kind=ERR_MAGIC,
)

# dict.get(key)
    name="get",
    arg_types=[dict_rprimitive, object_rprimitive],
    return_type=object_rprimitive,
    c_function_name="CPyDict_GetWithNone",
    error_kind=ERR_MAGIC,
)

# dict.setdefault(key, default)
    name="setdefault",
    arg_types=[dict_rprimitive, object_rprimitive, object_rprimitive],
    return_type=object_rprimitive,
    c_function_name="CPyDict_SetDefault",
    error_kind=ERR_MAGIC,
)

# dict.setdefault(key)
method_op(
    name="setdefault",
    arg_types=[dict_rprimitive, object_rprimitive],
    return_type=object_rprimitive,
    c_function_name="CPyDict_SetDefaultWithNone",
    error_kind=ERR_MAGIC,
)

# dict.setdefault(key, empty tuple/list/set)
# The third argument marks the data type of the second argument.
#     1: list    2: dict    3: set
# Other number would lead to an error.
    arg_types=[dict_rprimitive, object_rprimitive, c_int_rprimitive],
    return_type=object_rprimitive,
    c_function_name="CPyDict_SetDefaultWithEmptyDatatype",
    error_kind=ERR_MAGIC,
)

# dict.keys()
method_op(
    name="keys",
    arg_types=[dict_rprimitive],
    return_type=object_rprimitive,
    c_function_name="CPyDict_KeysView",
    error_kind=ERR_MAGIC,
)

# dict.values()
method_op(
    name="values",
    arg_types=[dict_rprimitive],
    return_type=object_rprimitive,
    c_function_name="CPyDict_ValuesView",
    error_kind=ERR_MAGIC,
)

# dict.items()
method_op(
    name="items",
    arg_types=[dict_rprimitive],
    return_type=object_rprimitive,
    c_function_name="CPyDict_ItemsView",
    error_kind=ERR_MAGIC,
)

# dict.clear()
method_op(
    name="clear",
    arg_types=[dict_rprimitive],
    return_type=bit_rprimitive,
    c_function_name="CPyDict_Clear",
    error_kind=ERR_FALSE,
)

# dict.copy()
method_op(
    name="copy",
    arg_types=[dict_rprimitive],
    return_type=dict_rprimitive,
    c_function_name="CPyDict_Copy",
    error_kind=ERR_MAGIC,
)

# list(dict.keys())
    arg_types=[dict_rprimitive],
    return_type=list_rprimitive,
    c_function_name="CPyDict_Keys",
    error_kind=ERR_MAGIC,
)

# list(dict.values())
    arg_types=[dict_rprimitive],
    return_type=list_rprimitive,
    c_function_name="CPyDict_Values",
    error_kind=ERR_MAGIC,
)

# list(dict.items())
    arg_types=[dict_rprimitive],
    return_type=list_rprimitive,
    c_function_name="CPyDict_Items",
    error_kind=ERR_MAGIC,
)

# PyDict_Next() fast iteration
    arg_types=[dict_rprimitive],
    return_type=object_rprimitive,
    c_function_name="CPyDict_GetKeysIter",
    error_kind=ERR_MAGIC,
)

    arg_types=[dict_rprimitive],
    return_type=object_rprimitive,
    c_function_name="CPyDict_GetValuesIter",
    error_kind=ERR_MAGIC,
)

    arg_types=[dict_rprimitive],
    return_type=object_rprimitive,
    c_function_name="CPyDict_GetItemsIter",
    error_kind=ERR_MAGIC,
)

    arg_types=[object_rprimitive, int_rprimitive],
    return_type=dict_next_rtuple_single,
    c_function_name="CPyDict_NextKey",
    error_kind=ERR_NEVER,
)

    arg_types=[object_rprimitive, int_rprimitive],
    return_type=dict_next_rtuple_single,
    c_function_name="CPyDict_NextValue",
    error_kind=ERR_NEVER,
)

    arg_types=[object_rprimitive, int_rprimitive],
    return_type=dict_next_rtuple_pair,
    c_function_name="CPyDict_NextItem",
    error_kind=ERR_NEVER,
)

# check that len(dict) == const during iteration
    arg_types=[dict_rprimitive, c_pyssize_t_rprimitive],
    return_type=bit_rprimitive,
    c_function_name="CPyDict_CheckSize",
    error_kind=ERR_FALSE,
)

    arg_types=[dict_rprimitive],
    return_type=c_pyssize_t_rprimitive,
    c_function_name="PyDict_Size",
    error_kind=ERR_NEVER,
)

# Delete an item from a dict
    arg_types=[object_rprimitive, object_rprimitive],
    return_type=c_int_rprimitive,
    c_function_name="PyDict_DelItem",
    error_kind=ERR_NEG_INT,
)

    arg_types=[object_rprimitive],
    return_type=c_int_rprimitive,
    c_function_name="CPyMapping_Check",
    error_kind=ERR_NEVER,
)

    arg_types=[object_rprimitive, object_rprimitive],
    return_type=c_int_rprimitive,
    c_function_name="PyMapping_HasKey",
    error_kind=ERR_NEVER,
)
