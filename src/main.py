from datetime import datetime
from typing import List, Dict

from src.food_truck import FoodTruck
from src.socrata_fetcher import SocrataFetcher


def main() -> None:
    results_desired_per_page: int = 10
    # this input could also be read in from
    # additional command line input, from a JSON configuration file, or from a web form

    current_datetime: datetime = datetime.now()
    # times other than "now" could also be considered via user input like the above comment mentions

    # how the fetcher is configured could also be exposed to the user,
    # this link is one example of doing that
    # https://data.sfgov.org/Economy-and-Community/Mobile-Food-Schedule/jjew-r69b/data
    fetcher = SocrataFetcher(base_url="http://data.sfgov.org/resource/bbb8-hzi6.json?")
    fetcher.add_limit(number_of_results_per_query=results_desired_per_page)
    fetcher.add_order(field_to_sort="applicant")
    fetcher.add_dayorder_filter(iso_weekday=current_datetime.isoweekday())
    fetcher.add_time_filter(time_in_24_hour_format=current_datetime.strftime("%X")[:-3])
    # trimming off the last three characters removes the ':seconds'

    open_food_trucks: List[Dict] = fetcher.fetch_next_results()
    if open_food_trucks:
        print_header()
    while open_food_trucks:
        # this loop could be modified to tell the user if there were no trucks found at all
        # or if a query returned less than the amount of "results_desired_per_page"
        # could say that's all there are
        # currently it just prints them and exists, as the prompt suggests

        for food_truck_data in open_food_trucks:
            print_food_truck(FoodTruck(data=food_truck_data))

        input("\nPress enter to see if there are more...")
        # this message could be removed for the user to push enter unprompted,
        # but it seemed necessary to me to prompt the user to go through the pages of results
        # I would be happy to match additional requirements if specified

        open_food_trucks = fetcher.fetch_next_results()

    # if an error occurs
    # (like Socrata returning a code other than 200
    # or a code-breaking change during further development)
    # it will be exposed as a stack trace
    # this function could catch the error and display it differently,
    # re-throw as part of a larger application, etc., but I would prefer to decide
    # this after further clarification and collaboration with my, hopefully, future team


def print_header() -> None:
    print("NAME ADDRESS", end=" ")
    # this matches output format suggested in the take home prompt
    # a newline character could be allowed here
    # by allowing the default "end" character ("\n")


def print_food_truck(food_truck: FoodTruck) -> None:
    print(f"{food_truck.name} {food_truck.address}")
    # this matches the output format suggested in the take home prompt
    # other formatting is possible if, for example,
    # you wanted to label each name and address as such


if __name__ == "__main__":
    main()
