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
   * Run `python FGC_final_to_DRCD.py` to convert official test set data to DRCD format
4. Run [run_fgc_baseline.ipynb](run_fgc_baseline.ipynb) (can be run in Google Colab)
   * On a single Titan X GPU with 12G of memory, we can use the hyperparameters listed in here
   * Multi-GPU support is in **beta**
5. Test set performance: correctly answer 15 out of 50 questions
