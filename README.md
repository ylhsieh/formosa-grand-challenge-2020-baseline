# Baseline for Formosa Grand Challenge 2020
1. Requirements
   * python 3
   * pytorch
   * https://github.com/huggingface/transformers
2. Install
   * Clone this repository
   * Download [FGC dataset](https://scidm.nchc.org.tw/dataset/grandchallenge2020) unzip and place under a sub-directory named `json`
   * Download [DRCD corpus](https://github.com/DRCKnowledgeTeam/DRCD) and place under `json`
3. Preprocess dataset
   * Run `python FGC_merge_to_DRCD_json.py` to merge FGC training data into DRCD
   * Run `python FGC_mocks_to_DRCD_json.py` to create development set data using FGC mock tests
