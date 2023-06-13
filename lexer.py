import ply.lex as plex

class lexer:
    tokens= ("ESCREVER","VAR", "COMENTAR", "string","numero")
    literals = ['*', '+', '(', ')', '-', '=', ':', ',', '/']
    t_ignore = " \n"

    def __init__(self):
        self.lexer = None

    def build(self, **kwargs):
        self.lexer = plex.lex(module=self, **kwargs)

    def input(self, string):
        self.lexer.input(string)

    def t_string(self, t):
        r'\"[^\"]*\"'
        t.value = {"string": t.value[1:-1]}
        return t
    
    def t_token(self, t):
        r'ESCREVER|VAR|COMENTAR'
        t.type = t.value
        return t
    
    def t_numero(self, t):
        r"[0-9]+(\.[0-9]+)?"
        t.value = {"numero": float(t.value)}
        return t
    
    def token(self):
        token = self.lexer.token()
        return token if token is None else token.type

    def t_error(self, t):
        print(f"Unexpected token: [{t.value[:10]}]")
        exit(1)