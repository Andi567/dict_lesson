language_set = set()
with open('4_vera.tsv') as f:
    for line_number, line_data in enumerate(f):
        if line_number == 0:
            continue
        student_id, account_created, last_active, balance, language_id = line_data.rstrip('\n').split('\t')
               
        language_set.add(language_id)


# Список языков
print (language_set)


