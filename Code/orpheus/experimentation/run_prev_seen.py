# This runs the "Previously Seen" experiment which varies the proportion of
# and measures the response of accuracy of the support vector classifier on
# all features tested.
from l0_100a_50d import ex

# TODO: add workspace-level config class and store all features in it
# read from that class here

for feat_col in ['review_contents', 'pos_tags', 'nested_pos_bigrams', 'path_pos_bigrams', 'path_pos_trigrams']:
    for clf in ['svc']:
        for m_df in [.003]:
            for test_prop in [.1, .2, .3, .4, .5, .6, .7, .8, .9]:
                ex.run(clf, config_updates={
                    'dataset.min_doc_freq': m_df,
                    'dataset.feature_column': feat_col,
                    'dataset.test_set_prop': test_prop,
                    'name': f'{clf}__min_df_{m_df}_{feat_col}',
                })
