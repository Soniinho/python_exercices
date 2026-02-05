% Definição de fatos para testar
palavra(cachorro).
palavra(cachorra).
palavra(banana).
palavra(mamute).
palavra(maçã).
palavra(cenoura).

% Verificar se uma letra está presente em uma palavra
verificar_letra(Letra, Palavra) :-
    atom_chars(Palavra, ListaLetras),
    memberchk(Letra, ListaLetras).

% Filtrar palavras com um tamanho específico
palavra_com_tamanho(Tamanho, Palavra) :-
    palavra(Palavra),
    atom_length(Palavra, Tamanho).

% Encontra a letra mais comum em uma determinada posição entre as palavras conhecidas
letra_mais_comum(Posicao, Letra) :-
    findall(L, (palavra(P), nth1(Posicao, P, L)), ListaLetras),
    msort(ListaLetras, ListaLetrasOrdenada),
    reverse(ListaLetrasOrdenada, ListaLetrasReversa),
    ListaLetrasReversa = [Letra|_].

% Regra para encontrar palavras com letras em posições específicas
encontrar_palavra(Tamanho, Padrao, Palavra) :-
    palavra(Palavra),
    atom_chars(Palavra, Lista),
    length(Lista, Tamanho),
    verificar_padrao(Padrao, Lista).

verificar_padrao([], _).
verificar_padrao([H|T], [H|Resto]) :-
    verificar_padrao(T, Resto).
verificar_padrao([_|T], [_|Resto]) :-
    verificar_padrao(T, Resto).
