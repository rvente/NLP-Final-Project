# TODO: addme @blake
# https://github.com/IDSIA/sacred/issues/416
# https://github.com/Qwlouse/Binding/blob/master/run_evaluation.py

from l0_100a_50d import ex

for feat_col in ['review_contents', 'pos_tags', 'nested_pos_bigrams', 'path_pos_bigrams']:
    for clf in ['svc', 'MultiNomNB']:
        for m_df in [.001, .003, .005, .01, .1]:
            ex.run(clf, config_updates={
                'dataset.min_doc_freq': m_df,
                'dataset.feature_column': feat_col,
                'name': f'{clf}__min_df_{m_df}_{feat_col}',
            })
