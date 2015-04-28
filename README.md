# tinkoff_bravo_picker
Командочка, для клиентов Тинькофф банка. Позволяет выбрать операции для компенсации, потратив при этом максимальное количество баллов Браво.

## Использование:
```bash
python tinkoff_bravo_picker.py --points=${points} --transactions=${transactions} --hidden
```
Где points — кол-во доступных баллов Браво
transactions — операции для компенсации через запятую (только сумма баллов)
