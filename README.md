# word-search
**Prosty skrypt sprawdzający, czy podany string znajduje się na polskiej liście słów do Scrabbli.**

## Co to takiego?

word-search.py jest malutkim skryptem który napisałem w celu łatwiejszego sprawdzania, czy zagrane w Scrabblach słowo jest prawidłowym wyrazem.

Program wczytuje listę wszystkich słów zaczynających się tylko na daną literę (w celu skrócenia czasu ładowania), a następnie przepuszcza ją przez prosty algorytm **wyszukiwania binarnego** aby potwierdzić istnienie słowa w ułamek sekundy.

Jeżeli komputer jest podłączony do internetu, program następnie wysyła zapytanie do serwera [sjp.pl](https://sjp.pl/), oficjalnej internetowej bazy słów do gier takich jak Scrabble albo Literaki, i scrapuje uzyskaną odpowiedź za pomocą **wyrażeń regularnych** aby wyświetlić definicję słowa.

## Wymagania
Skrypt działa wyłącznie w Pythonie 3, który dużo lepiej radzi sobie z polskimi znakami.

## Użycie
W celu użycia skryptu wystarczy uruchomić `python3 word-search.py` w oknie terminalu. Program poprosi o podanie sprawdzanego słowa.

## Linki 
* [Zbiór słów SJP.PL (7.8MB)](https://sjp.pl/slownik/growy/)
