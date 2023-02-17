from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    jobs = read(path)
    return max([int(salary['max_salary']) for salary in jobs
                if (salary['max_salary']).isdigit()])


def get_min_salary(path: str) -> int:
    jobs = read(path)
    return min([int(salary['min_salary']) for salary in jobs
                if (salary['min_salary']).isdigit()])


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError("min_salary or max_salary doesn't exists")
    if (
       not float(str(job["min_salary"])).is_integer()
       or not float(str(job["max_salary"])).is_integer()):
        # Seção 2 do site: https://bityli.com/1HsaL
        raise ValueError("min_salary or max_salary aren't valid integers")
    if int(job["min_salary"]) > int(job["max_salary"]):
        raise ValueError("min_salary is greather than max_salary")
    if not str(salary).replace("-", "").isnumeric():
        raise ValueError("salary isn't a valid integer")

    return int(job["min_salary"]) <= int(salary) <= int(job["max_salary"])


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:
    jobs_list = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                jobs_list.append(job)
        except ValueError as exc:
            print(exc)
    return jobs_list
