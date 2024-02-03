class MyCoustomError(TypeError):
    def __init__(self,message,code):
        super().__init__(f'Error code {code}:{message}')
        self.code = code

raise MyCoustomError('Ouch! An error happend.',600)


