import argparse
import os


def parse_args():
    parser = argparse.ArgumentParser(description='Page Loader Utilita')
    parser.add_argument('url_page', type=str)
    parser.add_argument('-o', '--output',
                        type=str,
                        default=os.getcwd(),
                        help='downland_path')
    args = parser.parse_args()
    return args.url_page, args.output
