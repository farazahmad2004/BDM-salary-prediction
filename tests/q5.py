OK_FORMAT = "ok"

test = {
    "name": "q5",
    "points": 2.5,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> import pandas as pd
                    >>> isinstance(avg_salary_industry, pd.Series)
                    True
                    """,
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": r"""
                    >>> len(avg_salary_industry) == 10
                    True
                    """,
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": r"""
                    >>> isinstance(highest_paid_industry, str)
                    True
                    """,
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": r"""
                    >>> highest_paid_industry == 'Education'
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