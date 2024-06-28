- Install the Python on the ALT Linux 10
- `source venv/bin/activate` & `sudo apt-get install -y $(cat requirements.txt | xargs)`


There is a start page. It's name `main.py`
# Не согласованные задачи
2024-06-26 пытался согласовать задачи, но в ответ получил `Я вам наврное не подскажу`. \ 
## Задача для согласования
 - `1) получает списки ...` & `2) делает сравнение полученных списков ...`
 - `делает сравнение полученных списков пакетов`
 - `- все пакеты, которые есть в p10 но нет в sisyphus`
 - `- все пакеты, version-release которых больше в sisyphus чем в p10`
### Вопросы без ответа 
 `1) получает списки ...` & `2) делает сравнение полученных списков ...` \
Вопрос. "Сравниваем два списка друг с другом или каждый по отдельности?" \
Сравнение проводил двух списком, как и сказано в задаче 2

За пакет принимаем словарь. 1 словарь есть 1 пакет. Если словарь не является пакетом , то уточнения в задачи не было. \
Далее \
"По какому свойству/строке пакета проводить сравнение на наличие в списке?"
Сравнение проводил по свойству `name`.

Далее \
`- все пакеты, version-release которых больше в sisyphus чем в p10` В словаре нет ключа `version-release`. \
Фраза `которых больше` говорит про количество. Значит по какому-то свойству надо сравнить количество. \
Вопрос. "По какому свойству если ключа `version-release` в словаре нет?" \
Сравнил по свойству `name`.

Далее \
`Сравнение version-release согласно ....` тут говориться об УСЛВИИИ для сравнения версии. \
Только вот самой задачи - `сравнивать версии` - НЕТУ.
Вопрос. "В задаче `- все пакеты, version-release которых больше ...` сравниваем количество или все же версии?"
Если сравнивать версии то код примерно такой
```python
import rpm

def compare_versions(v1, r1, v2, r2):
    """
    Сравнивает версии и релизы RPM-пакетов.
    
    Args:
        v1 (str): Версия первого пакета.
        r1 (str): Релиз первого пакета.
        v2 (str): Версия второго пакета.
        r2 (str): Релиз второго пакета.
    
    Returns:
        int: 0, если версии и релизы равны; 1, если первый пакет новее; -1, если второй пакет новее.
    """
    result = rpm.labelCompare((v1, r1), (v2, r2))
    return result

# Пример использования
print(compare_versions("2.1.0", "3", "2.0.5", "1"))  # Вывод: 1
print(compare_versions("1.5.2", "4", "1.5.2", "3"))  # Вывод: 1
print(compare_versions("3.2.1", "1", "3.2.1", "1"))  # Вывод: 0

```

Так как остался без уточнения, для выполнения просто взял и сравнил количество пакетов по свойству `name`


# Тестовое задание Python
Only two API-url for under the each run. \

This is module with two classes:
 - `BasicBranches` - this's checks for an API-url.  
 - `Postmen` - it's performs the all conditions.

### Conditions
1) получает списки бинарных пакетов ветки sisyphus и p10
2) делает сравнение полученных списков пакетов и выводит JSON (структуру нужно придумать), в котором будет отображено:
   - все пакеты, которые есть в p10 но нет в sisyphus
   - все пакеты, которые есть в sisyphus но их нет в p10
   - все пакеты, version-release которых больше в sisyphus чем в p10



#### Note
Refresh variables/code from the `sorter_data` and `filtering_data`. \
The `PACKAGES_SISYPHUS` and `PACKAGES_P10` delete.

## Review
I'm want to say what can't understand the task under number two. \ 
 - `- все пакеты` i take the one package that is the one dictionary.
 - `есть в p10 но нет в sisyphus` If package's list a `p10` has a key \
 `'name'` and list `sisyphus` does not have that key, it's True.  
 - `все пакеты, version-releas`  We gets lists - `sisyphus` and 'p10'. \
   Then:
    - searching a dingle key from the all lists.
    -  calculate quantity the every key from the evry lists
    - result that is list all dictionareis. It's dictionary for insert to the result if \
     quantity the key of the `sisyphus` more then quantity that key from the `p10`

