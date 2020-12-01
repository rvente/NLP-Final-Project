from l0_100a_50d import ex

#TODO: add workspace-level config class and store all features in it
# read from that class here
for feat_col in ['review_contents', 'pos_tags', 'nested_pos_bigrams', 'path_pos_bigrams']:
    for clf in ['svc', 'MultiNomNB']:
        for m_df in [.001, .003, .005, .01, .1]:
            ex.run(clf, config_updates={
                'dataset.min_doc_freq': m_df,
                'dataset.feature_column': feat_col,
                'name': f'{clf}__min_df_{m_df}_{feat_col}',
            })
