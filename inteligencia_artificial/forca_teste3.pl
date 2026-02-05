% Palavras de exemplo
palavra('cachorro').
palavra('cachorra').
palavra('gato').
palavra('elefante').
palavra('macaco').
palavra('papagaio').
palavra('cobra').

% Verificar se uma letra está presente em uma palavra
% Verifica se uma letra está presente em uma palavra
verificar_letra(Letra, Palavra) :-
    atom_chars(Palavra, ListaLetras),
    memberchk(Letra, ListaLetras).

% Filtrar palavras com um tamanho específico
palavra_com_tamanho(Tamanho, Palavra) :-
    palavra(Palavra),
    atom_length(Palavra, Tamanho).

% Predicado para verificar se a palavra tem as letras nas posições especificadas
palavra_com_letras_posicoes(Palavra, Posicoes, Letras) :-
    palavra(Palavra),                          % Verifica se a palavra está na base de conhecimento
    string_length(Palavra, Tamanho),           % Obtém o tamanho da palavra
    length(Posicoes, NumPosicoes),             % Obtém o número de posições
    length(Letras, NumPosicoes),               % Obtém o número de letras
    Tamanho =:= NumPosicoes,                   % Verifica se a quantidade de letras é igual ao tamanho da palavra
    verificar_posicoes(Palavra, Posicoes, Letras). % Verifica se as letras estão nas posições especificadas

% Verifica se as letras estão nas posições especificadas
verificar_posicoes(_, [], []).
verificar_posicoes(Palavra, [Posicao|RestoPosicoes], [Letra|RestoLetras]) :-
    nth1(Posicao, Palavra, Letra),             % Obtém a letra na posição especificada
    verificar_posicoes(Palavra, RestoPosicoes, RestoLetras).


% Encontra a letra mais comum em uma determinada posição entre as palavras conhecidas
letra_mais_comum(Posicao, Letra) :-
    findall(L, (palavra(P), nth1(Posicao, P, L)), ListaLetras),
    msort(ListaLetras, ListaLetrasOrdenada),
    reverse(ListaLetrasOrdenada, ListaLetrasReversa),
    ListaLetrasReversa = [Letra|_].

% Exemplo de uso:
% letra_mais_comum(3, Letra). % Encontra a letra mais comum na terceira posição entre as palavras conhecidas
