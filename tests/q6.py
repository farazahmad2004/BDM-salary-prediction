OK_FORMAT = "ok"

test = {
    "name": "q6",
    "points": 2.5,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> isinstance(common_edu_level, str)
                    True
                    """,
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": r"""
                    >>> common_edu_level == 'Master'
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