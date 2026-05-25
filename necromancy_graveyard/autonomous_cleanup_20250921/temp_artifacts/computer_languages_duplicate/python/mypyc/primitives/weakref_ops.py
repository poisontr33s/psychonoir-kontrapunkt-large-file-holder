#!/usr/bin/env python3
#-*- coding: utf-8 -*-

from mypyc.ir.ops import ERR_MAGIC
from mypyc.ir.rtypes import object_rprimitive, pointer_rprimitive
from mypyc.primitives.registry import function_op

# Weakref operations

    name="weakref.ReferenceType",
    arg_types=[object_rprimitive],
    return_type=object_rprimitive,
    c_function_name="PyWeakref_NewRef",
    extra_int_constants=[(0, pointer_rprimitive)],
    error_kind=ERR_MAGIC,
)

    name="weakref.ReferenceType",
    arg_types=[object_rprimitive, object_rprimitive],
    return_type=object_rprimitive,
    c_function_name="PyWeakref_NewRef",
    error_kind=ERR_MAGIC,
)

    name="_weakref.proxy",
    arg_types=[object_rprimitive],
    return_type=object_rprimitive,
    c_function_name="PyWeakref_NewProxy",
    extra_int_constants=[(0, pointer_rprimitive)],
    error_kind=ERR_MAGIC,
)

    name="_weakref.proxy",
    arg_types=[object_rprimitive, object_rprimitive],
    # steals=[True, False],
    return_type=object_rprimitive,
    c_function_name="PyWeakref_NewProxy",
    error_kind=ERR_MAGIC,
)
