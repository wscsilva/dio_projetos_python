#Changelog 

## [1.0.0] - 2025-02-28
### Adicionado

### Alterado
- Alteração no formato do arquivo de log gravado, segue a tabela de exemplo:

| Tipo  | Data      | Descrição                       | Valor     |
|-------|-----------|---------------------------------|-----------|
|D      | 27/02/2025| Depósito realizado com sucesso  | R$ 500,00 |
|S      | 27/02/2025| Saque efetuado no caixa 24h     | R$ 200,00 |
|S      | 27/02/2025| Consulta de saldo disponível    | R$ 300,00 |


## [1.0.0] - 2025-02-27
### Adicionado
- Adicionada função gravar_log_arquivo para registrar logs em um arquivo de forma persistente, 

### Corrigido
- Erro ao gravar log! , 'charmap' codec can't encode character '\u2795' in position 19: character maps to <undefined>.
Acrescentado o encoding="utf-8 ao metodo open().
