from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    with open(path) as file:
        jobs = csv.DictReader(file)

        all_jobs = []
        for row in jobs:
            all_jobs.append(row)
        return all_jobs


def get_unique_job_types(path: str) -> List[str]:
    jobs = read(path)

    job_types = []
    for job in jobs:
        job_types.append(job["job_type"])
    return set(job_types)


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    return [
        data for data in jobs
        if data['job_type'] == job_type
    ]
