#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Merge FGC released json to DRCD format
#

import json
import codecs
from collections import OrderedDict

def main():

  q_json = json.load(open('json/FGC_release_A.json'))
  a_json = json.load(open('json/FGC_release_A_answers.json'))
  answers = OrderedDict()
  docus = OrderedDict()

  for aa in a_json:
    answer_tmp = aa['ANSWER']
    if ';' in answer_tmp: # Enum type answers, get first one only
      answer_tmp = answer_tmp.split(';')
      answer_tmp = answer_tmp[0]
    answers[aa['QID']] = answer_tmp

  for dd in q_json:
    docus[dd['DID']] = OrderedDict()
    docus[dd['DID']]['context'] = dd['DTEXT']
    q_list = []
    docus[dd['DID']]['qas'] = q_list
    for qq in dd['QUESTIONS']:
      one_question = dict()
      one_question['question'] = qq['QTEXT']
      one_question['id'] = qq['QID']
      one_ans = dict([ ('id', qq['QID']),
                       ('text', answers[qq['QID']]),
                       ('answer_start', 0)])
      try:
        find_ans_pos = dd['DTEXT'].index(answers[qq['QID']])
      except:
        find_ans_pos = None

      if not find_ans_pos:
        # cannot find exact answer in document, skip
        continue
      one_ans['answer_start'] = find_ans_pos
      one_question['answers'] = [one_ans,]
      q_list.append(one_question)
    if len(q_list) < 1:
      docus.pop(dd['DID'], None)

  drcd_json = json.load(open('json/DRCD_training.json'))
  drcd_json['data'].append(dict({
      "title": "FGC",
      "id": "999999",
      "paragraphs": [d for k,d in docus.items()]}))
  to_file("DRCD_plus_FGC_training.json", drcd_json)

def to_file(filename, docs):
  with codecs.open(filename, 'w') as out_j_file:
    out_j_file.write(json.dumps(docs, ensure_ascii=False, indent=2, separators=(',', ': ')))

if __name__ == '__main__':
  main()
