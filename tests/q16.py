OK_FORMAT = "ok"

test = {
    "name": "q16",
    "points": 2.5,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> 'regression_model' in globals() and 'y_pred' in globals()
                    True
                    """,
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": r"""
                    >>> type(regression_model).__name__ == 'LinearRegression'
                    True
                    """,
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": r"""
                    >>> 'rmse' in globals() and 'r2' in globals()
                    True
                    """,
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": r"""
                    >>> bool(7800 < rmse < 7950)
                    True
                    """,
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": r"""
                    >>> bool(0.90 < r2 < 1.0)
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