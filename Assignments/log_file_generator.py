#!/usr/bin/env python3


from random import randint, random, choice as pick

DEFAULT_LOG_FILE_SIZE = 5000
DEFAULT_LOG_FILE = "access.log"

DEFAULT_IP_POOL_SIZE = 64
DEFAULT_PAGE_POOL_SIZE = 8


def generate_random_ip():
    return '.'.join([f'{randint(0, 255)}' for x in range(4)])


def generate_random_web_page():
    files = [
        'home', 'index', 'main', 'about',
        'contact', 'info', 'find_us', 'disclaimer',
        'staff', 'our_people', 'shop', 'press',
        'downloads', 'documents', 'gallery',
    ]
    extensions = ['html', 'htm', 'php']

    return f'{pick(files)}.{pick(extensions)}'


def generate_random_ip_pool(size=DEFAULT_IP_POOL_SIZE):
    return [generate_random_ip() for x in range(size)]


def generate_random_web_page_pool(size=DEFAULT_PAGE_POOL_SIZE):
    return [generate_random_web_page() for x in range(size)]


def generate_plausible_http_code():
    random_number_of_destiny = random()

    if random_number_of_destiny < 0.5:
        return 200
    elif random_number_of_destiny < 0.6:
        return 201
    elif random_number_of_destiny < 0.7:
        return 400
    elif random_number_of_destiny < 0.85:
        return 401
    elif random_number_of_destiny < 0.95:
        return 404
    else:
        return 500


def log_file_line(ips=generate_random_ip_pool(), pages=generate_random_web_page_pool()):
    return f'{pick(ips)},{pick(pages)},{generate_plausible_http_code()}'


if __name__ == '__main__':

    log_file = input(f'Output file? {[DEFAULT_LOG_FILE]}: ')
    log_file = log_file if log_file else DEFAULT_LOG_FILE

    try:
        log_file_size = input(f'How many entries in the log file? [{DEFAULT_LOG_FILE_SIZE}]: ')
        log_file_size = int(log_file_size) if log_file_size else DEFAULT_LOG_FILE_SIZE
    except ValueError:
        log_file_size = DEFAULT_LOG_FILE_SIZE

    try:
        ip_pool_size = input(f'How many distinct IPs? [{DEFAULT_IP_POOL_SIZE}]: ')
        ip_pool = generate_random_ip_pool(int(ip_pool_size) if ip_pool_size else DEFAULT_IP_POOL_SIZE)
    except ValueError:
        ip_pool = generate_random_ip_pool(DEFAULT_IP_POOL_SIZE)

    try:
        page_pool_size = input(f'How many possible pages? [{DEFAULT_PAGE_POOL_SIZE}]: ')
        page_pool = generate_random_web_page_pool(int(page_pool_size) if page_pool_size else DEFAULT_PAGE_POOL_SIZE)
    except ValueError:
        page_pool = generate_random_web_page_pool(DEFAULT_PAGE_POOL_SIZE)

    print()

    try:
        if log_file_size < 1 or len(ip_pool) < 1 or len(page_pool) < 1:
            raise ValueError
        with open(log_file, 'w') as log:
            for line in range(log_file_size):
                log.write(f'{log_file_line(ip_pool, page_pool)}\n')
        print(f'{log_file_size} {"records" if log_file_size > 1 else "record"} written to "{log_file}".')
    except (FileNotFoundError, IOError,):
        print('Error writing file. Sorry about that.')
    except ValueError:
        print('No records to write. Probably your problem, that.')

