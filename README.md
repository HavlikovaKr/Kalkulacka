#Kalkulačka v Pythonu

Tento projekt je jednoduchá kalkulačka napsaná v Pythonu, která podporuje základní aritmetické operace: sčítání, odčítání, násobení a dělení. 
Projekt obsahuje také testy napsané pomocí knihovny pytest (využívající @pytest.mark.parametrize), které zajišťují správnou funkčnost jednotlivých funkcí kalkulačky.

Importování knihoven:
Pro použití testů a kalkulačky jsou importovány následující knihovny: import pytest, from src import calculator

Struktura adresářů:
Projekt má následující strukturu:

Kalkulacka/
├── src/
│   ├── __init__.py
│   └── calculator.py
└── tests/
    ├── __init__.py
    └── test_calculator.py
    
src/: Obsahuje hlavní kód kalkulačky.
  calculator.py: Obsahuje implementaci funkcí kalkulačky.

tests/: Obsahuje testy pro kalkulačku.
  test_calculator.py: Obsahuje testovací případy napsané pomocí pytest.

  
