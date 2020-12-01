from l0_100a_50d import ex

# add the Ingredient while creating the experiment

for feat_col in ['path_pos_bigrams','path_pos_trigrams']:
    for clf in ['kernelsvc']:
        for m_df in [.01 ]:
            ex.run(clf, config_updates={
                'dataset.min_doc_freq': m_df,
                'dataset.feature_column': feat_col,
                'name': f'{clf}__min_df_{m_df}_{feat_col}',
            })
