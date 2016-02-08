#! /usr/bin/env python

import argparse
import time

from subprocess import check_output

todays_date = time.strftime("%m/%d/%y")

parser = argparse.ArgumentParser(description="Used to determine the number of commits to a git repo by email address.  "
    "This command must be run in a local git repostiory working directory."
)
parser.add_argument("--since",
    help="Search for commits more recent than a specific date.",
    default="6/6/2001",
)
parser.add_argument("--until",
    help="Search for commits older than a specific date.",
    default=todays_date,
)
parser.add_argument("email_list",
    help="A space seperated list of email address to search a git repository log for.",
    nargs='*',
    default=[],
)

args = parser.parse_args()

def get_commit_count(args):
    count_dict = {}
    for each_email_address in args.email_list:
        command = ['git', 'log', '--oneline','--author=%s' % each_email_address, '--since=%s' % args.since, '--until=%s' % args.until]
        log_entries_list = check_output(command)
        log_entry_count = len(log_entries_list.split('\n'))-1 # We do subtract 1 magic here to get the list back to base 0.
        count_dict[each_email_address] = log_entry_count

    return count_dict

if __name__ == "__main__":
    commit_counts = get_commit_count(args)
    print commit_counts
