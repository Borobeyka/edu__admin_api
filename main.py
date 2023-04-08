from typing import Dict, List, Optional

from fastapi import FastAPI

from database import dbPG, dbPGcon, dbMG
from models import ItemModel, EmployeeModel


app = FastAPI(
    title="AdminDB API"
)


@app.get("/items")
def get_all_items() -> List[ItemModel]:
    """
    Получение списка товаров
    """
    return [item for item in dbMG.items.find()]


@app.put("/items/add")
def add_item(item: ItemModel):
    """
    Добавление товара в базу данных
    """
    dbMG.items.insert_one(item.dict())
    return {"status": 200}


@app.delete("/items/delete")
def delete_item(title: str) -> Dict[str, str | int]:
    """
    Удаление товара из базы данных
    """
    try:
        dbMG.items.delete_many({
            "title": {
                "$regex": title,
                "$options": "i"
            }
        })
    except Exception:
        return {"status": 404, "msg": "Object not found"}
    else:
        return {"status": 200}


@app.get("/employees")
def get_all_employees() -> List[EmployeeModel]:
    """
    Получение списка сотрудников
    """
    return query_dict("SELECT * FROM employees")


@app.put("/employees/add")
def add_employee(employee: EmployeeModel):
    """
    Добавление сотрудника в базу данных
    """
    dbPG.execute("INSERT INTO employees VALUES (DEFAULT, %s, %s, %s)",
                 (employee.name, employee.surname, employee.phone))
    dbPGcon.commit()
    return {"status": 200}


@app.delete("/employees/delete")
def delete_employee(
    name: Optional[str] = None,
    surname: Optional[str] = None,
    phone: Optional[str] = None
) -> Dict[str, str | int]:
    """
    Удаление сотрудника из базы данных
    """
    dbPG.execute("SELECT * FROM employees WHERE name=%s OR surname=%s OR phone=%s",
                 (name, surname, phone))
    if not dbPG.rowcount:
        return {"status": 404, "msg": "Object not found"}
    dbPG.execute("DELETE FROM employees WHERE name=%s OR surname=%s OR phone=%s",
                 (name, surname, phone))
    dbPGcon.commit()
    return {"status": 200}


def query_dict(query, args=()) -> List[Dict[str, str | int]]:
    dbPG.execute(query, args)
    columns = list(dbPG.description)
    results = []
    for row in dbPG.fetchall():
        row_dict = {}
        for i, col in enumerate(columns):
            row_dict[col.name] = row[i]
        results.append(row_dict)
    return results
