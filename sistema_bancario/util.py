import locale
from datetime import datetime

class Util:
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

    @staticmethod
    def formatToReal(valor):
        return locale.currency(valor, grouping=True, symbol=True)
    
    @staticmethod
    def formatDate(data_hora=None):
        if not data_hora:
            data_hora = datetime.now()

        return data_hora.strftime("%d/%m/%Y")
