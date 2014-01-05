class ExpCurve(object):
    pass

FLUCTUATING = ExpCurve()
SLOW = ExpCurve()
MEDIUM_SLOW = ExpCurve()
MEDIUM_FAST = ExpCurve()
FAST = ExpCurve()
ERRATIC = ExpCurve()
NONE = ExpCurve()

def fromString(expString):
    if type(expString) != str:
        raise ValueError("Invalid input to expcurve.fromString()")
    expup = expString.upper().strip()
    if expup == 'ERRATIC':
        return ERRATIC
    elif expup == 'FAST':
        return FAST
    elif expup == 'MEDIUM_FAST':
        return MEDIUM_FAST
    elif expup == 'MEDIUM_SLOW':
        return MEDIUM_SLOW
    elif expup == 'SLOW':
        return SLOW
    elif expup == 'FLUCTUATING':
        return FLUCTUATING
    elif expup == 'NONE':
        return NONE
    else:
        raise ValueError("Invalid EXP curve "+expString)