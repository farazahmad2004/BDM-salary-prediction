OK_FORMAT = "ok"

test = {
    "name": "q13",
    "points": 2.5,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> import pandas as pd
                    >>> 'remote_work' not in df.columns
                    True
                    """,
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": r"""
                    >>> 'industry' not in df.columns and 'job_title' not in df.columns
                    True
                    """,
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": r"""
                    >>> df.select_dtypes(include=['object', 'category']).shape[1] == 0
                    True
                    """,
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": r"""
                    >>> any('_' in col for col in df.columns)
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