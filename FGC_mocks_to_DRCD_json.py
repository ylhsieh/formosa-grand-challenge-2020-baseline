#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
#
#

import json
import codecs
from collections import OrderedDict

def main():
  part_names = ['A', 'B', 'C']
  out_docs = OrderedDict()

  for part_name in part_names:
    q_json = json.load(open('json/FGC_mock_{}.json'.format(part_name)))

    for doc_js in q_json:
      doc_id = doc_js['DID']
      if doc_id not in out_docs:
        out_docs[doc_id] = OrderedDict()
      out_docs[doc_id]['context'] = doc_js['DTEXT']
      q_list = []
      out_docs[doc_id]['qas'] = q_list

      for qq in doc_js['QUESTIONS']:
        one_question = dict()
        one_question['question'] = qq['QTEXT']
        one_question['id'] = qq['QID']
        one_ans = qq['ANSWER']
        if ';' in one_ans:
          one_ans = one_ans.split(';')
          one_ans = one_ans[0]
        try:
          find_ans_pos = doc_js['DTEXT'].index(one_ans)
        except:
          find_ans_pos = -1

        ans_dict = dict([('id', qq['QID']),
                         ('text', one_ans),
                         ('answer_start', find_ans_pos)])

        ans_dict['answer_start'] = find_ans_pos
        one_question['answers'] = [ans_dict,]
        q_list.append(one_question)

  to_file("FGC_all_mocks_DRCD_format.json", out_docs)

def to_file(filename, docs):
  ## Output questions
  json_out_merged = list()
  for dd in docs.values():
    json_out = to_json(dd)
    if json_out:
      json_out_merged.append(json_out)

  with codecs.open(filename, 'w') as out_j_file:
    out_j_file.write('{"data":[{"title": "FGC_mock","id": "9999999","paragraphs":[')
    out_j_file.write(',\n'.join(json_out_merged))
    out_j_file.write(']}]}')

def to_json(doc):
  if len(doc['qas']) < 1: return None
  return json.dumps(doc, ensure_ascii=False, indent=2, separators=(',', ': '))

main()
