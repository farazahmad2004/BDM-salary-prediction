OK_FORMAT = "ok"

test = {
    "name": "q14",
    "points": 2.5,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> 'X_train' in globals() and 'X_test' in globals() and 'y_train' in globals() and 'y_test' in globals()
                    True
                    """,
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": r"""
                    >>> import pandas as pd
                    >>> bool(isinstance(X_train, pd.DataFrame) and isinstance(X_test, pd.DataFrame))
                    True
                    """,
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": r"""
                    >>> bool(isinstance(y_train, pd.Series) and isinstance(y_test, pd.Series))
                    True
                    """,
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": r"""
                    >>> total = len(X_train) + len(X_test)
                    >>> frac = len(X_train) / total
                    >>> bool(abs(frac - 0.8) < 0.05)
                    True
                    """,
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": r"""
                    >>> total = len(X_train) + len(X_test)
                    >>> frac = len(X_test) / total
                    >>> bool(abs(frac - 0.2) < 0.05)
                    True
                    """,
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": r"""
                    >>> bool(set(X_train.index).isdisjoint(set(X_test.index)))
                    True
                    """,
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": r"""
                    >>> bool(len(X_train) == len(y_train) and len(X_test) == len(y_test))
                    True
                    """,
                    "hidden": False,
                    "locked": False
                }
            ],
            "scored": True,
            "setup": "",
            "teardown": "",
            "type": "doctest"
        }
    ]
}