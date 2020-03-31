from typing import List, Dict

import requests
from requests import Response


class SocrataFetcher:
    """
    For fetching from Socrata per API documented here
    (https://dev.socrata.com/foundry/data.sfgov.org/jjew-r69b)
    """

    def __init__(self, base_url: str):
        self._base_url: str = base_url
        self.offset_counter: int = 0
        self._query_criteria: List[str] = [f"$offset={self.offset_counter}"]

    def fetch_next_results(self) -> List[Dict]:
        url: str = self._base_url + self._get_query_criteria()

        response: Response = requests.get(url)
        if response.status_code == 200:
            data: List[Dict] = response.json()
        else:
            raise ValueError(
                f"The Sorcrata query returned {response.status_code}: {response.reason}."
            )

        self._update_offset(increment_to_increase_offset=len(data))

        return data

    def _get_query_criteria(self) -> str:
        return "&".join(self._query_criteria)

    def _update_offset(self, increment_to_increase_offset: int) -> None:
        self.offset_counter += increment_to_increase_offset
        for i, criterion in enumerate(self._query_criteria):
            # since the offset is initialized as the first member of the criteria list,
            # this should be O(1) (but would be O(n) if placed last in a list of n elements),
            # I set it up this way in the case the list ordering is not like this in the future
            # I would be happy to improve this method based on your feedback
            if criterion.startswith("$offset"):
                self._query_criteria[i] = f"$offset={self.offset_counter}"
                return
        raise ValueError("No offset criteria was found to update.")

    def add_limit(self, number_of_results_per_query: int) -> None:
        self._append_to_query_criteria(f"$limit={number_of_results_per_query}")

    def add_order(self, field_to_sort: str) -> None:
        self._append_to_query_criteria(f"$order={field_to_sort}")

    def add_dayorder_filter(self, iso_weekday: int) -> None:
        """
        Must be provided in agreement with ISO weekday
        https://docs.python.org/3.7/library/datetime.html#datetime.date.isoweekday
        """
        self._append_to_query_criteria(f"dayorder={iso_weekday}")

    def add_time_filter(self, time_in_24_hour_format: str) -> None:
        """
        The opening time must before or exactly the same as the current time.
        The closing time must be after or exactly the same as the current time.
        """
        self._append_to_query_criteria(
            f"$where=start24 <= '{time_in_24_hour_format}' AND end24 >= '{time_in_24_hour_format}'"
        )

    def _append_to_query_criteria(self, text: str) -> None:
        if text:
            # to cover the whole domain of strings, I've ensured that empty string is handled
            # other verification could be performed to check
            # if the string represent a valid database query
            # this would become especially important the strings were to be provided by users
            self._query_criteria.append(text)
