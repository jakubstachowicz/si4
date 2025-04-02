def gini_gain(left_pos, left_neg, right_pos, right_neg):
    gini_left = 1 - (left_pos / (left_pos + left_neg)) ** 2 - (left_neg / (left_pos + left_neg)) ** 2
    gini_right = 1 - (right_pos / (right_pos + right_neg)) ** 2 - (right_neg / (right_pos + right_neg)) ** 2
    left = left_pos + left_neg
    right = right_pos + right_neg
    return 1 - left / (left + right) * gini_left - right / (left + right) * gini_right
