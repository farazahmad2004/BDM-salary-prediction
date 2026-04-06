OK_FORMAT = "ok"

test = {
    "name": "q18",
    "points": 2.5,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> 'log_reg' in globals() and 'accuracy' in globals()
                    True
                    """,
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": r"""
                    >>> type(log_reg).__name__ == 'LogisticRegression'
                    True
                    """,
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": r"""
                    >>> bool(set(y_train_binary.unique()).issubset({0, 1}))
                    True
                    """,
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": r"""
                    >>> bool(0.9 < accuracy <= 1.0)
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