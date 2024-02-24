import argparse
import glob
import logging
import os
import random

logging.basicConfig(level=logging.INFO)


def arguments() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', help='Name of the city config to load')
    parser.add_argument(
                            '--results',
                            help='How many options to return',
                            default=1,
                            type=int
                        )
    return parser.parse_args()


def get_random_results(required_results: int, target_list: list) -> list:
    choices = []
    for required_result in range(0, required_results):
        choice = random.choice(target_list)
        logging.debug(f"Random choice {required_result}: {choice}")
        choices.append(choice)
        target_list.remove(choice)
    return choices


def join_list(list1: list, list2: list) -> list:
    final_list = list1 + list2
    return final_list


def read_all_files() -> list:
    restaurants = []
    file_list = glob.glob(os.path.join(os.getcwd(), "cfg", "*.cfg"))
    for file in file_list:
        logging.debug(f'Pulling restaurant list for {file}')
        temp_list = read_file_to_list(file)
        logging.debug(temp_list)
        restaurants = join_list(restaurants, temp_list)
    return restaurants


def read_file_to_list(file):
    with open(file) as open_file:
        data = open_file.read()
    target_list = data.split('\n')
    target_list.remove('')
    logging.debug(f'List read from {file}\n' + str(target_list))
    return target_list


def main():
    args = arguments()
    restaurants = []
    if args.config:
        restaurants = read_file_to_list(f'cfg/{args.config}.cfg')
    else:
        restaurants = read_all_files()
    logging.info('list of restaurants:\n' + str(restaurants))
    choices = get_random_results(args.results, restaurants)
    logging.info('random choices:\n' + str(choices))


if __name__ == '__main__':
    main()
