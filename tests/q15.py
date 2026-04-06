OK_FORMAT = "ok"

test = {
    "name": "q15",
    "points": 2.5,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> bool(abs(X_train['experience_years'].mean()) < 0.1)
                    True
                    """,
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": r"""
                    >>> bool(abs(X_train['skills_count'].std() - 1.0) < 0.1)
                    True
                    """,
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": r"""
                    >>> bool(abs(X_train['certifications'].mean()) < 0.1)
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