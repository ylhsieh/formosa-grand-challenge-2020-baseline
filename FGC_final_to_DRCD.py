#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
#
#

import json
import codecs
from collections import OrderedDict

def main():

  out_docs = OrderedDict()

  q_json = json.load(open('json/FGC_official_final.json'))

  for doc_js in q_json:
    doc_id = doc_js['DID']
    if doc_id not in out_docs:
      out_docs[doc_id] = OrderedDict()
      this_doc = out_docs[doc_id]
      if 'context' not in this_doc:
        this_doc['context'] = doc_js['DTEXT']
      if 'qas' not in this_doc:
        this_doc['qas'] = []
      q_list = this_doc['qas']

      for q_a_pair in doc_js['QUESTIONS']:
        one_question = dict()
        one_question['question'] = q_a_pair['QTEXT']
        one_question['id'] = q_a_pair['QID']
        one_ans = q_a_pair['ANSWER']
        if ';' in one_ans:
          one_ans = one_ans.split(';')
          one_ans = one_ans[0]
        try:
          find_ans_pos = doc_js['DTEXT'].index(one_ans)
        except:
          find_ans_pos = -1

        ans_dict = dict([('id', q_a_pair['QID']),
                         ('text', one_ans),
                         ('answer_start', find_ans_pos)])

        ans_dict['answer_start'] = find_ans_pos
        one_question['answers'] = [ans_dict,]
        q_list.append(one_question)

  to_file("FGC_final_DRCD_format.json", out_docs)

def to_file(filename, docs):
  ## Output questions
  json_out_merged = list()
  for dd in docs.values():
    json_out = to_json(dd)
    if json_out:
      json_out_merged.append(json_out)

  with codecs.open(filename, 'w') as out_j_file:
    out_j_file.write('{"data":[{"title": "FGC_final","id": "0000000","paragraphs":[')
    out_j_file.write(',\n'.join(json_out_merged))
    out_j_file.write(']}]}')

def to_json(doc):
  if len(doc['qas']) < 1: return None
  return json.dumps(doc, ensure_ascii=False, indent=2, separators=(',', ': '))

main()
