% Base de conhecimento de palavras
palavra('PROGRAMACAO').
palavra('DESENVOLVIMENTO').
palavra('INTELIGENCIA').
palavra('ARTIFICIAL').
palavra('COMPUTADOR').
palavra('ALGORITMO').

% Regra para sugerir uma letra
sugerir_letra(Palavra, Letra) :-
    palavra(Palavra),
    atom_chars(Palavra, Chars),
    random_member(Letra, Chars).
