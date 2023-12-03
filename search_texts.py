# Это делает Наташа
#
# На вход подаются 1) (tf-idf запроса) список из чисел 2) (tf-idf текстов (заметок)) словарь со списками из чисел
# На выход возвращается список из индексов самых подходящих текстов (до 5 или 10)
#
# Пример 1 (запрос):
# Вход: 
# tf-idf запроса: [0.9, 0. , 0. , 0. , 0.1]
# tf-idf текстов: {0: [0.8, 0. , 0. , 0. , 0.2], 2: [0.66666667, 0. , 0. , 0. , 0.66666667]}
# Выход: [0]
#
# Ссылка на гугл колаб файл с примером реализации tf-idf (мой): 
# В самом конце там есть описание алгоритма, которое мы обсуждали на паре (где списки перемножаются)
# https://colab.research.google.com/drive/12lf77dL1nvCl5pk9TPKHDQnOSbsnZm8C?usp=sharing

# testDataset = {
#     "query": [[0., 0., 0., 0., 0., 0., 0., 0., 0.70710678, 0.70710678]],
#     "notes": {
#         2: [0. , 0., 0.42804604, 0.42804604, 0., 0., 0., 0.5628291, 0.5628291, 0.],
#         4: [0., 0.51741994, 0.3935112, 0.3935112, 0.3935112, 0.51741994, 0., 0., 0., 0.],
#         7: [0.52863461, 0., 0., 0., 0.40204024, 0. , 0.52863461, 0. , 0. , 0.52863461]
#     }
# } 


def getRelevantNotesByTFIDF (TFIDF, count = 5) :
    queryTFIDF = TFIDF['query'][0]
    notesDistTFIDF = TFIDF['notes']

    relevantNotes = []
    for (key, noteTFIDF) in notesDistTFIDF.items():
        amountRelevantWords = 0.0
        for j in range(len(noteTFIDF)) :
            amountRelevantWords += noteTFIDF[j] * queryTFIDF[j]
        relevantNotes.append({
            "relevated": amountRelevantWords,
            "notes": key
        })
    
    relevantNotes.sort(reverse=True,key=lambda note:note["relevated"])
    
    if (len(relevantNotes) > count):
        relevantNotes = relevantNotes[:count]

    return relevantNotes

# relevantNotes = getRelevantNotesByTFIDF(testDataset)
# print(relevantNotes)
