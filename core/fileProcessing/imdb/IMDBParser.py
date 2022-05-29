from core.basics.MovieReview import MovieReview


def ParseIMDB(text: str):
    return [MovieReview(id + 1, content) for id, content in enumerate(text.split('\n'))]
