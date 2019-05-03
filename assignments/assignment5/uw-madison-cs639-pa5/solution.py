
import pandas as pd
import numpy as np
from fuzzywuzzy import fuzz

import py_entitymatching as em


def main():

    A = em.read_csv_metadata(
        'ltable.csv', key="ltable_id", encoding='ISO-8859-1')
    B = em.read_csv_metadata(
        'rtable.csv', key="rtable_id", encoding='ISO-8859-1')

    ob = em.OverlapBlocker()
    C = ob.block_tables(A, B, 'title', 'title',
                        l_output_attrs=['title', 'category',
                                        'brand', 'modelno', 'price'],
                        r_output_attrs=['title', 'category',
                                        'brand', 'modelno', 'price'],
                        overlap_size=1, show_progress=False)
    S = em.sample_table(C, 450)

    G = em.read_csv_metadata("train.csv",
                             key='id',
                             ltable=A, rtable=B,
                             fk_ltable='ltable_id', fk_rtable='rtable_id')
    feature_table = em.get_features_for_matching(
        A, B, validate_inferred_attr_types=False)
    G = em.label_table(S, 'label')

    attrs_from_table = ['ltable_title', 'ltable_category', 'ltable_brand', 'ltable_modelno', 'ltable_price',
                        'rtable_title', 'rtable_category', 'rtable_brand', 'rtable_modelno', 'rtable_price']
    H = em.extract_feature_vecs(G,
                                feature_table=feature_table,
                                attrs_before=attrs_from_table,
                                attrs_after='label',
                                show_progress=False)
    H.fillna('0', inplace=True)
#     H = em.impute_table(
#         H, exclude_attrs=['_id', 'ltable_ltable_id', 'rtable_rtable_id','label'], strategy='mean')
    rf = em.RFMatcher()

    attrs_to_be_excluded = []
    attrs_to_be_excluded.extend(
        ['_id', 'ltable_ltable_id', 'rtable_rtable_id', 'label'])
    attrs_to_be_excluded.extend(attrs_from_table)

    rf.fit(table=H, exclude_attrs=attrs_to_be_excluded, target_attr='label')

    attrs_from_table = ['ltable_title', 'ltable_category', 'ltable_brand', 'ltable_modelno', 'ltable_price',
                        'rtable_title', 'rtable_category', 'rtable_brand', 'rtable_modelno', 'rtable_price']
    L = em.extract_feature_vecs(C, feature_table=feature_table,
                                attrs_before=attrs_from_table,
                                show_progress=False, n_jobs=-1)

    attrs_to_be_excluded = []
    attrs_to_be_excluded.extend(
        ['_id', 'ltable_ltable_id', 'rtable_rtable_id'])
    attrs_to_be_excluded.extend(attrs_from_table)

    predictions = rf.predict(table=L, exclude_attrs=attrs_to_be_excluded,
                             append=True, target_attr='predicted', inplace=False)

    dataset = pd.DataFrame({"id": G[0]['id'], 'label': predictions['label']})
    dataset.to_csv("./prediction2.csv", index=False)


if __name__ == "__main__":
    main()
