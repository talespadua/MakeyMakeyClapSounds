# MakeyMakey Clap Music

Esse projeto é parte da disciplina Sistemas Multimídia e Hipermídia do curso de Ciências da Computação do Senac - SP

O programa lê um arquivo txt com notas musicais e toca as notas ao pressionar da tecla espaço. Ao invés do teclado,o usuário deve utilizar o <a href="http://www.makeymakey.com/">Makey Makey</a>,
conforme o <a href="https://youtu.be/PjGneU0UBFw">vídeo</a>.

Esse projeto é baseado no projeto <a href="https://github.com/akajuvonen/beep-reader-player">Beep Reader Player</a>

# Utilização

Esse programa é escrito em Python 2.7 e tem como dependencia as bibliotecas Numpy e PyGame

Para executar, digite no terminal:
 
 python clap_music.py nome_da_musica
 
O nome da musica deve ser o mesmo do arquivo txt correspondende na pasta musics.
  
Para criar uma música, crie um arquivo txt com o nome da musica desejada. Nesse arquivo, cada linha receberá a nota (Funcionando apenas na escala de dó: C D E F G A B C) no formato:

`NOTA+OITAVA:DURAÇÂO:VOLUME`

O valor máximo do volume deve ser 1.0 e os valores de dutação e volume devem ser pontos flutuantes

Exemplo:

G4:0.3:0.5  
A4:0.3:0.5  
B4:0.3:0.5  
G4:0.3:0.5  


