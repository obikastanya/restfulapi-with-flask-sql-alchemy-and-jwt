
class Response:
    @staticmethod
    def make(status=True, msg='',data=[]):
        return {'status':status, 'msg':msg, 'data':data}