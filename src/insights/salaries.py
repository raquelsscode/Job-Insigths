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
     if not float(str(job["min_salary"])).is_integer() or not float(str(job["max_salary"])).is_integer():
    #   Seção 2 do site: https://www.techiedelight.com/pt/check-variable-integer-python/#:~:text=Usando%20int()%20fun%C3%A7%C3%A3o&text=A%20fun%C3%A7%C3%A3o%20int(x)%20converte,x)%20%3D%3D%20x%20ser%C3%A1%20verdade.&text=Isso%20%C3%A9%20tudo%20sobre%20determinar,inteiro%20ou%20n%C3%A3o%20em%20Python.
      raise ValueError("min_salary or max_salary aren't valid integers")
     if job["min_salary"] > job["max_salary"]:
      raise ValueError("min_salary is greather than max_salary")
     if not float(str(salary)).is_integer():
      raise ValueError("salary isn't a valid integer")
     
     return int(job["min_salary"]) <= int(salary) <= int(job["max_salary"])


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
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
    raise NotImplementedError
