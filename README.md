# Overview

1. Install dependencies: <a href="https://github.com/rvente/NLP-Final-Project/blob/release/Code/orpheus/INSTALLING.md">INSTALLING.md</a>
2. Process dataset: <a href="https://github.com/rvente/NLP-Final-Project/blob/release/Code/orpheus/data/DataFuncs.py">DataFuncs.py</a>
3. Extract Features: <a href="https://github.com/rvente/NLP-Final-Project/blob/release/Code/orpheus/feature_extraction/add_parse_tree.py">add_parse_tree.py</a>
4. Run experiments.  <a href="https://github.com/rvente/NLP-Final-Project/blob/release/Code/orpheus/experimentation/run_all.py">run_all.py</a>

<h1>Directory Tree</h1><p>
<a href="https://github.com/rvente/NLP-Final-Project/blob/release/Code/orpheus">https://github.com/rvente/NLP-Final-Project/blob/release/Code/orpheus</a><br>
├── <a href="https://github.com/rvente/NLP-Final-Project/blob/release/Code/orpheus/analysis/">analysis</a> Use these notebooks for analysis, reading and writing to /results .<br>
│   ├── <a href="https://github.com/rvente/NLP-Final-Project/blob/release/Code/orpheus/analysis/analysis.ipynb">analysis.ipynb</a><br>
│   ├── <a href="https://github.com/rvente/NLP-Final-Project/blob/release/Code/orpheus/analysis/chart_nb_x_alpha.ipynb">chart_nb_x_alpha.ipynb</a><br>
│   ├── <a href="https://github.com/rvente/NLP-Final-Project/blob/release/Code/orpheus/analysis/chart_prev_seen.ipynb">chart_prev_seen.ipynb</a><br>
│   ├── <a href="https://github.com/rvente/NLP-Final-Project/blob/release/Code/orpheus/analysis/chart_svc_prev_seen.ipynb">chart_svc_prev_seen.ipynb</a><br>
│   ├── <a href="https://github.com/rvente/NLP-Final-Project/blob/release/Code/orpheus/analysis/generate_charts.ipynb">generate_charts.ipynb</a><br>
│   ├── <a href="https://github.com/rvente/NLP-Final-Project/blob/release/Code/orpheus/analysis/Presentation.ipynb">Presentation.ipynb</a><br>
│   ├── <a href="https://github.com/rvente/NLP-Final-Project/blob/release/Code/orpheus/analysis/Presentation-NB.ipynb">Presentation-NB.ipynb</a><br>
│   └── <a href="https://github.com/rvente/NLP-Final-Project/blob/release/Code/orpheus/analysis/Presentation-SVC.ipynb">Presentation-SVC.ipynb</a><br>
├── <a href="https://github.com/rvente/NLP-Final-Project/blob/release/Code/orpheus/data/">data</a> Store data and feature extraction output here.<br>
│   ├── <a href="https://github.com/rvente/NLP-Final-Project/blob/release/Code/orpheus/data/1000A30D__doc%2Bpos.pkl">1000A30D__doc+pos.pkl</a><br>
│   ├── <a href="https://github.com/rvente/NLP-Final-Project/blob/release/Code/orpheus/data/1000A30D_with_doc.pkl">1000A30D_with_doc.pkl</a><br>
│   ├── <a href="https://github.com/rvente/NLP-Final-Project/blob/release/Code/orpheus/data/100A50D.csv">100A50D.csv</a><br>
│   ├── <a href="https://github.com/rvente/NLP-Final-Project/blob/release/Code/orpheus/data/100A50D__doc%2Bpos.pkl">100A50D__doc+pos.pkl</a><br>
│   ├── <a href="https://github.com/rvente/NLP-Final-Project/blob/release/Code/orpheus/data/100A50D_POS.pkl">100A50D_POS.pkl</a><br>
│   ├── <a href="https://github.com/rvente/NLP-Final-Project/blob/release/Code/orpheus/data/DataFuncs.py">DataFuncs.py</a><br>
│   ├── <a href="https://github.com/rvente/NLP-Final-Project/blob/release/Code/orpheus/data/Run_All.py">Run_All.py</a><br>
│   ├── ... <br>
│   ├── <a href="https://github.com/rvente/NLP-Final-Project/blob/release/Code/orpheus/data/small_with_doc.pkl">small_with_doc.pkl</a><br>
│   └── <a href="https://github.com/rvente/NLP-Final-Project/blob/release/Code/orpheus/data/small.xlsx">small.xlsx</a><br>
├── <a href="https://github.com/rvente/NLP-Final-Project/blob/release/Code/orpheus/experimentation/">experimentation</a> Configure and run the machine learning models <br>
│   ├── <a href="https://github.com/rvente/NLP-Final-Project/blob/release/Code/orpheus/experimentation/l0_100a_50d.py">l0_100a_50d.py</a><br>
│   ├── <a href="https://github.com/rvente/NLP-Final-Project/blob/release/Code/orpheus/experimentation/__pycache__/">__pycache__</a><br>
│   ├── <a href="https://github.com/rvente/NLP-Final-Project/blob/release/Code/orpheus/experimentation/run_all.py">run_all.py</a> Outlines the most general combinations of hyper-parameters. <br>
│   ├── <a href="https://github.com/rvente/NLP-Final-Project/blob/release/Code/orpheus/experimentation/run_prev_seen.py">run_prev_seen.py</a><br>
│   ├── <a href="https://github.com/rvente/NLP-Final-Project/blob/release/Code/orpheus/experimentation/sandbox.py">sandbox.py</a><br>
│   └── <a href="https://github.com/rvente/NLP-Final-Project/blob/release/Code/orpheus/experimentation/svc.py">svc.py</a><br>
├── <a href="https://github.com/rvente/NLP-Final-Project/blob/release/Code/orpheus/feature_extraction/">feature_extraction</a><br>
│   ├── <a href="https://github.com/rvente/NLP-Final-Project/blob/release/Code/orpheus/feature_extraction/add_parse_tree.py">add_parse_tree.py</a><br>
│   ├── <a href="https://github.com/rvente/NLP-Final-Project/blob/release/Code/orpheus/feature_extraction/add_path_features.py">add_path_features.py</a><br>
│   ├── <a href="https://github.com/rvente/NLP-Final-Project/blob/release/Code/orpheus/feature_extraction/instance_parser.py">instance_parser.py</a><br>
│   └── <a href="https://github.com/rvente/NLP-Final-Project/blob/release/Code/orpheus/feature_extraction/__pycache__/">__pycache__</a><br>
├── <a href="https://github.com/rvente/NLP-Final-Project/blob/release/Code/orpheus/figures/">figures</a> Figures generated by the analysis scripts. <br>
│   ├── <a href="https://github.com/rvente/NLP-Final-Project/blob/release/Code/orpheus/figures/nb_x_alpha.pdf">nb_x_alpha.pdf</a><br>
│   ├── <a href="https://github.com/rvente/NLP-Final-Project/blob/release/Code/orpheus/figures/nb_x_alpha.svg">nb_x_alpha.svg</a><br>
│   ├── <a href="https://github.com/rvente/NLP-Final-Project/blob/release/Code/orpheus/figures/nb_x_prev_seen.pdf">nb_x_prev_seen.pdf</a><br>
│   └── <a href="https://github.com/rvente/NLP-Final-Project/blob/release/Code/orpheus/figures/svm_x_prev_seen.pdf">svm_x_prev_seen.pdf</a><br>
├── <a href="https://github.com/rvente/NLP-Final-Project/blob/release/Code/orpheus/INSTALLING.md">INSTALLING.md</a> How to install and configure <br>
├── <code>logs</code> gitignored: The filesystem database of experiments<br>
│   ├── 1<br>
│   ├── 10<br>
│   ├── 100<br>
│   ├── 101<br>
│   ├── ... <br>
│   └── <code>&lowbar;sources</code> <br>
├── <a href="https://github.com/rvente/NLP-Final-Project/blob/main/Code/orpheus/prev_seen_logs/">prev_seen_logs</a> not gitignored: view sample logs here on another branch <br>
│   ├── <a href="https://github.com/rvente/NLP-Final-Project/blob/main/Code/orpheus/prev_seen_logs/1/">1</a><br>
│   ├── <a href="https://github.com/rvente/NLP-Final-Project/blob/main/Code/orpheus/prev_seen_logs/10/">10</a><br>
│   ├── <a href="https://github.com/rvente/NLP-Final-Project/blob/main/Code/orpheus/prev_seen_logs/11/">11</a><br>
│   ├── ... <br>
│   └── <a href="https://github.com/rvente/NLP-Final-Project/blob/release/Code/orpheus/prev_seen_logs/_sources/">_sources</a><br>
├── <a href="https://github.com/rvente/NLP-Final-Project/blob/release/Code/orpheus/INSTALLING.md">INSTALLING.md</a><br>
├── <a href="https://github.com/rvente/NLP-Final-Project/blob/release/Code/orpheus/requirements_2.txt">requirements_2.txt</a><br>
├── <a href="https://github.com/rvente/NLP-Final-Project/blob/release/Code/orpheus/requirements.txt">requirements.txt</a><br>
├── <a href="https://github.com/rvente/NLP-Final-Project/blob/release/Code/orpheus/results/">results</a><br>
│   ├── <a href="https://github.com/rvente/NLP-Final-Project/blob/release/Code/orpheus/results/nb_df_acc.pkl">nb_df_acc.pkl</a><br>
│   ├── <a href="https://github.com/rvente/NLP-Final-Project/blob/release/Code/orpheus/results/nb_df_f1.pkl">nb_df_f1.pkl</a><br>
│   ├── <a href="https://github.com/rvente/NLP-Final-Project/blob/release/Code/orpheus/results/nb_x_alpha_df_acc.pkl">nb_x_alpha_df_acc.pkl</a><br>
│   ├── <a href="https://github.com/rvente/NLP-Final-Project/blob/release/Code/orpheus/results/svc_df_acc.pkl">svc_df_acc.pkl</a><br>
│   ├── <a href="https://github.com/rvente/NLP-Final-Project/blob/release/Code/orpheus/results/svc_df_f1.pkl">svc_df_f1.pkl</a><br>
│   └── <a href="https://github.com/rvente/NLP-Final-Project/blob/release/Code/orpheus/results/svm_x_prev_seen.pkl">svm_x_prev_seen.pkl</a><br>
├── <a href="https://github.com/rvente/NLP-Final-Project/blob/release/Code/orpheus/software_citations.bib">software_citations.bib</a><br>
└── virtualenv  We recommend a virtual environment for installing packages. <br>
</p>
