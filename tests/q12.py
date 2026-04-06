OK_FORMAT = "ok"

test = {
    "name": "q12",
    "points": 2.5,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> import pandas as pd
                    >>> df['education_level'].dtype.kind in ['i', 'f', 'u']
                    True
                    """,
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": r"""
                    >>> df['company_size'].dtype.kind in ['i', 'f', 'u']
                    True
                    """,
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": r"""
                    >>> set(df['education_level'].dropna().unique()).issubset({0, 1, 2, 3, 4})
                    True
                    """,
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": r"""
                    >>> set(df['company_size'].dropna().unique()).issubset({0, 1, 2, 3, 4})
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