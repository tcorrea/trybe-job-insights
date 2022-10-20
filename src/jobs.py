from functools import lru_cache
import csv


@lru_cache
def read(path: str) -> list[dict]:
    """Reads a file from a given path and returns its contents

    Parameters
    ----------
    path : str
        Full path to file

    Returns
    -------
    list
        List of rows as dicts
    """

    with open(path, encoding="utf-8") as file:
        jobs = csv.reader(file, delimiter=",", quotechar='"')
        head, *tail = jobs

    # usando list comprehension
    return [dict(zip(head, job)) for job in tail]

    # usando for
    # result = list()

    # for job in tail:
    #     result.append(dict(zip(head, job)))

    # return result
