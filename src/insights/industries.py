from typing import List, Dict
from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    jobs = read(path)

    industries = []
    for industry in jobs:
        if not industry["industry"] == '':
            industries.append(industry["industry"])
    return set(industries)


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    return [
        data for data in jobs
        if data['industry'] == industry
    ]
