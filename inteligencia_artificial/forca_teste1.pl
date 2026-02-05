% Definição de fatos para testar
palavra(cachorro).
palavra(cachorra).
palavra(banana).
palavra(mamute).
palavra(maçã).
palavra(cenoura).

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
