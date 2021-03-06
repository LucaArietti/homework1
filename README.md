# Homework1
### Homework 1 per il Laboratorio Cyberfisico


#### Descrizione e scelte progettuali
Il progetto è stato sviluppato in Python.
Esso è articolato in tre nodi:
- `publisher`: si occupa di pubblicare ogni secondo tutte le informazioni (nome, età, dipartimento). Scrive su un topic chiamato `cyberchat`
- `keyreader`: legge da tastiera la lettera che fungerà da filtro, controlla che sia valida e la scrive sul topic chiamato `keychat`. È stata aggiunta una `signal` per assicurare la funzionalità di *ctrl+c*, altrimenti non riconosciuta. Inoltre è stato reso l'input case insensitive
- `shower`: è iscritto a entrambi i topic (`cyberchat` e `keychat`) e utilizza le informazioni inviate attraverso `keychat` per filtrare le informazioni di `cyberchat` mediante una variabile globale `filtro` settata di default su 'a'. Quindi mostra a video tramite `loginfo` le informazioni richieste

Pertanto il grafo dei nodi è cosi strutturato:
![alt text](/images/rqt_graph.png)

Si è scelta questa configurazione perché da subito appariva intuitiva, facile da implementare e che rispettasse le specifiche. Riflettendo, infatti, è apparsa come la scelta più comoda per evitare problemi che si sarebbero avuti con la configurazione *A -> B -> C*, quali per esempio l'inviare messaggi costantemente nonostante l'attesa della pressione di un tasto da parte dell'utente.

Per inviare l'array di stringhe, `publisher` utilizza una banale stringa concatenata dal carattere '.', sarà poi il `shower` a parsare la stringa, dividerla in tre e salvarla in una lista.
All'inizio si pensava ad una struttura più corretta, ma vedendo i divesti tipi nella libreria `std_msgs.msg` non ne è presente uno idoneo. Quindi si è valutata l'idea di usare un array di byte e codificare le stringhe in byte per poi decodificarle a destinazione, ma questa soluzione comportava un livello di complicazione non ritenuto strettamente necessario. Per cui in definitiva si è optato per la concatenazione di stringhe.

#### Makefile e Launchfile
Non è stato necessario creare un *makefile* poiché Python non ha bisogno di compilazione.

È stato creato un launchfile (chiamato `launchfile.launch`), ma se ne sconsiglia l'uso poiché viene stampato tutto su un'unica console e non risulta ben chiaro da quale nodo provengono le informazioni. È consigliato invece lanciare `roscore` e poi in altri terminali separati lanciare i vari `rosrun homework1 <nome_file>`

#### Screenshot dei nodi in esecuzione:
![alt text](/images/4terminal.png)
