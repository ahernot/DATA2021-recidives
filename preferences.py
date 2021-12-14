columns = [
    #'id',
    'sex',
    #'dob',
    'age',
    #'age_cat',
    'social_cat',
    'priors_count',
    'c_jail_in',
    'c_jail_out',
    #'c_case_number',
    'c_offense_date',
    'c_arrest_date',
    #'c_charge_degree',  # can be found in durée de peine
    #'c_charge_desc',  # can be found in durée de peine
    'is_recid',
    #'r_case_number',
    'r_charge_degree',
    'r_offense_date',
    #'r_charge_desc',
    #'is_violent_recid',
    'decile_score',
    #'score_text',
    #'screening_date'
]


SELECTED_FEATURES = [
    'sex',
    'age',
    'sex_val',
    #'social_cat',
    'priors_count',
    'c_jail_in',
    'c_jail_out',
    'jail_duration',
    'c_offense_date',
    'c_arrest_date', # combine those two cols
    'is_recid',
    'decile_score'

]
score = 'decile_score'
