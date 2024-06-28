- Install the Python on the ALT Linux 10
- `source venv/bin/activate` & `sudo apt-get install -y $(cat requirements.txt | xargs)`


There is a start page. It's name `main.py`



## Тестовое задание Python
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

