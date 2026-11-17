
"""The alert rule: decided before the incident (Week 12, Part 4)."""


def alert(psi_history, warn=0.10, act=0.25, windows=2):
    """Look at the last `windows` PSI values. ACT or WARN only if ALL of them are at or above the level."""

    last = psi_history[-windows:]

    if len(last) == windows and all(v >= act for v in last):
        return "ACT: retrain candidate"

    elif len(last) == windows and all(v >= warn for v in last):
        return "WARN: investigate"

    else:
        return "ok"
