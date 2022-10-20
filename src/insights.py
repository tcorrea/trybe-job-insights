from src.jobs import read

# from jobs import read


def get_unique_job_types(path: str) -> list[str]:
    """Checks all different job types and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique job types
    """
    jobs: list[dict] = read(path)
    # {} set -> elementos unicos
    # job["job_type"] -> chave que o requisito pede
    # list() -> converte para lista
    return list({job["job_type"] for job in jobs if job["job_type"]})


def filter_by_job_type(jobs: list[dict], job_type: str) -> list[dict]:
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    return [job for job in jobs if job["job_type"] == job_type]


def get_unique_industries(path: str) -> list[str]:
    """Checks all different industries and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique industries
    """
    jobs: list[dict] = read(path)
    # {} set -> elementos unicos
    # job["job_type"] -> chave que o requisito pede
    # list() -> converte para lista
    return list({job["industry"] for job in jobs if job["industry"]})


def filter_by_industry(jobs: list[dict], industry: str) -> list[dict]:
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    return [job for job in jobs if job["industry"] == industry]


def get_max_salary(path: str) -> int:
    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """
    jobs: list[dict] = read(path)
    # todos os salarios convertidos para int
    salaries: list[int] = [
        int(job["max_salary"])
        for job in jobs
        if job["max_salary"] and job["max_salary"] != "invalid"
    ]
    max_salary: int = max(salaries)
    return max_salary


def get_min_salary(path) -> int:
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    jobs: list[dict] = read(path)
    # todos os salarios convertidos para int
    salaries: list[int] = [
        int(job["min_salary"])
        for job in jobs
        if job["min_salary"] and job["min_salary"] != "invalid"
    ]
    min_salary: int = min(salaries)
    return min_salary


def matches_salary_range(job: dict, salary: int) -> bool:
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError("min_salary or max_salary doesn't exists")
    elif not isinstance(job["min_salary"], int) or not isinstance(
        job["max_salary"], int
    ):
        raise ValueError("aren't valid integers")
    elif job["min_salary"] > job["max_salary"]:
        raise ValueError("min_salary is greathe than max_salary")
    elif not isinstance(salary, int):
        raise ValueError("salary isn't a valid integer")

    return job["min_salary"] <= salary <= job["max_salary"]


def filter_by_salary_range(jobs: list[dict], salary: int) -> list[dict]:
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    found_jobs = list()

    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                found_jobs.append(job)
        except ValueError:
            pass

    return found_jobs
