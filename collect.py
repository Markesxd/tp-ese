from random import randint
from time import sleep
from pydriller import Repository
from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier
from textblob.sentiments import NaiveBayesAnalyzer
from datetime import datetime
import re as regex
from threading import Thread

def wrfl(commit):
    file = open('dados.txt', '+a')
    blob = TextBlob(commit.msg, analyzer=NaiveBayesAnalyzer())
    file.write(f'> {commit.msg}\n{cl.classify(commit.msg)}\n{blob.sentiment}\n')
    file.close()

train= [
        ('Add binary search tree.', 'add'),
        ('Add big O info', 'add'),
        ('Add Trie.', 'add'),
        ('Fix README.', 'fix'),
        ('Integrate codecov.','add'),
        ('Fix binary tree node.', 'fix'),
        ('Add AVL Tree.', 'add'),
        ('Add playground.', 'add'),
        ('Add big O sheet for sorting algorithms.', 'add'),
        ('Add selection sort.', 'add'),
        ('Typos fixed (lines 81, 130, 166, 248)', 'fix'),
        ('Restructure the Big O Notation table.','none'),
        ('Some text fixes.', 'fix'),
        ('Update README.md', 'none'),
        ('Fixing typos in Linked List README.es-ES.md', 'fix'),
        ('Update breadthFirstSearch.js', 'none'),
        ('Update README.pl-PL.md', 'none'),
        ('fixed spelling error for hash-table', 'fix'),
        ('fix typos', 'fix'),
        ('Correct inaccurate Chinese translation.', 'fix'),
        ('Correction', 'fix'),
        ('Create FUNDING.yml', 'add')
]

cl = NaiveBayesClassifier(train)

# i = 0
# for commit in Repository('https://github.com/trekhleb/javascript-algorithms.git').traverse_commits():
#     p = Thread(target=wrfl, args=(commit,))
#     p.start()
#     if i % 10 == 0:
#         sleep(1)

reporitories = [
    'https://github.com/google/gvisor.git',
    # 'https://github.com/trekhleb/javascript-algorithms.git',
    # 'https://github.com/google/googletest.git',
    # 'https://github.com/SeleniumHQ/selenium'
]

time = datetime.now()
file = open(f'./data/dados_{time}.csv', '+a')
file.write(f'classify,polarity,subjectivity\n')

i = 1
for repository in reporitories:
    for commit in Repository(repository).traverse_commits():
        msgv = regex.findall('[[a-z]|[A-Z]|[0-9]|\!|\,|\\|\?|\@|\#|\$|\%|\"|\&|\*|\(|\)|\-|\/|\+|\.|\s|\_|" "]', commit.msg)
        msg = ''.join(msgv)
        blob = TextBlob(msg)
        file.write(f'{cl.classify(msg)},{blob.sentiment[0]},{blob.sentiment[1]}\n')
    print(f'Repository #{i} drilled successfully')
    i += 1

file.close()