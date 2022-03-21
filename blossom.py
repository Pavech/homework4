from typing import Any, Callable
import requests as requests


class ValidatorError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return "Не валидные данные"





def blossom(max_retries: int = 1) -> Callable:
    """Проверка значения на допустимость"""
    if max_retries < 1 or not isinstance(max_retries, int):
        raise ValidatorError("значение не должно быть дробным или меньше 1")
    def decoration(func: Callable) -> Callable:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            result = dict()
            result[func.__name__] = {}
            result[func.__name__]['run'] = []
            for i in range(max_retries):
                try:
                    x = func(*args, **kwargs)
                    result[func.__name__]['is_success'] = True
                    result[func.__name__]['run'].append({"exception": None, "return": x})
                    break
                except BaseException as exc:
                    err = exc.__doc__
                    result[func.__name__]['is_success'] = False
                    result[func.__name__]['run'].append({"exception": err, "return": None})
            return result

        return wrapper

    return decoration


@blossom(3)
def get_page_content(url):
    resp = requests.get(url)
    return resp.content


content_with_retry = get_page_content("https://httpbin.org/get")

print(content_with_retry)
# content_with_retry = get_page_content("http://very_fake_address.com")
#
# print(content_with_retry)