from core.boolean.BooleanModel import BooleanModel
from time import time

def MeasureBooleanModel(documents, consults):
    booleanModel = BooleanModel(documents)

    precisionMeasures, recallMeasures, timeMetrics = [], [], []
    for q in consults:
        relevant = [i[1] for i in q.relevant if i[2] == 1]
        begTime = time()
        recovered = booleanModel.Consult(q, relaxed=0.5)
        timeElapsed = time() - begTime
        timeMetrics.append(timeElapsed)

        rr = sum((1 if i.id in relevant else 0 for i in recovered))
        precisionMeasures.append((rr + 1) / (len(recovered) + 1))
        recallMeasures.append((rr + 1) / (len(relevant) + 1))
    return precisionMeasures, recallMeasures, timeMetrics
    # 0.5173405778585659 0.8575238095238096 with exact relevant and relaxed=0.5
    # 0.6686247376979687 0.2702042873029432 with all relevants and relaxed=0.5







