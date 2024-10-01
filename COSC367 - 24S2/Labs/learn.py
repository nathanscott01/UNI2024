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
    true_spam_v_count = [0 for _ in range(n_variables)]
    true_count = 0
    false_spam_v_count = [0 for _ in range(n_variables)]
    false_count = 0
    for email in entries[1:]:
        if email[-1] == '1':
            true_count += 1
            for i in range(n_variables):
                if email[i] == '1':
                    true_spam_v_count[i] += 1
        else:
            false_count += 1
            for i in range(n_variables):
                if email[i] == '1':
                    false_spam_v_count[i] += 1
    likelihood = []
    for i in range(n_variables):
        element_class_t = (true_spam_v_count[i] + pseudo_count) / (true_count + 2 * pseudo_count)
        element_class_f = (false_spam_v_count[i] + pseudo_count) / (false_count + 2 * pseudo_count)
        likelihood.append(tuple((element_class_f, element_class_t)))
    return likelihood


def nb_classify(prior, likelihood, input_vector):
    """Return a tuple (Instance, Certainty) for the input vector"""
    n = len(likelihood)
    prob_true = 1
    prob_false = 1
    for i in range(n):
        prob_true *= likelihood[i][1] if input_vector[i] else (1 - likelihood[i][1])
        prob_false *= likelihood[i][0] if input_vector[i] else (1 - likelihood[i][0])
    alpha = 1 / (prior * prob_true + (1 - prior) * prob_false)
    prosterior_prob_t = alpha * prob_true * prior
    prosterior_prob_f = alpha * prob_false * (1 - prior)
    if prosterior_prob_t <= prosterior_prob_f:
        return "Not Spam", prosterior_prob_f
    else:
        return "Spam", prosterior_prob_t
