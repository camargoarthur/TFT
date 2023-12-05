Sequencia: getPlayerInfo > getMatchHistory > getPlayersName > dataCleaning

Etapas:
- Logar na API da RIOT e validar token
- Pegar dados de partidas do dia anterior (modelo D -1) e armazenar no mongo
- Tratar dados
- Armazenar no postgres

Tratativas dados:
postgres:
Chave primaria = match_id
Informações pra coletar:
Colocação nas partidas
Nivel final
Dano total a jogadores
rounds jogados
jogadores eliminados
#############
Estrutura postgres:
matchs: Dados da partida
matchtraits: caracteristicas 
    FK match_id
    Remover "Set10_" do name ao salvar
matchunits: unidades usadas
matchsitem: itens da unidade
