#Changelog 

## [1.0.0] - 2025-02-27
### Adicionado
- Adicionada função gravar_log_arquivo para registrar logs em um arquivo de forma persistente, 

### Corrigido
- Erro ao gravar log! , 'charmap' codec can't encode character '\u2795' in position 19: character maps to <undefined>.
Acrescentado o encoding="utf-8 ao metodo open().
