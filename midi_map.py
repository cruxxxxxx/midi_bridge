import rtmidi.midiconstants as const
from bus_fx import Bus12
import math
import copy

def efx(i):
    return const.CONTROLLER_CHANGE + (i - 1)

def invert_val(val):
    return 127 - val

#EFX switch (0–63: OFF, 64–127: ON)
def efx_toggle(i):
    return [efx(i), 19, invert_val]

efx_ctrl_map = {
    1: 16,
    2: 17,
    3: 18,
    4: 80,
    5: 81,
    6: 82
}

def append_val(val):
    return val

def efx_ctrl(i, ctrl):
    return [efx(i), efx_ctrl_map[ctrl], append_val]

def efx_select(i, fx_type):
    return [efx(i), 83, fx_type]


m = {
    str([const.NOTE_ON, 48]): [
        efx_select(1, Bus12.Distortion), efx_toggle(1)
    ],

    str([const.NOTE_ON+9, 49]): [
        efx_select(2, Bus12.Scatter), efx_toggle(2)
    ],

    str([const.CONTROLLER_CHANGE, 16]): [
        efx_ctrl(1, 1)
    ],

    str([const.CONTROLLER_CHANGE, 9]): [
        efx_ctrl(2, 1)
    ]
}


def translate(event):
    key = str(event[0][0:2])
    val = event[0][2]

    if key in m.keys():
       events = m[key]
       cpy_events = copy.deepcopy(events)

       for each in cpy_events:
            if callable(each[2]):
                each[2] = each[2](val)

       return cpy_events

    else:
        return []