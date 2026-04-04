OK_FORMAT = "ok"

test = {
    "name": "q1",
    "points": 2.5,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> import pandas as pd
                    >>> isinstance(df, pd.DataFrame)
                    True
                    """,
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": r"""
                    >>> len(df) == 250000
                    True
                    """,
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": r"""
                    >>> required_cols = {"job_title", "experience_years", "education_level", "skills_count", "industry", "company_size", "location", "remote_work", "certifications", "salary"}
                    >>> required_cols.issubset(set(df.columns))
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