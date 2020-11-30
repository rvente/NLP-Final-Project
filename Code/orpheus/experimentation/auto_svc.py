from sklearn.metrics import accuracy_score, confusion_matrix, f1_score
from sklearn.svm import LinearSVC
from sacred import Experiment
from l0_100a_50d import ex

for m_df in [.001, .003, .005, .01, .1]:
    ex.run('svc', config_updates={
        'dataset.min_doc_freq': m_df,
        'name': f'svc @min_df {m_df}'
    })
