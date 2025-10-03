from typing import List, Any, Dict

import pandas as pd


def collect_votes(votes: List[Any]) -> Dict[Any, int]:
    res = {}
    for vote in votes:
        res[vote] = res.get(vote, 0) + 1
    return res

def majority_vote(voting_dict: Dict[Any, int], threshold: int) -> Any:
    for key, count in voting_dict.items():
        if count >= threshold:
            return key
    return None

def get_contested_filter(df: pd.DataFrame, voting_columns: List[str], majority_threshold: int) -> pd.Series:
    contested_filter = pd.Series([False] * len(df))
    for col in voting_columns:
        contested_filter |= df[col].apply(lambda votes: majority_vote(collect_votes(votes), majority_threshold) is None)
    return contested_filter
