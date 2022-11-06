### Hexlet tests and linter status:
[![Actions Status](https://github.com/sergey-emelyanov/python-project-49/workflows/hexlet-check/badge.svg)](https://github.com/sergey-emelyanov/python-project-49/actions)
<a href="https://codeclimate.com/github/sergey-emelyanov/python-project-49/maintainability"><img src="https://api.codeclimate.com/v1/badges/60465d0e3a0cad1e5d26/maintainability" /></a>

### Links

| Tool                                                                        | Description                                             |
|-----------------------------------------------------------------------------|---------------------------------------------------------|
| [poetry](https://poetry.eustace.io/)                                        | "Python dependency management and packaging made easy"  |
| [flake8](https://flake8.pycqa.org/en/latest/)                               | "Flake8: Your Tool For Style Guide Enforcement"         |


## Install
```
git clone https://github.com/sergey-emelyanov/python-project-49
cd python-project-49
```
+ If you have 'make' utility
```python
make install
make build
make publish
make package-install
```
+ If you don`t, you can use poetry instead of 'make'
```python
poetry install
poetry build
poetry publish --dry-run
python3 -m pip install --user dist/*.whl
```

Use python instead of python3, if you're using Windows


## Usage

* For game even-number: `brain-even`
* For game calculation:  `brain-calc`
* For game greatest common divisor: `brain-gcd`
* For game missing number: `brain-progression`
* For game prime number: `brain-prime`


## Description
___

### **Игра: "Проверка на чётность"**
Суть игры в следующем: пользователю показывается случайное число. И ему нужно ответить yes, если число чётное, или no — если нечётное.
[![asciicast](https://asciinema.org/a/80jFrviGFmHqCPouIp5ZDLaLf.svg)](https://asciinema.org/a/80jFrviGFmHqCPouIp5ZDLaLf)

### **Игра: "Калькулятор"**
Суть игры в следующем: пользователю показывается случайное математическое выражение, например 35 + 16, которое нужно вычислить и записать правильный ответ.
[![asciicast](https://asciinema.org/a/SiWObD4Xj3tO5bFi8j7bN5J3Z.svg)](https://asciinema.org/a/SiWObD4Xj3tO5bFi8j7bN5J3Z)

### **Игра "НОД"**
Суть игры в следующем: пользователю показывается два случайных числа, например, 25 50. Пользователь должен вычислить и ввести наибольший общий делитель этих чисел.
[![asciicast](https://asciinema.org/a/PVEgQzKc5ubHhx7FK3mx4GwrJ.svg)](https://asciinema.org/a/PVEgQzKc5ubHhx7FK3mx4GwrJ)

### **Игра "Арифметическая прогрессия"**
Суть игры в следующем:Показываем игроку ряд чисел, образующий арифметическую прогрессию, заменив любое из чисел двумя точками. Игрок должен определить это число.
[![asciicast](https://asciinema.org/a/gGrgtNqVN1oHZpeR2geFh72uV.svg)](https://asciinema.org/a/gGrgtNqVN1oHZpeR2geFh72uV)

### **Игра "Простое ли число?"**
Суть игры в следующем:Показываем игроку число если это число простое ему ножно ответить yes,если не простое то no.
[![asciicast](https://asciinema.org/a/dO4FRGul0fXMMgx9zBw4M509x.svg)](https://asciinema.org/a/dO4FRGul0fXMMgx9zBw4M509x)
