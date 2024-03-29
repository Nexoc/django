from time import sleep


class Wait:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        sleep(2)
        response = self.get_response(request)

        return response
