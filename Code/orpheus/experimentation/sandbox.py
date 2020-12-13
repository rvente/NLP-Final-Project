# sandbox for experimenting with various classifiers
from l0_100a_50d import ex

# for m_df in [.001, .003, .005, .01, .1]:
#     ex.run('svc', config_updates={
#         'dataset.min_doc_freq': m_df,
#         'name': f'svc__min_df_{m_df}'
#     })

# for m_df in [.001, .003, .005, .01, .1]:
#     ex.run('MultiNomNB', config_updates={
#         'dataset.min_doc_freq': m_df,
#         'name': f'nb__min_df_{m_df}'
#     })

for feat_col in ['review_contents', 'pos_tags', 'nested_pos_bigrams', 'path_pos_bigrams','path_pos_trigrams']:
    for alpha in [.02]:
        ex.run('MultiNomNB', config_updates={
            'dataset.min_doc_freq': .003,
            'dataset.feature_column': feat_col,
            'name': f'MultiNomNB__min_df_.003_{feat_col}',
            'naivebayes.alpha': alpha
        })
