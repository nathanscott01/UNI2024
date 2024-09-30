"""
Nathan Scott
COSC367 Lab 9
Learn Prior
Learn Likelihood
NB Classify
"""
import csv


def open_file(csv_file):
    """Return a list of tuples representing the entries of each row
    in the file"""
    with open(csv_file) as in_file:
        training_examples = [tuple(row) for row in csv.reader(in_file)]
    return training_examples


def learn_prior(file_name, pseudo_count=0):
    """Take the file and return the prior probability of spam being true"""
    entries = open_file(file_name)
    total_emails = len(entries) - 1
    spam_true = 0
    for email in entries:
        if email[-1] == '1':
            spam_true += 1
    p_true = (spam_true + pseudo_count) / (total_emails + pseudo_count * 2)
    return p_true


def learn_likelihood(file_name, pseudo_count=0):
    """Learn the likelihood of the variables"""
    entries = open_file(file_name)
    n_variables = len(entries[0]) - 1
    true_spam_count = [0 for _ in range(n_variables)]
    true_count = 0
    false_spam_count = [0 for _ in range(n_variables)]
    false_count = 0
    for email in entries[1:]:
        if email[-1] == '1':
            true_count += 1


