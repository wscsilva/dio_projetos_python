import locale

class Util:
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

    @staticmethod
    def formatToReal(valor):
        return locale.currency(valor, grouping=True, symbol=True)
